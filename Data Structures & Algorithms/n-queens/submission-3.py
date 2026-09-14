class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        used_col = set()
        used_positive_diag = set()
        used_negative_diag = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(board_row) for board_row in board])
            for col in range(n):
                positive_diag = row + col
                negative_diag = row - col
                if col in used_col or positive_diag in used_positive_diag or negative_diag in used_negative_diag:
                    continue

                board[row][col] = "Q"
                used_col.add(col)
                used_positive_diag.add(positive_diag)
                used_negative_diag.add(negative_diag)

                backtrack(row + 1)


                board[row][col] = "."
                used_col.remove(col)
                used_positive_diag.remove(positive_diag)
                used_negative_diag.remove(negative_diag)

        backtrack(0)

        return result

        