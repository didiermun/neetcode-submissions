class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dirs = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        memo = {}

        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            longest = 1

            for dr, dc in dirs:
                new_row = row + dr
                new_col = col + dc

                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue

                if matrix[row][col] >= matrix[new_row][new_col]:
                    continue

                longest = max(longest, 1 + dfs(new_row, new_col))
            memo[(row, col)] = longest
            return longest


        answer = 0

        for i in range(rows):
            for j in range(cols):
                answer = max(answer, dfs(i, j))

        
        return answer