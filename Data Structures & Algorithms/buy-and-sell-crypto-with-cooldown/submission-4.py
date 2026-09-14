from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache
        def dfs(index, buying):
            if index >= len(prices):
                return 0

            if buying:
                buy = -prices[index] + dfs(index + 1, False)
                skip = dfs(index + 1, True)

                return max(buy, skip)

            else:
                sell = prices[index] + dfs(index + 2, True)
                hold = dfs(index + 1, False)

                return max(sell, hold)


        return dfs(0, True) 
        