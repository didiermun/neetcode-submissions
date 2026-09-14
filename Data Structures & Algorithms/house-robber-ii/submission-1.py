class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(chunk):
            prev1 = chunk[0]
            prev2 = 0

            for i in range(1, len(chunk)):
                temp = prev1
                prev1 = max(prev2+chunk[i], prev1)
                prev2 = temp

            return prev1

        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))
            

        