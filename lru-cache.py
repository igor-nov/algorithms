"""
146. LRU Cache

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

Solutions:

Implement An LRU Cache - The LRU Cache Eviction Policy ("LRU Cache" on LeetCode) - https://www.youtube.com/watch?v=S6IfqDXWa10
Python Dict + Double LinkedList (+ comments) - https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList
Clean Python solution with __unlink_node and __insert_at_head method, dictionary + doubly linked list - https://leetcode.com/problems/lru-cache/discuss/46149/Clean-Python-solution-with-__unlink_node-and-__insert_at_head-method-dictionary-%2B-doubly-linked-list
Python concise solution with comments (Using OrderedDict). - https://leetcode.com/problems/lru-cache/discuss/45952/Python-concise-solution-with-comments-(Using-OrderedDict).

"""


"""
Solution 1 - based on add/remove which is not very efficient

Runtime: 160 ms, faster than 52.40% of Python online submissions for LRU Cache.
Memory Usage: 20 MB, less than 53.81% of Python online submissions for LRU Cache.
Next challenges
"""
class Node(object):
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return 'Node {}:{}'.format(self.key, self.value)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            #pop node up
            node = self.cache[key]
            self.remove(node)
            self.add(node.key, node.value)
            return node.value
        else:
            return -1
            
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        else:
            self.manageCapacity()
            
        self.add(key, value)
            
    def manageCapacity(self):
        #print '{} capacity'.format(self.capacity)
        if self.capacity < 1:
            self.remove(self.tail.prev)
            
    def remove(self, node):
        #print '{}-{} remove'.format(node.key, node.value)
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        del self.cache[node.key]
        self.capacity += 1
        
    def add(self, key, value):
        newNode = Node(key, value)
        nextNode = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = nextNode
        nextNode.prev = newNode
        self.capacity -= 1
        self.cache[key] = newNode
        #print self.cache


"""
Solution 2 - (use swam instead of remove - add) - faster, but consumes more memory

Runtime: 128 ms, faster than 92.44% of Python online submissions for LRU Cache.
Memory Usage: 20.2 MB, less than 31.25% of Python online submissions for LRU Cache.
"""
class Node(object):
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return 'Node {}:{}'.format(self.key, self.value)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.swam(node)
#             self.remove(node)
#             self.add(node.key, node.value)
            return node.value
        else:
            return -1
            
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            #self.remove(node)
            node.value = value
            self.swam(node)
        else:
            self.manageCapacity()
            self.add(key, value)
        #self.add(key, value)
            
    def manageCapacity(self):
        #print '{} capacity'.format(self.capacity)
        if self.capacity < 1:
            self.remove(self.tail.prev)
            
    def remove(self, node):
        #print '{}-{} remove'.format(node.key, node.value)
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        del self.cache[node.key]
        self.capacity += 1
        
    def add(self, key, value):
        newNode = Node(key, value)
        nextNode = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = nextNode
        nextNode.prev = newNode
        self.capacity -= 1
        self.cache[key] = newNode
        
    def swam(self, node):
        nodePrev = node.prev
        nodeNext = node.next
        
        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev
        
        head = self.head.next
        node.next = self.head.next
        node.prev = self.head
        head.prev = node
        self.head.next = node
       
