class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)

        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)


        visited = set()
        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)


        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        

        return components