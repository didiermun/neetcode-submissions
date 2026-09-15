class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left <= right:
            subarrays = 1
            curr_sum = 0

            mid = left + (right-left)//2

            for num in nums:
                if curr_sum + num > mid:
                    curr_sum = 0
                    subarrays += 1

                curr_sum += num

            if subarrays <= k:
                right = mid - 1
            else:
                left = mid + 1

        return left

        