"""
95. Unique Binary Search Trees II

Solution 1
Runtime: 64 ms, faster than 12.76% of Python3 online submissions for Unique Binary Search Trees II.
Memory Usage: 14.4 MB, less than 80.00% of Python3 online submissions for Unique Binary Search Trees II.

Solution 2 with cache
Runtime: 52 ms, faster than 57.45% of Python3 online submissions for Unique Binary Search Trees II.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Unique Binary Search Trees II.
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def __str__(self):
    #     return f'node:{self.val} | left->{self.left} | right->{self.right}'

class Solution1:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def generateTree(start, end):

            if start > end:
                return [None, ]

            trees = []
            for i in range(start, end + 1):
                left_tree = generateTree(start, i - 1)
                right_tree = generateTree(i + 1, end)

                for l in left_tree:
                    for r in right_tree:
                        tree = TreeNode(i)
                        tree.left = l
                        tree.right = r
                        trees.append(tree)

            return trees

        return [] if not n else generateTree(1, n)

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        cache = {}
        def generateTree(start, end):

            if start > end:
                return [None, ]

            if (start, end) in cache: return cache[start, end]
            trees = []
            for i in range(start, end + 1):
                left_tree = generateTree(start, i - 1)
                right_tree = generateTree(i + 1, end)

                for l in left_tree:
                    for r in right_tree:
                        tree = TreeNode(i)
                        tree.left = l
                        tree.right = r
                        trees.append(tree)
            cache[(start, end)] = trees
            return trees

        return [] if not n else generateTree(1, n)


#############
#@todo - fix
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = 3
        out = [
            [1, None, 3, 2],
            [3, 2, None, 1],
            [3, 1, None, None, 2],
            [2, 1, 3],
            [1, None, 2, None, 3]
        ]
        res = Solution().generateTrees(inp)
        #print('res=', res)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
