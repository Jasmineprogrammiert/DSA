# ***** Method 1 (better) *****
# res = set() - anomaly
# seen = set()
# opened = dict() <ticket_number, agent> (removed on close)
# agent_open = dict() <agent, ticket_number> (removed on close)
# 
# For each [agent, action, ticket] in log:
#   agent in agent_open on a different ticket? -> add that other ticket to res
#   If ticket already in res -> continue
#
#   If "open":
#       1. ticket in seen? -> anomaly
#       2. Update: 
#           seen.add(ticket), 
#           opened[ticket] = agent, 
#           agent_open[agent] = ticket
#
#   If "close":
#       1. ticket not in opened? -> anomaly
#       2. opened[ticket] != agent? -> anomaly
#       3. Update:
#           del opened[ticket], 
#           del agent_open[agent]
#
# After the loop: any ticket still in opened -> anomaly
# Return list(res)

# n: length of log
# T: O(n) - once pass through log, all dict/set operations are O(1)
# S: O(n) - the set and map each stores at most n entries

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
                continue
            seen.add(ticket)
            opened[ticket] = agent
            agent_open[agent] = ticket
        
        else: # close
            if ticket not in opened or opened[ticket] !=agent:
                res.add(ticket)
                continue
            del opened[ticket]
            del agent_open[agent]
    
    res.update(opened.keys())
    return list(res)

# print(action_log_anomalies([
#     ["Dwight", "close", 2],
#     ["Dwight", "open", 2],
#     ["Drew", "open", 32],
#     ["Drew", "close", 32],
#     ["Drew", "open", 32],
#     ["Drew", "close", 32],
#     ["Susa", "open", 7],
#     ["Jo", "close", 7],
#     ["Susa", "open", 33],
#     ["Jo", "open", 8],
#     ["Jo", "open", 36],
#     ["Jo", "close", 8],
#     ["Susa", "close", 33]
# ]))
    
# ***** Method 2 *****
# res = set() - anomaly
# ticket_map = dict() <ticket_number, [state, agent]> (never removed)
# agent_map = dict() <agent, ticket_number> (removed on close)
#
# For each [agent, action, ticket] in log:
#   agent in agent_map on a different ticket? -> add that other ticket to res
#
#   If "open":
#       1. ticket in ticket_map? -> anomaly
#       2. Update:
#           ticket_map[ticket] = ["open", agent],
#           agent_map[agent] = ticket
#
#   If "close":
#       1. ticket not in ticket_map, or state is "closed"? -> anomaly
#       2. ticket_map[ticket][agent] != agent? -> anomaly
#       3. Update:
#           ticket_map[ticket][state] = "closed",
#           del agent_map[agent]
#
# After the loop: any ticket with state "open" in ticket_map -> anomaly
# Return list(res)



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