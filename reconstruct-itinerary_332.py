"""
332. Reconstruct Itinerary

Solution 1
Runtime: 84 ms, faster than 52.75% of Python3 online submissions for Reconstruct Itinerary.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reconstruct Itinerary.

Solution 2
Runtime: 76 ms|88|100, faster than 88.78% of Python3 online submissions for Reconstruct Itinerary.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reconstruct Itinerary.

Solution 3
Runtime: 84 ms, faster than 52.75% of Python3 online submissions for Reconstruct Itinerary.
Memory Usage: 13 MB, less than 92.31% of Python3 online submissions for Reconstruct Itinerary.


--------------------------------
https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
After reading leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C++/83576 comments, i finally understand this algs.
Here is some points to understand this algs and hope it helps.

In Eulerian paths, there must exist a start node(which is JFK in this problem) and a end node.
End node can be start node or another node.
end node is start node iff all nodes has even degree.
end node is another node iff there is another odd degree node and start node has an odd degree.
So, the algorithm is to find the end node first and delete the path to this node(backtrack), meanwhile using PriorityQueue to guarantee lexical order.
Really amazing solution, I always don't know how to deal with Euler Path and know I begin to be some less confused.
-----

some observations:
The nodes which have odd degrees (int and out) are the entrance or exit. In your example it's JFK and A.
If there are no nodes have odd degrees, we could follow any path without stuck until hit the last exit node
The reason we got stuck is because that we hit the exit
In your given example, nodes A is the exit node, we hit it and it's the exit. So we put it to the result as the last node.
-----------


Awesome question | new algo to learn |  Eulerian Path | Full explanation |  Code - https://leetcode.com/problems/reconstruct-itinerary/discuss/359942/Awesome-question-or-new-algo-to-learn-or-Eulerian-Path-or-Full-explanation-or-Code

I think this algorithm is often called Fleury's algorithm. But actually it is Hierholzer's algorithm according to the wiki. Anyway, it works like this: - https://leetcode.com/problems/reconstruct-itinerary/discuss/78835/28ms-C%2B%2B-beats-100-Short-and-Elegant.

"""
from typing import List


class Solution1:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routes = {}
        for from_, to_ in sorted(tickets):
            routes[from_] = routes.get(from_, []) + [to_]

        path = []
        stack = ['JFK']

        i = 0
        while stack:
            if stack[-1] in routes and routes[stack[-1]]:
                stack.append(routes[stack[-1]].pop(0))
            else:
                path.append(stack.pop())
        return path[::-1]


import heapq


class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routes = {}
        # for from_, to_ in sorted(tickets):
        for from_, to_ in tickets:
            routes[from_] = routes.get(from_, []) + [to_]

        for p in routes.values():
            heapq.heapify(p)

        path = []
        stack = ['JFK']

        i = 0
        while stack:
            if stack[-1] in routes and routes[stack[-1]]:
                # stack.append(routes[stack[-1]].pop(0))
                stack.append(heapq.heappop(routes[stack[-1]]))
            else:
                path.append(stack.pop())
        return path[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routes = {}
        for from_, to_ in sorted(tickets):
            routes[from_] = routes.get(from_, []) + [to_]

        path = []
        def dfs(to_):
            while to_ in routes and routes[to_]:
                dfs(routes[to_].pop(0))
            path.append(to_)

        dfs('JFK')
        return path[::-1]


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        out = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        res = Solution().findItinerary(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        out = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        res = Solution().findItinerary(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        out = ["JFK", "NRT", "JFK", "KUL"]
        res = Solution().findItinerary(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
