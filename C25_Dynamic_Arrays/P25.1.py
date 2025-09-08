class DynamicArray:
    def __init__(self):
        self._size = 0
        self.capacity = 10
        self.arr = [None] * self.capacity

    def append(self, x):
        if self._size == self.capacity:
            self.resize(self.capacity * 2)
            
        self.arr[self._size] = x
        self._size += 1
    
    def get(self, i):
        if i <= self._size - 1 and i >= 0: 
            return self.arr[i]
        raise IndexError('Index out of bounds')
    
    def set(self, i, x):
        if i >= self._size or i < 0: 
            raise IndexError('Index out of bounds')
        self.arr[i] = x
    
    def size(self):
        return self._size

    def pop_back(self):
        if self._size == 0: 
            raise IndexError('Pop from empty array')

        self._size -= 1

        if self._size <= self.capacity * 0.25 and self.capacity > 10:
            self.resize(self.capacity // 2)

    def resize(self, capacity):
        new_arr = [None] * capacity

        i = 0
        while i < self._size:
            new_arr[i] = self.arr[i]
            i += 1
        
        self.arr = new_arr
        self.capacity = capacity

# Algo: dynamic arrays
# n: the length of arr
# T: O(n) for all methods except append and pop_back, which has an amortized time of O(1)
# S: O(n) extra space



# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Implement Dynamic Array

# Assume your programming language only supports fixed-size arrays. Implement a dynamic array data structure that supports the following:

# `Dynamic Array API:`

# - `append(x)`: adds element `x` to the end of the array
# - `get(i)`: returns the element at index `i`
# - `set(i, x)`: updates the preexisting element at index `i` to be `x`
# - `size()`: returns the number of elements in the array
# - `pop_back()`: removes the last element

# You should only declare arrays of a fixed size and not use built-in `append()` methods or equivalent.

# Example 1:
# d = DynamicArray()
# d.append(1)
# d.append(2)
# d.get(0)  # returns 1
# d.get(1)  # returns 2
# d.size()  # returns 2

# Example 2:
# d = DynamicArray()
# d.append(1)
# d.set(0, 10)
# d.get(0)  # returns 10

# Example 3:
# d = DynamicArray()
# d.append(1)
# d.append(2)
# d.pop_back()
# d.size()  # returns 1
# d.get(0)  # returns 1

# Constraints:

# - If you are coding in a strongly typed language, you can either assume all elements are integers, or define a generic dynamic array type.
# - All operations should work with arrays of up to `10^6` elements