# n: the number of elements in the set
# T: O(1) - each bucket is designed to contain a constant number of elements
# S: O(n) - the hash table is designed to maintain n buckets with n elements
class HashSet:
    def __init__(self, h):
        self.h = h # hash function (decides index)
        self.capacity = 10
        self._size = 0
        # nested list handles collision: list[index] = [val, val2]
        self.buckets = [[] for _ in range(self.capacity)]
    
    def size(self):
        return self._size
    
    def contains(self, x):
        # map input x its designated bucket index
        hash = self.h(x, self.capacity)
    
        # only search the specific bucket where x would live
        for ele in self.buckets[hash]:
            if ele == x:
                return True
        return False
    
    def add(self, x):
        # get the bucket index for x
        hash = self.h(x, self.capacity)
        
        # check the specific bucket to prevent duplicate values
        for ele in self.buckets[hash]:
            if ele == x: 
                return # if x already exists, do nothing and exit
        
        # add x to the bucket and update the total count
        self.buckets[hash].append(x)
        self._size += 1
        
        # calculate if the table is getting too crowded  (ele > buckets)
        load_factor = self._size / self.capacity
        if load_factor > 1:
            # double the capacity to keep operation fast(O(1))
            self.resize(self.capacity * 2)

    def resize(self, new_capacity):
        new_buckets = [[] for _ in range(new_capacity)]
        for bucket in self.buckets:
            for ele in bucket:
                # Re-calculate the hash index for each element, 
                # then append the element to the new position
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



# Problem 1 - Hash Set Class

# Implement a hash set data structure with the following API:
    # add(x): if x is not in the set, add x to the set. If x is already in the set, do nothing.
    # remove(x): if x is in the set, remove it from the set.
    # contains(x): return whether the element x is in the set.
    # size(): return the number of elements in the set.
# Constraints:
    # If your language is typed, you can either implement a hash set for integers, or make it generic.
    # The set will contain at most 10^6 elements.