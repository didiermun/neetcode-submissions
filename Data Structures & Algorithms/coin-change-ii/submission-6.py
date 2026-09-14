from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # @lru_cache
        # def dfs(remaining, index):
        #     if remaining == 0:
        #         return 1
            
        #     if remaining < 0 and index == len(coins):
        #         return 0

        #     take = dfs(remaining - coins[index], index)
            
        #     skip = dfs(remaining, index + 1)

        #     return take + skip

        # return dfs(amount, 0)

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for current_amount in range(coin, amount + 1):
                dp[current_amount] += dp[current_amount - coin]

        return dp[amount]
        