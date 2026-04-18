# Initialize an empty array, then iterate each bucket and apppend either key or value to the empty array

# n: the number of key-value pairs in the map
# Basic operations (add, remove, get, contains)
#       T: O(1) amortized. With a load factor around 1, bucket depth ia constant
#       Resize takes O(n), but happens infrequently enough to maintain amortized constant time. This assumes that hashing takes contatn time, which is not true for key types like strings
#       S: O(n) - all bucket must be iterated one by one to collect the key/value into a new array

# Collections (keys, values)
#       T: O(n) - O(size + capacity)  = O(size) because all buckets are iterated to collect the key/value into a new array. Since the load factor is at least 25%, the capacity is at most four times the size, it's simplified to O(n)
#       S: O(n) - the hash table maintains approximately n buckets with a total of n key-value pairs, plus some overhead for dynamic resizing
class HashMap:
    def __init__(self, h):
        self.h = h
        self.capacity = 10
        self._size = 0
        self.buckets = [[] for _ in range(self.capacity)]
    
    def size(self):
        return self._size
    
    def contains(self, k):
        hash = self.h(k, self.capacity)
        for key, _ in self.buckets[hash]:
            if key == k:
                return True
        return False
    
    def get(self, k):
        hash = self.h(k, self.capacity)
        for key, val in self.buckets[hash]:
            if key == k:
                return val
        return None

    def add(self, k, v):
        hash = self.h(k, self.capacity)
        for i, (key, _) in enumerate(self.buckets[hash]):
            if key == k: 
                self.buckets[hash][i] = (k, v)
                return
        self.buckets[hash].append((k, v))
        self._size += 1
        load_factor = self._size / self.capacity
        if load_factor > 1:
            self.resize(self.capacity * 2)

    def resize(self, new_capacity):
        new_buckets = [[] for _ in range(new_capacity)]
        for bucket in self.buckets:
            for k, v in bucket:
                hash = self.h(k, new_capacity)
                new_buckets[hash].append((k, v))
        self.buckets = new_buckets
        self.capacity = new_capacity
    
    def remove(self, k):
        hash = self.h(k, self.capacity)
        for i, (key, _) in enumerate(self.buckets[hash]):
            if key == k:
                self.buckets[hash].pop(i)
                self._size -= 1
                load_factor = self._size / self.capacity
                if load_factor < 0.25 and self.capacity > 10:
                    self.resize(self.capacity // 2)
                return 
    
    def keys(self):
        res = []
        for bucket in self.buckets:
            for k, _ in bucket:
                res.append(k)
        return res
    
    def values(self):
        res = []
        for bucket in self.buckets:
            for _, v in bucket:
                res.append(v)
        return res



# # Problem 5 - Hash Map Class Extensions

# Implement a hash map data structure with the following API:
    # add(k, v): if k is not in the map, add key k to the map with value v. If k is already in the map, update its value to v.
    # remove(k): if k is in the map, remove it from the map
    # contains(k): return whether the key k is in the map
    # get(k): return the value for key k. If k is not in the map, return a null value
    # size(): return the number of keys in the map
    
# Then extend it with these additional methods:
    # keys(): return all keys in the map in a dynamic array. The output order doesn't matter.
    # values(): return all values in the map in a dynamic array. The output order doesn't matter. If a value appears more than once, return it as many times as it occurs.
    
# For each method, provide time and space complexity analysis.

# Constraints:
    # If your language is typed, you can either implement a hash map for integers, or make it generic.
    # The map will contain at most 10^6 key-value pairs.