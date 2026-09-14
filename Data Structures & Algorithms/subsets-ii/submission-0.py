class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []

        nums.sort()


        def backtrack(start):
            subsets.append(list(subset))
            

            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i-1]:
                    continue

                subset.append(nums[i])
                backtrack(i+1)


                subset.pop()

        backtrack(0)
        return subsets
                


        