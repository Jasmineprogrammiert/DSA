# tracks the number of viewers within a configurable time window for a live stream event. Viewer types may be "guest", "follower", or "subscriber".
# each method call receives a time that is greater than or equal to any timestamp used in previous calls to either `join()` or `get_viewers()`.

# window = 10
# timestamps = {
#     subscriber: [1],
#     guest: [1],
#     follower: [2, 2, 2, 3],
# }
# get_viewers(13, follower): edge = 13 - 10 = 3, pop the front while < 3 -> [3], count 1

# n: number of join calls
# T: O(1) amortized per call - each timestamp is appended once and popped at most once
# S: O(n) - the queues hold at most n timestamps; the dict has at most 3 keys

from collections import defaultdict, deque

class ViewerCounter:
    def __init__(self, window):
        self.window = window
        self.timestamps = defaultdict(deque)

    def join(self, time, viewer):
        self.timestamps[viewer].append(time)

    def get_viewers(self, time, viewer):
        q = self.timestamps[viewer]
        while q and q[0] < time - self.window:
            q.popleft()
        return len(q)


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