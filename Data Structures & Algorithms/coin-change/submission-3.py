class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        required = [float("inf")]*(amount+1)
        required[0] = 0

        for bill in range(1, amount+1):
            for coin in coins:
                if coin <= bill:
                    required[bill] = min(required[bill], 1 + required[bill - coin] )

        return required[amount] if required[amount] != float("inf") else -1