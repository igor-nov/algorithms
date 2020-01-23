"""
380. Insert Delete GetRandom O(1)


Solution 1
Runtime: 128 ms, faster than 32.00% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 16.8 MB, less than 79.17% of Python3 online submissions for Insert Delete GetRandom O(1).


https://leetcode.com/problems/insert-delete-getrandom-o1/solution/
Java solution using a HashMap and an ArrayList along with a follow-up. (131 ms) - https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85401/Java-solution-using-a-HashMap-and-an-ArrayList-along-with-a-follow-up.-(131-ms)
Simple solution in Python - https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python
"""

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = dict()
        self.data = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.cache:
            return False
        else:
            self.data.append(val)
            self.cache[val] = len(self.data) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.cache:
            idx = self.cache[val]
            if idx != len(self.data) - 1:
                last_idx = len(self.data) - 1
                self.data[idx], self.data[last_idx] = self.data[last_idx], self.data[idx]
                self.cache[self.data[idx]] = idx
            self.data.pop()
            del self.cache[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand_pos = random.randrange(0, len(self.data)-1)
        return self.data[rand_pos]


##########
import unittest


class TestCase(unittest.TestCase):
    randomizedSet = RandomizedSet()

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    def test1(self):
        res = self.randomizedSet.insert(1)
        out = True
        self.assertEqual(res, out)

    def test2(self):
        res = self.randomizedSet.remove(2)
        out = False
        self.assertEqual(res, out)

    def test3(self):
        res = self.randomizedSet.insert(2)
        out = True
        self.assertEqual(res, out)

    def test4(self):
        res = self.randomizedSet.getRandom()
        out = (1, 2)
        self.assertIn(res, out)

    def test5(self):
        res = self.randomizedSet.remove(1)
        out = True
        self.assertEqual(res, out)

    def test6(self):
        res = self.randomizedSet.insert(2)
        out = False
        self.assertEqual(res, out)

    def test7(self):
        res = self.randomizedSet.getRandom()
        out = 2
        self.assertEqual(res, out)

    def test8(self):
        res = self.randomizedSet.getRandom()
        out = 2
        self.assertEqual(res, out)

class TestCase2(unittest.TestCase):
    randomizedSet = RandomizedSet()

    def __init__(self, *args, **kwargs):
        super(TestCase2, self).__init__(*args, **kwargs)

    def test1(self):
        res = self.randomizedSet.insert(1)
        out = True
        self.assertEqual(res, out)

    def test2(self):
        res = self.randomizedSet.insert(10)
        out = True
        self.assertEqual(res, out)

    def test3(self):
        res = self.randomizedSet.insert(20)
        out = True
        self.assertEqual(res, out)

    def test4(self):
        res = self.randomizedSet.insert(30)
        out = True
        self.assertEqual(res, out)

    def test5(self):
        res = self.randomizedSet.getRandom()
        out = (1, 10, 20, 30)
        self.assertIn(res, out)

    def test6(self):
        res = self.randomizedSet.getRandom()
        out = (1, 10, 20, 30)
        self.assertIn(res, out)

    def test7(self):
        res = self.randomizedSet.getRandom()
        out = (1, 10, 20, 30)
        self.assertIn(res, out)

    def test8(self):
        res = self.randomizedSet.getRandom()
        out = (1, 10, 20, 30)
        self.assertIn(res, out)

    def test9(self):
        res = self.randomizedSet.getRandom()
        out = (1, 10, 20, 30)
        self.assertIn(res, out)

    def test91(self):
        res = self.randomizedSet.getRandom()
        out = (1, 10, 20, 30)
        self.assertIn(res, out)

    def test92(self):
        res = self.randomizedSet.getRandom()
        out = (1, 10, 20, 30)
        self.assertIn(res, out)
        out = tuple([item for item in out if item != res])

    def test93(self):
        res = self.randomizedSet.getRandom()
        out = (1, 10, 20, 30)
        self.assertIn(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
