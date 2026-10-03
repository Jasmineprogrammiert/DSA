#!/usr/bin/env python3
"""Read and edit a Google Doc from the command line.

Talks to the Docs REST API directly over HTTPS using only the standard
library. Exists because the official Google Docs MCP server and Claude Code's
MCP client disagree about transport: the server always answers POSTs with
`application/json`, the client expects `text/event-stream`, so tool discovery
fails even though auth succeeds.

    tools/gdoc.py auth                    one-time, opens a consent screen
    tools/gdoc.py read  <docId>           dump the document as plain text
    tools/gdoc.py batch <docId> <file>    apply a documents.batchUpdate payload

Sheets live in tools/gsheet.py and share this file's auth, so the scope below
covers Docs, Sheets and Drive metadata (listing and renaming files); re-run
`auth` after changing it.

Credentials live in ~/.config/gdoc/credentials.json (mode 600), outside the
repo -- client id, client secret and refresh token alike, so nothing
identifying is committed. `auth` takes the first two from GOOGLE_CLIENT_ID /
GOOGLE_CLIENT_SECRET, or from a previous auth, or prompts for them. The
refresh token does not expire while the OAuth app stays published
"In production".
"""

import http.server
import json
import os
import secrets
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from getpass import getpass

SCOPE = (
    "https://www.googleapis.com/auth/documents "
    "https://www.googleapis.com/auth/spreadsheets "
    "https://www.googleapis.com/auth/drive.metadata"
)
AUTH_URI = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URI = "https://oauth2.googleapis.com/token"
DOCS_API = "https://docs.googleapis.com/v1/documents"

CRED_DIR = os.path.expanduser("~/.config/gdoc")
CRED_PATH = os.path.join(CRED_DIR, "credentials.json")


def post_form(url, fields):
    body = urllib.parse.urlencode(fields).encode()
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urllib.request.urlopen(req, context=ssl.create_default_context()) as r:
        return json.load(r)


def api(method, url, token, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + token)
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, context=ssl.create_default_context()) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit("API %s: %s" % (e.code, e.read().decode()[:800]))


class Catcher(http.server.BaseHTTPRequestHandler):
    """Single-shot loopback listener for the OAuth redirect."""

    result = {}

    def do_GET(self):
        self.server.query = urllib.parse.parse_qs(
            urllib.parse.urlparse(self.path).query
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(
            b"<h2>Authorized.</h2><p>Close this tab and return to the terminal.</p>"
        )

    def log_message(self, *args):
        pass


def stored(key):
    """Reuse a value from a previous auth, so re-consent needs no TTY."""
    try:
        with open(CRED_PATH) as f:
            return json.load(f).get(key, "")
    except (OSError, ValueError):
        return ""


def cmd_auth():
    client_id = os.environ.get("GOOGLE_CLIENT_ID") or stored("client_id")
    if client_id:
        print("Reusing the client id already in %s" % CRED_PATH)
    else:
        client_id = input(
            "Paste the OAuth client id (ends .apps.googleusercontent.com): "
        ).strip()
    if not client_id:
        sys.exit("No client id given.")

    secret = os.environ.get("GOOGLE_CLIENT_SECRET") or stored("client_secret")
    if secret:
        print("Reusing the client secret already in %s" % CRED_PATH)
    else:
        secret = getpass(
            "Paste the OAuth client secret (starts GOCSPX-, input hidden): "
        ).strip()
    if not secret:
        sys.exit("No client secret given.")

    server = http.server.HTTPServer(("127.0.0.1", 0), Catcher)
    redirect_uri = "http://127.0.0.1:%d/" % server.server_port
    state = secrets.token_urlsafe(16)

    url = AUTH_URI + "?" + urllib.parse.urlencode(
        {
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "response_type": "code",
            "scope": SCOPE,
            "access_type": "offline",
            "prompt": "consent",
            "state": state,
        }
    )

    print("\nOpen this URL and approve access:\n\n%s\n" % url)
    print("(An 'unverified app' warning is expected: Advanced -> Go to app.)")
    try:
        webbrowser.open(url)
    except Exception:
        pass

    print("Waiting for the redirect...")
    server.handle_request()
    query = getattr(server, "query", {})
    if query.get("state", [None])[0] != state:
        sys.exit("State mismatch - aborting.")
    code = query.get("code", [None])[0]
    if not code:
        sys.exit("No authorization code received: %r" % query)

    tok = post_form(
        TOKEN_URI,
        {
            "code": code,
            "client_id": client_id,
            "client_secret": secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        },
    )
    if "refresh_token" not in tok:
        sys.exit("No refresh token returned: %s" % json.dumps(tok)[:400])

    os.makedirs(CRED_DIR, exist_ok=True)
    with open(CRED_PATH, "w") as f:
        json.dump(
            {
                "client_id": client_id,
                "client_secret": secret,
                "refresh_token": tok["refresh_token"],
            },
            f,
            indent=2,
        )
    os.chmod(CRED_PATH, 0o600)
    print("Saved credentials to %s" % CRED_PATH)


def access_token():
    if not os.path.exists(CRED_PATH):
        sys.exit("No credentials. Run: tools/gdoc.py auth")
    with open(CRED_PATH) as f:
        c = json.load(f)
    tok = post_form(
        TOKEN_URI,
        {
            "client_id": c["client_id"],
            "client_secret": c["client_secret"],
            "refresh_token": c["refresh_token"],
            "grant_type": "refresh_token",
        },
    )
    if "access_token" not in tok:
        sys.exit("Refresh failed: %s" % json.dumps(tok)[:400])
    return tok["access_token"]


def walk_text(elements, out):
    """Collect text runs, tagging each with its start index."""
    for el in elements:
        if "paragraph" in el:
            for run in el["paragraph"].get("elements", []):
                text = run.get("textRun", {}).get("content")
                if text:
                    out.append((run["startIndex"], text))
        elif "table" in el:
            for row in el["table"].get("tableRows", []):
                for cell in row.get("tableCells", []):
                    walk_text(cell.get("content", []), out)
        elif "tableOfContents" in el:
            walk_text(el["tableOfContents"].get("content", []), out)


def cmd_read(doc_id, show_index):
    doc = api("GET", "%s/%s" % (DOCS_API, doc_id), access_token())
    runs = []
    walk_text(doc.get("body", {}).get("content", []), runs)
    if show_index:
        for start, text in runs:
            print("%6d  %s" % (start, text.rstrip("\n")))
    else:
        sys.stdout.write("".join(text for _, text in runs))


def cmd_batch(doc_id, payload_path):
    with open(payload_path) as f:
        requests = json.load(f)
    if isinstance(requests, dict):
        requests = requests.get("requests", [])
    res = api(
        "POST",
        "%s/%s:batchUpdate" % (DOCS_API, doc_id),
        access_token(),
        {"requests": requests},
    )
    print(json.dumps(res, indent=2)[:2000])


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd = args[0]
    if cmd == "auth":
        cmd_auth()
    elif cmd == "read" and len(args) >= 2:
        cmd_read(args[1], "--index" in args)
    elif cmd == "batch" and len(args) >= 3:
        cmd_batch(args[1], args[2])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()