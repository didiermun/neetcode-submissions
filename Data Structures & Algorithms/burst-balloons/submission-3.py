from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # nums = [1] + nums + [1]

        # @lru_cache
        # def dfs(left, right):
        #     if left + 1 == right:
        #         return 0

        #     max_coins = 0

        #     for i in range(left + 1, right):
        #         coins = nums[i] * nums[left] * nums[right] + dfs(left, i) + dfs(i, right)

        #         max_coins = max(max_coins, coins)

        #     return max_coins

        # return dfs(0, len(nums) - 1)


        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # length is the distance between boundaries
        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[k] * nums[right]
                        + dp[left][k]
                        + dp[k][right]
                    )

        return dp[0][n - 1]


        