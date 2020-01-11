"""
1315. Sum of Nodes with Even-Valued Grandparent

Solution 1
Runtime: 140 ms, faster than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.

Solution 2 - optimized 1
Runtime: 136 ms, faster than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 16.4 MB, less than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.

Solution 3
Runtime: 116 ms, faster than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.

Solutions
[Java/C++/Python] 1-Line Recursive Solution - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/discuss/477048/JavaC%2B%2BPython-1-Line-Recursive-Solution
[Java/Python 3] BFS succinct codes. - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/discuss/477232/JavaPython-3-BFS-succinct-codes.
"""

from tree_hepler import TreeNode

class Solution1:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0

        even_value_nodes = {}
        stack = [(root, 0)]

        while stack:
            root, level = stack.pop()
            if root:
                if root.val % 2 == 0:
                    even_value_nodes[root] = level
                stack.append((root.left, level + 1))
                stack.append((root.right, level + 1))

        res = 0
        for node in even_value_nodes:
            res += self.sumHelper(node, 0, 0)
        return res

    def sumHelper(self, root, sub_level, sum_res):
        if not root:
            return 0
        if sub_level == 2:
            return root.val
        if sub_level > 2:
            return 0
        return self.sumHelper(root.left, sub_level+1, sum_res) + self.sumHelper(root.right, sub_level+1, sum_res)


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.sumHelper(root, 1, 1)

    def sumHelper(self, node, parent, gr_parent):
        if not node:
            return 0
        if  gr_parent % 2 == 0:
            val = node.val
        else:
            val = 0
        return val + self.sumHelper(node.left, node.val, parent) + self.sumHelper(node.right, node.val, parent)

#####################################################
import unittest
import tree_hepler


class TestSolution(unittest.TestCase):

    def test1(self):
        inp = "[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]"
        root = tree_hepler.stringToTreeNode(inp)
        out = 18
        res = Solution().sumEvenGrandparent(root)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
