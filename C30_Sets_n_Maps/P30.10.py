# string  open/close  num
# (agent, action, ticket_number)

# return all ticket_number with anomalies, in any order
# without anomalies:
#   1. opened and closed once, in order
#       - on OPEN: is ticket in seen(set)?
#       - on CLOSE: is ticket in opened(map(ticket: agent))?
#   2. same opening and closing agent
#       - on CLOSE: opened[ticket] = agent
#   3. The agent didn't do any action for a different ticket between opening and closing
#       - agent_open[agent] = ticket

# log = [
    # ["Dwight", "close", 2],
    # ["Dwight", "open", 2],
    # ["Drew", "open", 32],
    # ["Drew", "close", 32],
    # ["Drew", "open", 32],
    # ["Drew", "close", 32],
    # ["Susa", "open", 7],
    # ["Jo", "close", 7],
    # ["Susa", "open", 33],
    # ["Jo", "open", 8],
    # ["Jo", "open", 36],
    # ["Jo", "close", 8],
    # ["Susa", "close", 33]
# ]
#       [2, 32, 7, 8, 36]
# res = {2, 32, 7, 8, 36} -> turn to arr
# seen = {}
# opened = {}
# agent_open = {}

# n: length of log
# T: O(n) - each item in the log is iterated once, then opened is iterated once at the end. Operations like add, lookup and update take O(1) time
# S: O(n) - res, seen, opened hold at most one entry per ticket; agent_open one per agent. Both <= n

def action_log_anomalies(log):
    res = set()
    seen = set()
    opened = dict()
    agent_open = dict()
    
    for agent, action, ticket in log:
        if agent in agent_open and agent_open[agent] != ticket:
            res.add(agent_open[agent])
        if ticket in res:
            continue

        if action == "open":
            if ticket in seen:
                res.add(ticket)
            else:
                seen.add(ticket)
                opened[ticket] = agent
                agent_open[agent] = ticket
        else:
            if ticket not in opened or agent != opened[ticket]:
                res.add(ticket)
            else:
                del opened[ticket]
                del agent_open[agent]
                
    res.update(opened.keys())

    return list(res)


# # Action Log Anomalies

# You are given an action log, `log`, from a tech support system. Each entry is a tuple `[agent, action, ticket_number]`, where the ticket number is a positive integer, the agent is a string, and the action is `"open"` or `"close"`. The log is sorted chronologically.

# Your goal is to find all the tickets with _anomalies_, in any order. A ticket **doesn't** have anomalies if:

# - It is opened and closed once, in that order.
# - The opening and closing agent is the same.
# - The agent didn't do any action for a different ticket between opening and closing.

# Example 1: log = [
    # ["Dwight", "close", 2],
    # ["Dwight", "open", 2],
    # ["Drew", "open", 32],
    # ["Drew", "close", 32],
    # ["Drew", "open", 32],
    # ["Drew", "close", 32],
    # ["Susa", "open", 7],
    # ["Jo", "close", 7],
    # ["Susa", "open", 33],
    # ["Jo", "open", 8],
    # ["Jo", "open", 36],
    # ["Jo", "close", 8],
    # ["Susa", "close", 33]
# ]
# Output: [2, 32, 7, 8, 36]
# Explanation:
# - 2 was closed before it was opened.
# - 32 was opened multiple times.
# - 7 was opened and closed by different agents.
# - 8 was opened and closed, but the agent did something in between.
# - 36 was not closed.

# Example 2: log = [["Alice", "open", 1], ["Alice", "close", 1]]
# Output: []
# Explanation: The ticket was opened and closed once, in order, by the same agent.

# Example 3: log = [["Alice", "open", 1], ["Alice", "open", 1]]
# Output: [1]
# Explanation: The ticket was opened multiple times.

# Example 4: log = [
#     ["Drew", "open", 32],
#     ["Drew", "close", 2],
#     ["Drew", "close", 32]
# ]
# Output: [2, 32]
# Explanation:
# - 2 was closed without being opened
# - 32 was opened but Drew did another action (closing ticket 2) before closing it

# Example 5: log = [
#     ["Dwight", "close", 2],
#     ["Dwight", "open", 2],
#     ["Drew", "open", 32],
#     ["Drew", "open", 2],
#     ["Drew", "close", 32]
# ]
# Output: [2, 32]
# Explanation:
# - 2 was closed before being opened, and later opened by a different agent
# - 32 was opened but Drew did another action (opening ticket 2) before closing it


# Constraints:

# - `0 ≤ log.length ≤ 10^5`
# - Each `ticket_number` is a positive integer less than `10^6`
# - Each `agent` is a non-empty string
# - Each `action` is either `"open"` or `"close"`
# - The log is sorted chronologically

# Acknowledgements: Thanks to a reader for Examples 4 and 5.