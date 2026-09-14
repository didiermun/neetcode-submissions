class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()

        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        return len(visited) == n
        