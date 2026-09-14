from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache
        def dfs(index, curr_sum):
            if index == len(nums):
                return 1 if curr_sum == target else 0

            add = dfs(index + 1, curr_sum + nums[index])
            substract = dfs(index + 1, curr_sum - nums[index])

            return add + substract

        return dfs(0, 0)

        