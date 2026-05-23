# n: number of rows
# m: number of columns
# T: 
#   O(m log m + n * m) - sort_columns_by_row sorts and rebuilds grid
#   O(n log n) - sort_rows_by_column sorts rows in-place
# S: 
#   O(n * m) - sort_columns_by_row rebuilds grid
#   O(1) - sort_rows_by_column sorts in-place
class Spreadsheet:
    def __init__(self):
        self.spreadsheet = []
    
    def new(self, rows, cols):
        self.spreadsheet = [[0] * cols for _ in range(rows)]
        
    def set(self, row, col, val):
        self.spreadsheet[row][col] = val
    
    def get(self, row, col):
        return self.spreadsheet[row][col]
    
    def sort_columns_by_row(self, row):
        # 1. get the sorted column order
        sorted_row = sorted(enumerate(self.spreadsheet[row]), key=lambda pair: pair[1])
        
        # 2. rearrange each row according to the sorted column order
        new_spreadsheet = []
        for r in range(len(self.spreadsheet)):
            new_row = []
            for idx, _ in sorted_row:
                new_row.append(self.spreadsheet[r][idx])
            new_spreadsheet.append(new_row)
        self.spreadsheet = new_spreadsheet
    
    def sort_rows_by_column(self, col):
        self.spreadsheet.sort(key=lambda row: row[col])



# # Spreadsheet

# Design a class called Spreadsheet with the following API. Spreadsheets have between `1` and `100` rows and columns. The values at each cell are integers.

# Spreadsheet API:

# - `new(rows, cols)`: initializes a spreadsheet with the specified size and 0 in every cell.
# - `set(row, col, value)`: sets the cell at (row, col) to value.
# - `get(row, col)`: gets the value at (row, col).
# - `sort_columns_by_row(row)`: sorts all the columns based on the values in the given row. Sorting should be stable.
# - `sort_rows_by_column(col)`: sorts all the rows based on the values in the given column. Sorting should be stable.

# Rows and columns start at `0`. Assume that no rows or columns will be out of bounds.

# Example 1:
spreadsheet = Spreadsheet()
spreadsheet.new(3, 3)
spreadsheet.set(0, 0, 5)
spreadsheet.set(0, 1, 3)
spreadsheet.set(0, 2, 8)
spreadsheet.set(1, 0, 6)
spreadsheet.set(2, 1, 1)
spreadsheet.sort_columns_by_row(0)
spreadsheet.sort_rows_by_column(1)
spreadsheet.get(1, 1)  # Returns 5

# Example 2:
# spreadsheet = Spreadsheet()
# spreadsheet.new(1, 1)
# spreadsheet.set(0, 0, 42)
# spreadsheet.get(0, 0)  # Returns 42

# Example 3:
# spreadsheet = Spreadsheet()
# spreadsheet.new(3, 2)
# spreadsheet.sort_rows_by_column(0)
# spreadsheet.get(0, 0)  # Returns 0

# Here is a visualization of Example 1:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/sorting-fig6.png

# Constraints:

# - `1 ≤ rows, cols ≤ 100`
# - All values set in cells are integers between `-10^9` and `10^9`