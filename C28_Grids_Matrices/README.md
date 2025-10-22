# P28.2 Queen's Reach

## How many cells can a queen reach?
Up: r
Down: n - r - 1
Left: c
Right: n - c - 1
Up-Left: min(r, c) 
Up-Right: min(r, n - c - 1)
Down-Left: min(n - r - 1, c)
Down-Right: min(n - r - 1, n - c - 1)

Sum 
= 2*(n-1) + min(r, c) + min(r, n-c-1) + min(n-r-1, c) + min(n-r-1, n-c-1)

The max value for each min(...) occurs when the queen is as close as possible to the center of the board. For a queen near the center, each min(...) is about (n-1) // 2

Thus, the total max reach per queen is about: 4*(n-1) cells

## Naive Upper Bound
There could be up to O(n²) queens on the board
Each queen can mark up to 4*(n-1) cells
This suggests a time complexity of O(n^3)

## Actual Upper bound
Each cell can be reached by at most 8 queens (from 8 directions)
There're O(n^2) cells
Time complexity = O(n^2)
-------------------------------

# Initialize an empty grid
`grid = [[0] * num_cols for _ in range(num_rows)]`

# Copy a grid
`grid = [row.copy() for row in grid]`

> Warning
Initialize an empty grid using `grid = [[0] * num_cols] * num_rows` creates a bug: modifying a value in one row will modify all the rows

Python creates one single inner list [0, 0, ..., 0] of length `num_cols`
Then it repeats references to that same inner list `num_rows` times
i.e. all rows point to the exact same list object in memory
So, if you modify one element in one row, it changes that element in every row because they are all the same list
```
grid = [[0] * 3] * 2
grid[0][0] = 1
print(grid)  # Output: [[1, 0, 0], [1, 0, 0]]
```