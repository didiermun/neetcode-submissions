class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for current in range(1, n + 1):
            square = 1

            while square * square <= current:
                dp[current] = min(
                    dp[current],
                    1 + dp[current - square * square]
                )
                square += 1

        return dp[n]