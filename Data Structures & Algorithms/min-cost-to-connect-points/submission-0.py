class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_heap = [(0, 0)]
        visited = set()

        total_cost = 0

        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)

            if point in visited:
                continue

            visited.add(point)
            total_cost += cost

            x1, y1 = points[point]

            for neighbor in range(n):
                if neighbor in visited:
                    continue

                x2, y2 = points[neighbor]

                distance = abs(x1 - x2) + abs(y1 - y2)

                heapq.heappush(
                    min_heap,
                    (distance, neighbor)
                )

        return total_cost
        