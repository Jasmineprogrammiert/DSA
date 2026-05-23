# ============================================================
# Question 1 - Case Insensitive Sort
# Given an array of strings, sort lexicographically (dictionary
# order) in descending order, ignoring case.
# ============================================================
def case_insensitive_sort(arr):
    return sorted(arr, key=str.lower, reverse=True)

print(case_insensitive_sort(["apple", "Banana", "3", "Cherry", "42", "GRAPE", "10"]))
# ['GRAPE', 'Cherry', 'Banana', 'apple', '42', '3', '10']


# ============================================================
# Question 2 - Sort by Element at Index
# Given an array of intervals, where each interval is a start
# value and an end value, sort the intervals by the end value.
# ============================================================
def sort_by_element_at_index(arr):
    return sorted(arr, key=lambda elem: elem[1])

print(sort_by_element_at_index([[3,9], [1,4], [4,7], [2,3]]))
# [[2,3], [1,4], [4,7], [3,9]]


# ============================================================
# Question 3 - Sort by Field
# Given an array, deck, of objects of the Card class, representing 
# a deck of playing cards:
#   class Card:
#     def __init__(self, value, suit):
#       self.value = value # A number between 1 and 13.
#       self.suit = suit   # 'clubs', 'hearts', 'spades', or 'diamonds'
#
# Sort the cards by value in ascending order. A card's value is
# between 1-13 (1=Ace, 11=Jack, 12=Queen, 13=King). When
# values are the same, break tie with suit:
# Clubs < Hearts < Spades < Diamonds.
# ============================================================
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return f"({self.value}, '{self.suit}')"

def sort_by_field(deck):
    suit_order = {'clubs': 0, 'hearts': 1, 'spades': 2, 'diamonds': 3}
    return sorted(deck, key=lambda card: (card.value, suit_order[card.suit]))

print(sort_by_field([Card(8, "hearts"), Card(8, "clubs"), Card(3, "clubs"), Card(3, "hearts")]))
# [(3, 'clubs'), (3, 'hearts'), (8, 'clubs'), (8, 'hearts')]


# ============================================================
# Question 4 - New Deck Order
# Given the same deck array, sort in "new deck order" where
# suits are separated in the order:
# Hearts < Clubs < Diamonds < Spades,
# and each suit is sorted from Ace to King (low to high).
# ============================================================
def new_deck_order(deck):
    suit_order = {'hearts': 0, 'clubs': 1, 'diamonds': 2, 'spades': 3}
    return sorted(deck, key=lambda card: (card.value, suit_order[card.suit]))

print(new_deck_order([Card(8, "hearts"), Card(8, "clubs"), Card(3, "clubs"), Card(3, "hearts")]))
# [(3, 'hearts'), (8, 'hearts'), (3, 'clubs'), (8, 'clubs')]


# ============================================================
# Question 5 - Stable Sorting
# Given the same deck array, sort by value preserving the relative
# order of the cards for each value. A sorting algorithm that breaks ties by the input order is called stable.
# ============================================================
def stable_sorting(deck):
    return sorted(deck, key=lambda card: card.value)

print(stable_sorting([Card(9, "clubs"), Card(4, "spades"), Card(4, "clubs")]))
# [(4, 'spades'), (4, 'clubs'), (9, 'clubs')]