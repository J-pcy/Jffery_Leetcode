"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

"""
#Time Limit Exceeded
class LRUCache:
    def __init__(self, capacity):
        self.myList = [0] * capacity
        self.myDict = {}
        self.cap = capacity

    def get(self, key):
        if key in self.myDict:
            tmp = self.myDict[key][1]
            for i in range(self.myDict[key][0] + 1, self.cap):
                self.myList[i - 1] = self.myList[i]
                if self.myList[i - 1] in self.myDict:
                    self.myDict[self.myList[i - 1]] = (i - 1, self.myDict[self.myList[i - 1]][1])
            self.myList[self.cap - 1] = key
            self.myDict[key] = (self.cap - 1, tmp)
            return self.myDict[key][1]
        return -1

    def put(self, key, value):
        if key not in self.myDict:
            if self.myList[0] in self.myDict:
                self.myDict.pop(self.myList[0])
            for i in range(1, self.cap):
                self.myList[i - 1] = self.myList[i]
                if self.myList[i - 1] in self.myDict:
                    self.myDict[self.myList[i - 1]] = (i - 1, self.myDict[self.myList[i - 1]][1])
            self.myList[self.cap - 1] = key
            self.myDict[key] = (self.cap - 1, value)
        else:
            for i in range(self.myDict[key][0] + 1, self.cap):
                self.myList[i - 1] = self.myList[i]
                if self.myList[i - 1] in self.myDict:
                    self.myDict[self.myList[i - 1]] = (i - 1, self.myDict[self.myList[i - 1]][1])
            self.myList[self.cap - 1] = key
            self.myDict[key] = (self.cap - 1, value)
"""
"""
class LRUCache:
    def __init__(self, capacity):
        self.deque = collections.deque()
        self.myDict = {}
        self.cap = capacity

    def get(self, key):
        if key not in self.myDict:
            return -1
        self.deque.remove(key)
        self.deque.append(key)
        return self.myDict[key]

    def put(self, key, value):
        if key not in self.myDict:
            self.deque.append(key)
            if len(self.deque) > self.cap:
                self.myDict.pop(self.deque.popleft())
        else:
            self.deque.remove(key)
            self.deque.append(key)
        self.myDict[key] = value
"""
class LRUCache(object):

    def __init__(self, capacity):
        self.od = collections.OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in self.od: 
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
        else:
            if len(self.od) == self.cap:
                self.od.popitem(False)
        self.od[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)