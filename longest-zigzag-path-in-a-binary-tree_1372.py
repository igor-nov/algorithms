"""
1372. Longest ZigZag Path in a Binary Tree

Solution 1
Runtime: 432 ms, faster than 75.99% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
Memory Usage: 52.8 MB, less than 100.00% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.

Solution 2
Runtime: 420 ms, faster than 83.72% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
Memory Usage: 51.9 MB, less than 100.00% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
Runtime: 416 ms, faster than 86.22% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
Memory Usage: 52 MB, less than 100.00% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.

Solution 3 - same as above but without global variable for res
Runtime: 412 ms, faster than 89.14% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
Memory Usage: 51.6 MB, less than 100.00% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.

Solution 4 !!!
Runtime: 400 ms, faster than 93.95% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
Memory Usage: 52.9 MB, less than 100.00% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
Runtime: 368 ms, faster than 99.58% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
Memory Usage: 52.9 MB, less than 100.00% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.

Solution 5 !!!!!!!!!! - same as above but more concise
Runtime: 368 ms, faster than 99.58% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
Memory Usage: 52.9 MB, less than 100.00% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.


Solutions
[Python] Intuitive Top Down Solution - https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/discuss/533335/Python-Intuitive-Top-Down-Solution
Python - DFS with Direction of Parent - https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/discuss/531859/Python-DFS-with-Direction-of-Parent
Python small and simple solution - https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/discuss/532836/Python-small-and-simple-solution

Java beats 100 percent with explanation - https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/discuss/532399/Java-beats-100-percent-with-explanation
[Java/Python] DFS Solution - https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/discuss/531867/JavaPython-DFS-Solution

@todo - solve using BFS
[Python] BFS Solution - https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/discuss/531990/Python-BFS-Solution

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# solution 1
class Solution:

    def __init__(self):
        self.final_max = 0

    def longestZigZag(self, root: TreeNode) -> int:
        self.final_max = 0
        self.helper(root.left, False, 0)
        self.helper(root.right, True, 0)
        return self.final_max

    def helper(self, root: TreeNode, is_next_left_move: bool, current_max: int):
        if not root:
            self.final_max = max(current_max, self.final_max)
            return
        if is_next_left_move:
            self.helper(root.left, False, current_max + 1)
            self.helper(root.right, True, 0)
        else:
            self.helper(root.left, False, 0)
            self.helper(root.right, True, current_max + 1)


# solution 2
class Solution:
    def __init__(self):
        self.res = 0

    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.helper(root.left, False)
        self.helper(root.right, True)
        return self.res

    def helper(self, node: TreeNode, is_next_left_move: bool):
        if not node:
            return 0
        left_path = self.helper(node.left, False)
        right_path = self.helper(node.right, True)
        next_result = left_path + 1 if is_next_left_move else right_path + 1
        self.res = max(self.res, next_result)
        return next_result

# same as above but without global variable for res
class Solution3:
    def longestZigZag(self, root: TreeNode) -> int:
        _, left_path = self.helper(root.left, False)
        _, right_path = self.helper(root.right, True)
        return max(left_path, right_path)

    def helper(self, root: TreeNode, is_next_left_move: bool):
        if not root:
            return 0, 0

        left_path_from_now, max_left_path = self.helper(root.left, False)
        right_path_from_now, max_right_path = self.helper(root.right, True)

        next_path = left_path_from_now + 1 if is_next_left_move else right_path_from_now + 1
        res = max(next_path, max_left_path, max_right_path)

        return next_path, res


# Solution 4 !!!
## inspired by https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/discuss/532836/Python-small-and-simple-solution
class Solution4:

    def longestZigZag(self, root: TreeNode) -> int:
        return self.helper(root, 0, 0)

    def helper(self, root: TreeNode, left_max: int, right_max: int) -> int:
        if not root:
            return 0
        left_max_next = self.helper(root.left, right_max + 1, 0) if root.left else right_max
        right_max_next = self.helper(root.right, 0, left_max + 1) if root.right else left_max
        return max(left_max_next, right_max_next)


class Solution5:

    def longestZigZag(self, root: TreeNode) -> int:
        return self.helper(root, 0, 0)

    def helper(self, root: TreeNode, sum_from_left_parent: int, sum_from_right_parent: int) -> int:
        if root.left:
            next_sum_in_left_direction = self.helper(root.left, sum_from_right_parent + 1, 0)
        else:
            next_sum_in_left_direction = sum_from_right_parent

        if root.right:
            next_sum_in_right_direction = self.helper(root.right, 0, sum_from_left_parent + 1)
        else:
            next_sum_in_right_direction = sum_from_left_parent

        return max(next_sum_in_right_direction, next_sum_in_left_direction)



#####################
import unittest
import tree_hepler

print('tests')


class TestSolution(unittest.TestCase):

    def test_1(self):
        inp = '[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]'
        root = tree_hepler.stringToTreeNode(inp)
        out = 3
        res = Solution().longestZigZag(root)
        self.assertEqual(res, out)

    def test_2(self):
        inp = '[1,1,1,null,1,null,null,1,1,null,1]'
        root = tree_hepler.stringToTreeNode(inp)
        out = 4
        res = Solution().longestZigZag(root)
        self.assertEqual(res, out)

    def test_3(self):
        inp = '[1]'
        root = tree_hepler.stringToTreeNode(inp)
        out = 0
        res = Solution().longestZigZag(root)
        self.assertEqual(res, out)

    def test_4(self):
        inp = '[6,9,7,3,null,2,8,5,8,9,7,3,9,9,4,2,10,null,5,4,3,10,10,9,4,1,2,null,null,6,5,null,null,null,null,9,null,9,6,5,null,5,null,null,7,7,4,null,1,null,null,3,7,null,9,null,null,null,null,null,null,null,null,9,9,null,null,null,7,null,null,null,null,null,null,null,null,null,6,8,7,null,null,null,3,10,null,null,null,null,null,1,null,1,2]'
        root = tree_hepler.stringToTreeNode(inp)
        out = 5
        res = Solution().longestZigZag(root)
        self.assertEqual(res, out)

    def test_5(self):
        inp = '[1,null,1,1,1,null,null,null,1]'
        root = tree_hepler.stringToTreeNode(inp)
        out = 2
        res = Solution().longestZigZag(root)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
