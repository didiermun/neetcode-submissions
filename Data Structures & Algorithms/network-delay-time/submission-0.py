class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for source, destination, time in times:
            graph[source].append((destination, time))

        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            max_time = current_time

            for neighbor, travel_time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        min_heap,
                        (current_time + travel_time, neighbor)
                    )

        if len(visited) != n:
            return -1

        return max_time
        