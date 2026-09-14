class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(index, remaining):
            if remaining == 0:
                result.append(list(combination))
                return
            if remaining < 0 or index == len(nums):
                return

            #add curr number
            combination.append(nums[index])
            backtrack(index, remaining - nums[index])

            #skip curr number
            combination.pop()
            backtrack(index + 1, remaining)

        backtrack(0, target)

        return result
        