"""
381. Insert Delete GetRandom O(1) - Duplicates allowed

Solution 1
Runtime: 128 ms, faster than 13.46% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
Memory Usage: 18.1 MB, less than 100.00% of Python3 online submissions for Insert Delete GetRandom O(1)

Solution 2
Runtime: 168 ms, faster than 10.00% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
Memory Usage: 17.8 MB, less than 100.00% of Python3 online submissions for Insert Delete GetRandom O(1)

Frugal Python code - https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/85556/Frugal-Python-code

"""

import random
import collections
class RandomizedCollection1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = collections.defaultdict(set)
        self.data = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.cache[val].add(len(self.data))
        self.data.append(val)
        return len(self.cache[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.cache[val]:
            return False
        remove_idx, last = self.cache[val].pop(), self.data[-1]
        self.data[remove_idx] = last
        self.cache[last].add(remove_idx)
        self.cache[last].discard(len(self.data) - 1)
        self.data.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if self.data:
            return random.choice(self.data)
        return False

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = dict()
        self.data = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.cache[val] = self.cache.get(val, set()) | {len(self.data)}
        self.data.append(val)
        return len(self.cache[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.cache:
            return False

        idx_to_remove = self.cache[val].pop()
        val_to_update = self.data[-1]
        self.data[idx_to_remove] = val_to_update
        self.cache[val_to_update].add(idx_to_remove)
        self.cache[val_to_update].remove(len(self.data) - 1)

        if not len(self.cache[val]):
            del self.cache[val]

        self.data.pop()

        return True

    def remove__(self, val: int) -> bool:
        if val not in self.cache or not self.data:
            return False

        remove_idx, last = self.cache[val].pop(), self.data[-1]

        self.data[remove_idx] = last
        self.cache[last].add(remove_idx)
        self.cache[last].discard(len(self.data) - 1)

        if not len(self.cache[val]):
            del self.cache[val]

        self.data.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if self.data:
            return random.choice(self.data)
        return False

#########

##########
import unittest
#
#
# class TestCase(unittest.TestCase):
#     RandomizedCollection = RandomizedCollection()
#
#     def __init__(self, *args, **kwargs):
#         super(TestCase, self).__init__(*args, **kwargs)
#
#     def test1(self):
#         res = self.RandomizedCollection.insert(1)
#         out = True
#         self.assertEqual(res, out)
#
#     def test2(self):
#         res = self.RandomizedCollection.remove(2)
#         out = False
#         self.assertEqual(res, out)
#
#     def test3(self):
#         res = self.RandomizedCollection.insert(2)
#         out = True
#         self.assertEqual(res, out)
#
#     def test4(self):
#         res = self.RandomizedCollection.getRandom()
#         out = (1, 2)
#         self.assertIn(res, out)
#
#     def test5(self):
#         res = self.RandomizedCollection.remove(1)
#         out = True
#         self.assertEqual(res, out)
#
#     def test6(self):
#         res = self.RandomizedCollection.insert(2)
#         out = True
#         self.assertEqual(res, out)
#
#     def test7(self):
#         res = self.RandomizedCollection.getRandom()
#         out = 2
#         self.assertEqual(res, out)
#
#     def test8(self):
#         res = self.RandomizedCollection.getRandom()
#         out = 2
#         self.assertEqual(res, out)
#
# class TestCase2(unittest.TestCase):
#     RandomizedCollection = RandomizedCollection()
#
#     def __init__(self, *args, **kwargs):
#         super(TestCase2, self).__init__(*args, **kwargs)
#
#     def test1(self):
#         res = self.RandomizedCollection.insert(1)
#         out = True
#         self.assertEqual(res, out)
#
#     def test2(self):
#         res = self.RandomizedCollection.insert(1)
#         out = True
#         self.assertEqual(res, out)
#
#     def test3(self):
#         res = self.RandomizedCollection.remove(1)
#         out = True
#         self.assertEqual(res, out)
#
#
#     def test4(self):
#         res = self.RandomizedCollection.getRandom()
#         out = 1
#         self.assertEqual(res, out)
#

class TestCase3(unittest.TestCase):
    RandomizedCollection = RandomizedCollection()

    def __init__(self, *args, **kwargs):
        super(TestCase3, self).__init__(*args, **kwargs)

    def test1(self):
        res = self.RandomizedCollection.insert(0)
        out = True
        self.assertEqual(res, out)

    def test2(self):
        res = self.RandomizedCollection.insert(1)
        out = True
        self.assertEqual(res, out)

    def test3(self):
        res = self.RandomizedCollection.remove(0)
        out = True
        self.assertEqual(res, out)

    def test4(self):
        res = self.RandomizedCollection.insert(2)
        out = True
        self.assertEqual(res, out)

    def test5(self):
        res = self.RandomizedCollection.remove(1)
        out = True
        self.assertEqual(res, out)

    def test6(self):
        res = self.RandomizedCollection.getRandom()
        out = 2
        self.assertEqual(res, out)

class TestCase4(unittest.TestCase):
    RandomizedCollection = RandomizedCollection()

    def __init__(self, *args, **kwargs):
        super(TestCase4, self).__init__(*args, **kwargs)

    def test1(self):
        res = self.RandomizedCollection.insert(1)
        out = True
        self.assertEqual(res, out)

    def test2(self):
        res = self.RandomizedCollection.remove(1)
        out = True
        self.assertEqual(res, out)

    def test3(self):
        res = self.RandomizedCollection.insert(1)
        out = True
        self.assertEqual(res, out)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
