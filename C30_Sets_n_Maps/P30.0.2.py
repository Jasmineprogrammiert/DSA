# n: the number of elements in the set
# m: the number of elements in the other set
# T: 
#   O(1) - add, remove, contains and size: each bucket contains a constant number of elements on average
#   O(n) - resize, elements, intersections: iteration
#   O(n + m) - iteration through both sets to create a new set
#   O(min(n, m)) - optimization for intersection(): iterate the smaller set first

# S: O(n) - the hash table is designed to maintain n buckets with n elements
class HashSet:
    def __init__(self, h):
        self.h = h
        self.capacity = 10
        self._size = 0
        self.buckets = [[] for _ in range(self.capacity)]
    
    def size(self):
        return self._size
    
    def contains(self, x):
        hash = self.h(x, self.capacity)
        for ele in self.buckets[hash]:
            if ele == x:
                return True
        return False
    
    def add(self, x):
        hash = self.h(x, self.capacity)
        for ele in self.buckets[hash]:
            if ele == x: 
                return
        self.buckets[hash].append(x)
        self._size += 1
        load_factor = self._size / self.capacity
        if load_factor > 1:
            self.resize(self.capacity * 2)

    def resize(self, new_capacity):
        new_buckets = [[] for _ in range(new_capacity)]
        for bucket in self.buckets:
            for ele in bucket:
                hash = self.h(ele, new_capacity)
                new_buckets[hash].append(ele)
        self.buckets = new_buckets
        self.capacity = new_capacity
    
    def remove(self, x):
        hash = self.h(x, self.capacity)
        for i, ele in enumerate(self.buckets[hash]):
            if ele == x:
                self.buckets[hash].pop(i)
                self._size -= 1
                load_factor = self._size / self.capacity
                if load_factor < 0.25 and self.capacity > 10:
                    self.resize(self.capacity // 2)
                return 
            
    def elements(self):
        res = []
        for bucket in self.buckets:
            for ele in bucket:
                res.append(ele)
        return res
    
    def unions(self, s):
        res = HashSet(self.h)
        
        for ele in self.elements():
            res.add(ele)
        for ele in s.elements():
            res.add(ele)
        return res
    
    def intersections(self, s):
        res = HashSet(self.h)
        
        for ele in self.elements():
            if s.contains(ele):
                res.add(ele)
        return res


# # Problem 2 - Hash Set Class Extensions

# Implement a hash set data structure with the following API:
    # add(x): if x is not in the set, add x to the set
    # remove(x): if x is in the set, remove it from the set
    # contains(x): return whether element x is in the set
    # size(): return the number of elements in the set
    
# Then extend it with these additional methods:
    # elements(): return all elements in the set in a dynamic array
    # union(s): return a new set containing all elements in either this set or set s
    # intersection(s): return a new set containing only elements present in this set and set s
    
# For each method, provide time and space complexity analysis.

# Constraints:
    # If your language is typed, you can either implement a hash set for integers, or make it generic.
    # The set will contain at most 10^6 elements.