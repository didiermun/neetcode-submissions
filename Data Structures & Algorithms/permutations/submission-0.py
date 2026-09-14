class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        permutation = []
        used = [False]*len(nums)

        def backtrack():
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                permutation.append(nums[i])
                used[i] = True
                backtrack()

                #skip
                permutation.pop()
                used[i] = False
        
        backtrack()
        return permutations
        