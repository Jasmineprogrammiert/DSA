# Problem 31.4 - Spreadsheet
# Design a Spreadsheet class with the following API:
# - new(rows, cols): initialize with given size, all cells = 0
# - set(row, col, value): set cell at (row, col) to value
# - get(row, col): get value at (row, col)
# - sort_columns_by_row(row): sort all columns based on values in given row (stable)
# - sort_rows_by_column(col): sort all rows based on values in given column (stable)
#
# Rows and columns start at 0. Assume no rows or columns will be out of bounds.
#
# Constraints:
# - 1 <= rows, cols <= 100
# - cell values between -10^9 and 10^9