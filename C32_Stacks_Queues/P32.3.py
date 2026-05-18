# Problem 32.3 - Viewer Counter Class
# Implement a ViewerCounter class that tracks the number of viewers within a
# configurable time window for a live stream event.
# Viewer types: "guest", "follower", or "subscriber".
#
# API:
# - __init__(window): establishes a window size >= 1
# - join(t, v): registers that a viewer of type v joined at time t
# - get_viewers(t, v): gets viewer count of type v within [t - window, t]
#
# Timestamps are integers, guaranteed non-decreasing across all calls.
#
# Example:
# counter = ViewerCounter(10)
# counter.join(1, "subscriber")
# counter.join(1, "guest")
# counter.join(2, "follower")
# counter.join(2, "follower")
# counter.join(2, "follower")
# counter.join(3, "follower")
# counter.get_viewers(10, "subscriber")  # 1
# counter.get_viewers(10, "guest")       # 1
# counter.get_viewers(10, "follower")    # 4
# counter.get_viewers(13, "follower")    # 1
#
# Constraints:
# - Number of join and get_viewers operations <= 10^5
# - 1 <= window <= 10^5