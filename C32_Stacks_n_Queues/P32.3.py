# Window of size w, return count of viewer type v in [t - w, t]
# Dict of { "viewer type": queue[] }, need per-type counts + FIFO removal of expired timestamps
# join(t, v): append t to queue[v]
# get_viewers(t, v): pop left while front < t - window, return len
# Edge: v not in dict, return 0
# 
# n: number of join calls
# T: O(n) - queue operations are O(1), but the while loop could pop up to n items in worst case
# S: O(n) - the queues store at most n timestamp total

from collections import deque, defaultdict

class ViewerCounter:
    def __init__(self, window):
        self.window = window
        self.queue = defaultdict(deque)
    
    def join(self, time, viewer):
        self.queue[viewer].append(time)
    
    def get_viewers(self, time, viewer):
        q = self.queue[viewer]
        while q and q[0] < time - self.window:
            q.popleft()
        return len(q)

# slightly better
# class ViewerCounter:
#     def __init__(self, window):
#         self.window = window
#         self.queue = defaultdict(deque)
    
#     def _remove_expired(self, time):
#         for q in self.queue.values():
#             while q and q[0] < time - self.window:
#                 q.popleft()
            
#     def join(self, time, viewer):
#         self._remove_expired(time)
#         self.queue[viewer].append(time)
    
#     def get_viewers(self, time, viewer):
#         self._remove_expired(time)
#         return len(self.queue[viewer])



# # Viewer Counter Class

# Streamers make money based on the number of views they receive while streaming. Implement a `ViewerCounter` class that tracks the number of viewers within a configurable time window for a live stream event. Viewer types may be "guest", "follower", or "subscriber".

# ViewerCounter:
#   __init__(window): establishes a window size ≥ 1.
#   join(t, v): registers that a viewer of type v joined at time t.
#   get_viewers(t, v): gets the viewer count of viewer type v within the time window of length 'window' ending at timestamp t: [t - window, t], with both endpoints included.

# Both methods accept a timestamp `t` represented by an integer. It is guaranteed that each method call receives a time that is greater than or equal to any timestamp used in previous calls to either `join()` or `get_viewers()`.

# Example:
# counter = ViewerCounter(10)
# counter.join(1, "subscriber")
# counter.join(1, "guest")
# counter.join(2, "follower")
# counter.join(2, "follower")
# counter.join(2, "follower")
# counter.join(3, "follower")
# counter.get_viewers(10, "subscriber")  # Returns 1
# counter.get_viewers(10, "guest")       # Returns 1
# counter.get_viewers(10, "follower")    # Returns 4
# counter.get_viewers(13, "follower")    # Returns 1

# Constraints:

# - The number of `join` and `get_viewers` operations is at most `10^5`
# - `1 ≤ window ≤ 10^5`



# print(counter.get_viewers(10, "subscriber"))  # Returns 1
# print(counter.get_viewers(10, "guest"))       # Returns 1
# print(counter.get_viewers(10, "follower"))    # Returns 4
# print(counter.get_viewers(13, "follower"))    # Returns 1