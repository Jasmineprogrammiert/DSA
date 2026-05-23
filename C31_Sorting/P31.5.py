# class Book:
#     def __init__(self, title, author, page_count, genre, year_published):
#         self.title = title
#         self.author = author
#         self.page_count = page_count
#         self.genre = genre
#         self.year_published = year_published

#     def __repr__(self):
#         return f'Book("{self.title}", {self.year_published})'
# Above is part of the problem description
# 1. Find the publishing year range
# 2. Create empty buckets
# 3. Place each book into its bucket
# 4. Collect from buckets in order

def sort_by_publication_year(books):
    if not books: return []
    min_year = min(book.year_published for book in books)
    max_year = max(book.year_published for book in books)
    buckets = [[] for _ in range(max_year - min_year + 1)]
    res = []
    
    for book in books:
        buckets[book.year_published - min_year].append(book)
    for bucket in buckets:
        res.extend(bucket)
    return res
# 
# n: length of books
# k: range of publishing years (max_year - min_year + 1)
# T: O(n + k) - O(n) to find min/max and place books, O(k) to iterate buckets
# S: O(n + k) - O(n) for res, O(k) for buckets

# def sort_by_publication_year(books):
#     if not books: return []
#     buckets = {}
#     res = []
    
#     for book in books:
#         if book.year_published not in buckets:
#             buckets[book.year_published] = []
#         buckets[book.year_published].append(book)
#     for year in sorted(buckets):
#         res.extend(buckets[year])
#     return res
# 
# # n: length of books
# # k: number of unique publishing years
# # T: O(n + k log k) - O(n) to place books, O(k log k) to sort dict keys
# # S: O(n + k) - O(n) for res, O(k) for buckets

# print(sort_by_publication_year([
#     Book("Shadow of Tomorrow", "Elliot Greyson", 350, "Science Fiction", 2020),
#     Book("Whispers in the Wind", "Lila Hart", 280, "Romance", 2018),
#     Book("Echoes of Eternity", "Mara Vance", 420, "Fantasy", 2018),
#     Book("Fragments of Dawn", "Cora Blake", 310, "Mystery", 2019),
#     Book("Beneath the Starlit Sky", "Aria Monroe", 270, "Drama", 2020)
# ]))



# # Sort By Publication Year

# You are given an array, `books`, of objects of a `Book` class, where each book has fields `title`, `author`, `page_count`, `genre`, and `year_published`.
      
# Return the books sorted by publication year. It doesn't matter how you break ties.

# Example 1:
# books = [
#   Book("Shadow of Tomorrow", "Elliot Greyson", 350, "Science Fiction", 2020),
#   Book("Whispers in the Wind", "Lila Hart", 280, "Romance", 2018),
#   Book("Echoes of Eternity", "Mara Vance", 420, "Fantasy", 2018),
#   Book("Fragments of Dawn", "Cora Blake", 310, "Mystery", 2019),
#   Book("Beneath the Starlit Sky", "Aria Monroe", 270, "Drama", 2020)
# ]
# Output: [
#   Book("Echoes of Eternity", "Mara Vance", 420, "Fantasy", 2018),
#   Book("Whispers in the Wind", "Lila Hart", 280, "Romance", 2018),
#   Book("Fragments of Dawn", "Cora Blake", 310, "Mystery", 2019),
#   Book("Beneath the Starlit Sky", "Aria Monroe", 270, "Drama", 2020),
#   Book("Shadow of Tomorrow", "Elliot Greyson", 350, "Science Fiction", 2020)
# ]

# Example 2:
# books = []
# Output: []. Empty list is valid input.

# Example 3:
# books = [Book("Solo", "Author", 100, "Genre", 2000)]
# Output: [Book("Solo", "Author", 100, "Genre", 2000)]. Single book is already sorted.

# Constraints:

# - The length of `books` is at most `5 * 10^6`
# - All years are between `1000` and `2025` (inclusive)