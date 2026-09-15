class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            days_needed = 1
            curr_weight = 0
            capacity = left + (right - left)//2

            for weight in weights:
                if curr_weight + weight > capacity:
                    days_needed += 1
                    curr_weight = 0

                curr_weight += weight

            if days_needed <= days:
                right = capacity - 1
            else:
                left = capacity + 1

        return left
        