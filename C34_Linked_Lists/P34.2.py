# Problem 34.2 - Doubly Linked List Design
# Implement a DoublyLinkedList class with the following methods:
#
# push_front(v): Adds a node with value v at the beginning of the list.
# pop_front(): Removes the node at the beginning and returns its value. Returns None if empty.
# push_back(v): Adds a node with value v at the end of the list.
# pop_back(): Removes the node at the end and returns its value. Returns None if empty.
# size(): Returns the number of nodes in the list.
# contains(v): Returns the first node with value v, or None if not found.
#
# Example 1:
# list = DoublyLinkedList()
# list.push_front(1)  # 1
# list.push_front(2)  # 2<->1
# list.push_back(3)   # 2<->1<->3
# list.contains(2)    # Returns node with value 2
# list.contains(4)    # Returns None
# list.size()         # Returns 3
# list.pop_front()    # Returns 2, list: 1<->3
# list.pop_back()     # Returns 3, list: 1
#
# Example 2:
# list = DoublyLinkedList()
# list.pop_front()    # Returns None
# list.pop_back()     # Returns None
# list.size()         # Returns 0
#
# Constraints:
# - Create Node class with val field and prev and next pointers
# - push_front(), pop_front(), push_back(), pop_back(), and size() should all be O(1)
# - Up to 10^5 nodes