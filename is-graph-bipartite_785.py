"""
785. Is Graph Bipartite?

Solution 1 - DFS
Runtime: 184 ms, faster than 74.44% of Python3 online submissions for Is Graph Bipartite?.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Is Graph Bipartite?.

Solution2 - explicit DFS
Runtime: 168 ms, faster than 99.88% of Python3 online submissions for Is Graph Bipartite?.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Is Graph Bipartite?.

Solution 3 - BFS
Runtime: 176 ms, faster than 97.02% of Python3 online submissions for Is Graph Bipartite?.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Is Graph Bipartite?.

Solution 4 - explicit BFS
Runtime: 176 ms, faster than 97.02% of Python3 online submissions for Is Graph Bipartite?.
Memory Usage: 13 MB, less than 90.91% of Python3 online submissions for Is Graph Bipartite?.

Solutions
+ - (so so)  Bipartite Graph | Leetcode 785 | Graph | Breadth First Search - https://www.youtube.com/watch?v=FofydiwP5YQ
"""

from typing import List


class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colors = {}

        for from_node in range(len(graph)):
            if from_node in colors:
                continue

            stack = [from_node]
            colors[from_node] = 1  # 1 is just starting color, could be -1 also

            while stack:
                from_node = stack.pop()

                for to_node in graph[from_node]:
                    if to_node in colors:
                        if colors[to_node] == colors[from_node]:
                            return False
                    else:
                        stack.append(to_node)
                        colors[to_node] = colors[from_node] * -1
        return True


class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for node_from in range(len(graph)):
            if node_from not in colors and not self.dfs(graph, node_from, colors, 1):
                return False

        return True

    def dfs(self, graph, node, colors, color):

        colors[node] = color

        for node_to in graph[node]:
            if node_to in colors:
                if colors[node_to] == colors[node]:
                    return False
            else:
                if not self.dfs(graph, node_to, colors, color * -1):
                    return False

        return True



from collections import deque
class Solution3:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colors = {}

        for from_node in range(len(graph)):
            if from_node in colors:
                continue
            queue = deque([from_node])
            colors[from_node] = 1 # 1 is just starting color, could be -1 also

            while queue:
                from_node = queue.popleft()
                for to_node in graph[from_node]:
                    if to_node in colors:
                        if colors[to_node] == colors[from_node]:
                            return False
                    else:
                        queue.append(to_node)
                        colors[to_node] = colors[from_node] * -1

        return True

from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for node_from in range(len(graph)):
            if node_from not in colors and not self.bfs(graph, node_from, colors):
                return False
        return True

    def bfs(self, graph, node, colors):
        color = 1
        queue = deque([node])
        colors[node] = color
        while queue:
            node_from = queue.popleft()
            for node_to in graph[node_from]:
                if node_to in colors:
                    if colors[node_to] == colors[node_from]:
                        return False
                else:
                    colors[node_to] = colors[node_from] * -1
                    queue.append(node_to)
        return True


from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for node_from in range(len(graph)):
            if node_from not in colors and not self.bfs(graph, node_from, colors, 1):
                return False
        return True

    def bfs(self, graph, node, colors, color):
        queue = deque([node])
        colors[node] = color
        while queue:
            node_from = queue.popleft()
            for node_to in graph[node_from]:
                if node_to in colors:
                    if colors[node_to] == colors[node_from]:
                        return False
                else:
                    colors[node_to] = colors[node_from] * -1
                    queue.append(node_to)
        return True


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [[1, 3], [0, 2], [1, 3], [0, 2]]
        out = True
        res = Solution().isBipartite(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        out = False
        res = Solution().isBipartite(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [[], [2], [1], [], [], [7, 8], [7, 8, 9], [5, 6], [5, 6], [6], [12, 13, 14], [12], [10, 11], [10], [10],
               [18], [17, 18], [16], [15, 16], [], [22, 23, 24], [22, 23, 24], [20, 21], [20, 21], [20, 21],
               [27, 28, 29], [27, 28, 29], [25, 26], [25, 26], [25, 26], [32, 33, 34], [33], [30], [30, 31], [30],
               [37, 39], [38], [35], [36], [35], [44], [43, 44], [], [41], [40, 41], [47, 48, 49], [47, 48, 49],
               [45, 46], [45, 46], [45, 46]]
        out = True
        res = Solution().isBipartite(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
