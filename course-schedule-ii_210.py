"""
210. Course Schedule II


Solution 1 - indegree
Runtime: 96 ms, faster than 95.06% of Python3 online submissions for Course Schedule II.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Course Schedule II.

Solution 2 - dfs
Runtime: 96 ms, faster than 95.06% of Python3 online submissions for Course Schedule II.
Memory Usage: 15.6 MB, less than 60.71% of Python3 online submissions for Course Schedule II.

Solution 3 - pop 1st element from stack
Runtime: 104 ms, faster than 61.65% of Python3 online submissions for Course Schedule II.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Course Schedule II


Solution - https://leetcode.com/problems/course-schedule-ii/solution/

Python dfs, bfs solutions with comments. - https://leetcode.com/problems/course-schedule-ii/discuss/59321/Python-dfs-bfs-solutions-with-comments.
Fast python DFS solution with inline explanation - https://leetcode.com/problems/course-schedule-ii/discuss/59455/Fast-python-DFS-solution-with-inline-explanation
IN/OUT degree - AC Python topological sort 72 ms, O(V+E) time and O(V+E) space - https://leetcode.com/problems/course-schedule-ii/discuss/59486/AC-Python-topological-sort-72-ms-O(V%2BE)-time-and-O(V%2BE)-space

"""

from typing import List


class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        in_degree = [0] * numCourses

        for to_, from_ in prerequisites:
            adj[from_] = adj.get(from_, []) + [to_]
            in_degree[to_] += 1

        stack = [key for key, val in enumerate(in_degree) if val == 0]
        res = []

        while stack:
            from_ = stack.pop()
            if from_ in adj:
                for to_ in adj[from_]:
                    ##detect cycle
                    in_degree[to_] -= 1
                    if in_degree[to_] == 0:
                        stack.append(to_)

            res.append(from_)

        if numCourses != len(res):
            return []

        return res

#dfs
class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        path = []
        visited = [0] * numCourses

        for to_, from_ in prerequisites:
            adj[from_] = adj.get(from_, []) + [to_]

        def dfs(from_):
            if visited[from_] == -1:
                return False

            if visited[from_]:
                return True

            visited[from_] = -1

            if from_ in adj:
                for to_ in adj[from_]:
                    if not dfs(to_):
                        return []

            visited[from_] = 1
            path.append(from_)
            return True

        for from_ in range(numCourses):
            if not dfs(from_):
                return []

        # path.reverse()
        # return path if len(path) == numCourses else []

        return path[::-1] if len(path) == numCourses else []


from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        in_degree = [0] * numCourses

        for to_, from_ in prerequisites:
            adj[from_] = adj.get(from_, []) + [to_]
            in_degree[to_] += 1


        #stack = deque([key for key, val in enumerate(in_degree) if val == 0])
        stack = [key for key, val in enumerate(in_degree) if val == 0]
        res = []

        while stack:
            from_ = stack.pop(0)
            #from_ = stack.popleft()
            res.append(from_)
            if from_ in adj:
                for to_ in adj[from_]:
                    ##detect cycle
                    in_degree[to_] -= 1
                    if in_degree[to_] == 0:
                        stack.append(to_)

            # res.append(from_)

        if numCourses != len(res):
            return []

        return res

#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [[1, 0]]
        num = 2
        out = [0, 1]
        res = Solution().findOrder(num, inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [[1, 0], [0, 1]]
        num = 2
        out = []
        res = Solution().findOrder(num, inp)
        self.assertEqual(res, out)

    def test22(self):
        inp = [[0, 1], [1, 0]]
        num = 2
        out = []
        res = Solution().findOrder(num, inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = []
        num = 1
        out = [0]
        res = Solution().findOrder(num, inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = [[1, 0]]
        num = 3
        out = [2, 0, 1]
        out = [0, 2, 1] #indegree 2
        res = Solution().findOrder(num, inp)
        self.assertEqual(res, out)

    def test5(self):
        inp = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]
        num = 8
        out = [5, 0, 7, 1, 4, 6, 2, 3]  # indegree1
        out = [3, 4, 5, 6, 0, 2, 7, 1]  # indegree 2

        # out = [5, 4, 6, 3, 2, 0, 7, 1] #dfs
        res = Solution().findOrder(num, inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
