# Multimap: a collection of key-value pairs where one key can have many values. Associated multiple pieces of data with one identifier
# Map<Key, List<Value>>

# Implement a multimap on top of a standard HashMap

# n: the total number of key-value pairs in the multimap
# T: 
#       O(1) on average. With a load factor around 1, bucket depth ia constant
#       Resize takes O(n), but happens infrequently enough to maintain amortized constant time. This assumes that hashing takes contatn time, which is not true for key types like strings
#       It also assumed that get() returns a reference (instead of copying), and the garbage collection handles the deleted list efficiently
# S: O(n) - the hash table maintains approximately n buckets with a total of n key-value pairs, plus some overhead for dynamic resizing
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
class MultiMap:
    def __init__(self, h):
        self.map = HashMap(h)
        self._size = 0
    
    def size(self):
        return self._size
    
    def contains(self, k):
        return self.map.contains(k)
    
    def get(self, k):
        values = self.map.get(k)
        if values is None:
            return []
        return values
    
    def add(self, k, v):
        values = self.get(k)
        values.append(v)
        self.map.add(k, values)
        self._size += 1
    
    def remove(self, k):
        if self.contains(k):
            self._size -= len(self.get(k))
            self.map.remove(k)


# Problem 6 - Multimap

# A multimap is a map that allows multiple key-value pairs with the same key. Implement a multimap data structure with the following API:
    # add(k, v): adds key k with value v to the multimap, even if key k is already found
    # remove(k): removes all key-value pairs with k as the key
    # contains(k): returns whether the multimap contains any key-value pair with k as the key
    # get(k): returns all values associated to key k in a list. If there is none, returns an empty list
    # size(): returns the number of key-value pairs in the multimap
    
# Constraints:
    # If your language is typed, you can either implement a multimap for integers, or make it generic.
    # The multimap will contain at most 10^6 key-value pairs.