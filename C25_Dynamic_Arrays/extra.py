def pop(self, i): 
    if i < 0 or i >= self._size:
        raise IndexError('Index out of bounds!')
    
    remove_ele = self.get(i)

    for index in range(i, self._size -1):
        self.set(index, self.get(index + 1))
    self._size -= 1

    return remove_ele
  
# # Extra Dynamic Array Operations

# In this problem, we are building off of an existing dynamic array data structure, which already has `append`, `pop_back`, `set`, `get`, and `size` methods, and adding additional methods. Please refer to the [Implement Dynamic Array](https://bctci.co/implement-dynamic-array) problem first.

# Add the following methods:

# 1. `pop(i)`: Removes the element at index `i`. Every element after that index should be shifted left by one index so that there are no gaps remaining in the fixed-size array. Returns the element removed.

# 2. `contains(x)`: Takes an element and returns whether the element appears in the array.

# 3. `insert(i, x)`: Takes an index and an element and adds the element at that index, shifting right any preexisting elements at index `i` or greater.

# 4. `remove(x)`: Takes in an element and removes the first instance of that element in the array. Returns the index that the element was at or `-1` if the element was not found.

# Example 1:
# d = DynamicArrayExtras()
# d.append(1)
# d.append(2)
# d.append(3)
# d.pop(1)  # returns 2
# d.get(1)  # returns 3
# d.size()  # returns 2

# Example 2:
# d = DynamicArrayExtras()
# d.append(1)
# d.append(2)
# d.contains(1)  # returns True
# d.contains(3)  # returns False

# Example 3:
# d = DynamicArrayExtras()
# d.append(1)
# d.append(2)
# d.insert(1, 3)  # array becomes [1,3,2]
# d.get(1)  # returns 3

# Example 4:
# d = DynamicArrayExtras()
# d.append(1)
# d.append(2)
# d.append(2)
# d.remove(2)  # returns 1 (first index where 2 appears)
# d.get(1)  # returns 2 (the second 2 shifted left)