class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            hours =  0
            mid = left + (right - left) // 2
            for pile in piles:
                hours += (pile + mid - 1) // mid
            
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left
        