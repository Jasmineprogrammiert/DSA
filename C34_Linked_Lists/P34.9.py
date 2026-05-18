# Problem 34.9 - Doubly Linked List To Array
# Given a non-null node from a doubly linked list (which might or might not be
# the head), return an array with the values from head to tail.
#
# Example 1:
# null <-> 1 <-> 2 <-> 3 <-> 4 <-> null
# node = pointer to node at index 2
# Output: [1, 2, 3, 4]
#
# Example 2:
# null <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> null
# node = pointer to node at index 0
# Output: [1, 2, 3, 4, 5]
#
# Constraints:
# - Create Node class with integer val field and prev and next pointers
# - Up to 10^5 nodes