#!/usr/bin/env python3
"""Read and edit a Google Sheet from the command line.

Talks to the Sheets REST API directly over HTTPS using only the standard
library, and reuses the OAuth plumbing in gdoc.py (same client, same token
store). Exists for the same reason gdoc.py does: the Google-hosted MCP
servers and Claude Code's MCP client disagree about transport.

    tools/gsheet.py auth                          one-time (shared with gdoc.py)
    tools/gsheet.py tabs   <sheetId>              list tabs, sizes, sheetIds
    tools/gsheet.py read   <sheetId> [range]      dump values as TSV
    tools/gsheet.py write  <sheetId> <range> <f>  overwrite a range from JSON
    tools/gsheet.py append <sheetId> <range> <f>  append rows after the table
    tools/gsheet.py clear  <sheetId> <range>      empty a range, keep formatting
    tools/gsheet.py batch  <sheetId> <f>          raw spreadsheets.batchUpdate

<range> is A1 notation: "Notes!A1:D20", or just "Notes" for a whole tab.
<f> is a JSON file holding a 2-D array of rows, or "-" to read stdin.
Values go in as USER_ENTERED (formulas and dates are parsed); pass --raw for
literal strings.

Formatting, column widths, conditional formats, adding or deleting tabs all
live in `batch` — a JSON array of Request objects, same shape as gdoc.py's.
"""

import json
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gdoc  # noqa: E402  - shares credentials, token refresh, and api()

SHEETS_API = "https://sheets.googleapis.com/v4/spreadsheets"


def _rng(r):
    return urllib.parse.quote(r, safe="")


def _rows(path):
    text = sys.stdin.read() if path == "-" else open(path).read()
    rows = json.loads(text)
    if not isinstance(rows, list) or (rows and not isinstance(rows[0], list)):
        sys.exit("Expected a JSON 2-D array of rows, e.g. [[\"a\",1],[\"b\",2]]")
    return rows


def cmd_tabs(sheet_id):
    meta = gdoc.api(
        "GET",
        "%s/%s?fields=properties.title,sheets.properties" % (SHEETS_API, sheet_id),
        gdoc.access_token(),
    )
    print(meta.get("properties", {}).get("title", "(untitled)"))
    for s in meta.get("sheets", []):
        p = s["properties"]
        g = p.get("gridProperties", {})
        print(
            "  %-28s sheetId=%-12s %sx%s"
            % (p["title"], p["sheetId"], g.get("rowCount", "?"), g.get("columnCount", "?"))
        )


def cmd_read(sheet_id, rng):
    url = "%s/%s/values/%s" % (SHEETS_API, sheet_id, _rng(rng))
    res = gdoc.api("GET", url, gdoc.access_token())
    for row in res.get("values", []):
        print("\t".join(str(c) for c in row))


def cmd_write(sheet_id, rng, path, raw):
    url = "%s/%s/values/%s?valueInputOption=%s" % (
        SHEETS_API,
        sheet_id,
        _rng(rng),
        "RAW" if raw else "USER_ENTERED",
    )
    res = gdoc.api("PUT", url, gdoc.access_token(), {"values": _rows(path)})
    print("updated %s cells in %s" % (res.get("updatedCells"), res.get("updatedRange")))


def cmd_append(sheet_id, rng, path, raw):
    url = "%s/%s/values/%s:append?valueInputOption=%s&insertDataOption=INSERT_ROWS" % (
        SHEETS_API,
        sheet_id,
        _rng(rng),
        "RAW" if raw else "USER_ENTERED",
    )
    res = gdoc.api("POST", url, gdoc.access_token(), {"values": _rows(path)})
    u = res.get("updates", {})
    print("appended %s cells at %s" % (u.get("updatedCells"), u.get("updatedRange")))


def cmd_clear(sheet_id, rng):
    url = "%s/%s/values/%s:clear" % (SHEETS_API, sheet_id, _rng(rng))
    res = gdoc.api("POST", url, gdoc.access_token(), {})
    print("cleared %s" % res.get("clearedRange"))


def cmd_batch(sheet_id, path):
    payload = json.load(sys.stdin if path == "-" else open(path))
    if isinstance(payload, dict):
        payload = payload.get("requests", [])
    res = gdoc.api(
        "POST",
        "%s/%s:batchUpdate" % (SHEETS_API, sheet_id),
        gdoc.access_token(),
        {"requests": payload},
    )
    print(json.dumps(res, indent=2)[:2000])


def main():
    args = [a for a in sys.argv[1:] if a != "--raw"]
    raw = "--raw" in sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd = args[0]
    if cmd == "auth":
        gdoc.cmd_auth()
    elif cmd == "tabs" and len(args) >= 2:
        cmd_tabs(args[1])
    elif cmd == "read" and len(args) >= 2:
        cmd_read(args[1], args[2] if len(args) > 2 else "A1:ZZ")
    elif cmd == "write" and len(args) >= 4:
        cmd_write(args[1], args[2], args[3], raw)
    elif cmd == "append" and len(args) >= 4:
        cmd_append(args[1], args[2], args[3], raw)
    elif cmd == "clear" and len(args) >= 3:
        cmd_clear(args[1], args[2])
    elif cmd == "batch" and len(args) >= 3:
        cmd_batch(args[1], args[2])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()