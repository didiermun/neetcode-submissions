class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pc = set()
        ac = set()

        rows = len(heights)
        cols = len(heights[0])

        def dfs(row, col, visited):
            visited.add((row, col))
            ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in ds:
                new_row = dr + row
                new_col = dc + col

                new_cell = (new_row, new_col)

                if new_row >= rows or new_row < 0 or new_col >= cols or new_col < 0 or new_cell in visited:
                    continue

                if heights[new_row][new_col] < heights[row][col]:
                    continue

                dfs(new_row, new_col, visited)

        for i in range(rows):
            dfs(i, 0, pc)
            dfs(i, cols-1, ac)

        for i in range(cols):
            dfs(0, i, pc)
            dfs(rows-1, i, ac)



        return list(pc & ac)
        