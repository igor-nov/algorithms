"""
133. Clone Graph

Solution
run 1 - Runtime: 40 ms, faster than 38.72% of Python3 online submissions for Clone Graph.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Clone Graph
run 2 - Runtime: 36 ms, faster than 72.60% of Python3 online submissions for Clone Graph.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Clone Graph.

Solution 2 - DFS
Runtime: 60 ms, faster than 7.38% of Python3 online submissions for Clone Graph.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Clone Graph.

Solution 3- BFS
Runtime: 68 ms, faster than 7.38% of Python3 online submissions for Clone Graph.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Clone Graph.

@todo - add unit tests

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution1:
    def cloneGraph(self, node: 'Node') -> 'Node':

        # create adjacency list
        adj = {}
        cache = {}
        visited = set()
        stack = [node]
        start_pointer = node.val
        while stack:
            from_node = stack.pop(0)
            cache[from_node.val] = from_node
            if from_node.val not in visited:
                visited.add(from_node.val)
                adj[from_node.val] = []
                for to_node in from_node.neighbors:
                    stack += to_node,
                    adj[from_node.val] += to_node.val,

        # print(adj)

        # using adjacency list clone graph
        # create nodes without neighbors
        created = {}
        for node_val in adj:
            created[node_val] = Node(node_val, [])

        # fill in neighbors
        for node_val in adj:
            self.fill_in_neighbors(node_val, adj, created)

        return created[start_pointer]

    def fill_in_neighbors(self, node_val, adj, created):
        curr_node = created[node_val]
        neighbors = []
        for to_node in adj[node_val]:
            neighbors.append(created[to_node])
        curr_node.neighbors = neighbors


class Solution2:

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return

        if node.val not in self.visited:
            cloned_node = Node(node.val, [])
            self.visited[node.val] = cloned_node
            neighbors = []
            for child in node.neighbors:
                neighbors.append(self.cloneGraph(child))
            cloned_node.neighbors = neighbors
        else:
            return self.visited[node.val]


from collections import deque


class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':

        queue = deque([node])
        visited = []
        start_pointer = node.val

        while queue:
            current_node = queue.popleft()

            if not current_node:
                continue

            if current_node.val not in self.visited:
                copied_node = Node(current_node, [])
                self.visited[copied_node.val] = copied_node

                for child in current_node.neighbors:
                    if child.val not in visited:
                        child_copied = Node(child.val, [])
                    copied_node.neighbors.append(child_copied)

                    queue.append(child)

            # else:
            #     return self.visited[copied_node]

        return visited[start_pointer]


from collections import deque


class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return

        queue = deque([node])
        visited = {node: Node(node.val, [])}

        while queue:
            current_node = queue.popleft()

            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)

                visited[current_node].neighbors.append(visited[neighbor])

        return visited[node]
