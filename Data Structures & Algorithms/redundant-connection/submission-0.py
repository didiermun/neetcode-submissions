class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]

        def union(node1: int, node2: int) -> bool:
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return False

            if rank[root1] < rank[root2]:
                root1, root2 = root2, root1

            parent[root2] = root1
            rank[root1] += rank[root2]

            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]

        return []