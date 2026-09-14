class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        dp = {0}

        for num in nums:
            next_dp = dp.copy()

            for curr_sum in dp:
                next_dp.add(curr_sum+num)

            dp = next_dp

        return target in dp
        