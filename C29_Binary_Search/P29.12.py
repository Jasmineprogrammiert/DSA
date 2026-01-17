# Goal: Find the picture where the number of 1's is closest to O's
# Binary search the picture to find the transition point between 'low tide' (< 50%) and 'high tide' (>= 50%),
# then check the two pictures at the transition point (the last l and first r).
# Choose the last l if they're even, otherwise choose the one with the smallest absolute difference from n^2 / 2

# k: the number of pictures
# n: the dimension of the grid
# T: O(log k * (n log n))
# S: O(1)

# 1. The 'Horizontal' Search: inside one row, binary search to find the 1-to-0 transition. Cost: log n
# 2. The 'Vertical' Sum: to get the total water in one picture, do the horizontal search for every single row: n * log n
# 3. The 'Time' Search: to find the right picture in the chronological list, need to binary search the picture. log k
# When 'Time' search is applied on top of the 'Picture' search, they're multiplied and thus: O(log k * (n log n))

def tide_aerial_view(pictures, n):
    mid_point = (n ** 2) / 2
    
    # LEVEL 1: The Row Counter - O(log n)
    def get_ones_in_row(row):
        if row[0] == 0: return 0
        if row[-1] == 1: return n
        
        l, r = 0, n - 1
        while r - l > 1:
            mid = (l + r) // 2
            if row[mid] == 1:
                l = mid
            else:
                r = mid
        return r # Index of the first 0 = count of 1s
    
    # LEVEL 2: The Picture Counter - O(n log n)
    def get_ones_in_picture(pic_index):
        total = 0
        for row in pictures[pic_index]:
            total += get_ones_in_row(row)
        return total
    
    # LEVEL 3: The Recipe Abstration - O(n log n)
    def is_before(pic_index):
        return get_ones_in_picture(pic_index) < mid_point
    
    # LEVEL 4: The Main Search - O(log k) * O(n log n)
    l, r = 0, len(pictures) - 1
    
    # Boundary Checks (Safety)
    if not is_before(l): return l
    if is_before(r): return r
    
    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
    
    # Final Tie-Breaker
    l_water = get_ones_in_picture(l)
    r_water = get_ones_in_picture(r)
    if abs(l_water - mid_point) <= abs(r_water - mid_point):
        return l
    else:
        return r
 
# def tide_aerial_view(pictures, n):
#     mid_point = (n ** 2) / 2
    
#     def count_ones(pic_index):
#         count = 0
#         for row in pictures[pic_index]:
#             for cell in row:
#                 if cell == 1: count += 1
#         return count
    
#     def is_before(pic_index):
#         return count_ones(pic_index) < mid_point
    
#     l, r = 0, len(pictures) - 1
#     while r - l > 1:
#         mid = (l + r) // 2
#         if is_before(mid):
#             l = mid
#         else:
#             r = mid
    
#     l_water = count_ones(l)
#     r_water = count_ones(r)
#     if abs(l_water - mid_point) <= abs(r_water - mid_point):
#         return l
#     else:
#         return r

# print(tide_aerial_view([
#     [[0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]],

#     [[1, 0, 0],
#     [0, 0, 0],
#     [1, 0, 0]],

#     [[1, 1, 0],
#     [0, 0, 0],
#     [1, 0, 0]],

#     [[1, 1, 0],
#     [1, 1, 1],
#     [1, 0, 0]],

#     [[1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 0]]
# ], 3))



# # Tide Aerial View

# You are provided a series of aerial-view pictures of the same coastal region, taken a few minutes apart from each other around the time the tide rises. Each picture consists of an nxn binary grid, where `0` represents a part of the region above water, and `1` represents a part below water.

# - The tide appears from the left side and rises toward the right, so, in each picture, for each row, all the 1's will be before all the 0's.
# - Once a region is under water, it stays under water.
# - All pictures are different.

# Determine which picture shows the most even balance between regions above and below water (i.e., where the number of 1's most closely equals the number of 0's). In the event of a tie, return the earliest picture.

# Example 1:

# Picture 0:
# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 0]
# Picture 1:
# [1, 0, 0]
# [0, 0, 0]
# [1, 0, 0]
# Picture 2:
# [1, 1, 0]
# [0, 0, 0]
# [1, 0, 0]
# Picture 3:
# [1, 1, 0]
# [1, 1, 1]
# [1, 0, 0]
# Picture 4:
# [1, 1, 1]
# [1, 1, 1]
# [1, 1, 0]

# Output: 2. The pictures at index 2 and 3 are equally far from having 50% water. We break the tie by picking the earlier one, 2.

# Example 2:

# Picture 0:
# [1, 1]
# [1, 1]

# Output: 0. It's the only picture.

# Here is a visualization of Example 1:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/binary-search-fig6.png

# Constraints:

# - `1 ≤ pictures.length ≤ 500`
# - All pictures have dimension `n x n`, where `1 ≤ n ≤ 500`