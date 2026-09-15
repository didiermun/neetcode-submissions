class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        minute = 0

        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                directions = [(0,1), (0, -1), (-1, 0), (1, 0)]

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if new_col < 0 or new_col >= cols or new_row < 0 or new_row >= rows or grid[new_row][new_col] != 1:
                        continue

                    fresh -= 1
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col))

            minute += 1

        return minute if fresh == 0 else -1

        