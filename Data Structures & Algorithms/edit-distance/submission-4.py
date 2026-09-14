from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # @lru_cache
        # def dfs(i, j):
        #     if i == len(word1):
        #         return len(word2) - j

        #     if j == len(word2):
        #         return len(word1) -  i

        #     if word1[i] == word2[j]:
        #         return dfs(i + 1, j + 1)

        #     insert = 1 + dfs(i, j + 1)
        #     remove = 1 + dfs(i + 1, j)
        #     replace = 1 + dfs(i + 1, j + 1)

        #     return min(insert, remove, replace)


        # return dfs(0, 0)

        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # If word2 is exhausted,
        # delete remaining characters from word1.
        for i in range(m + 1):
            dp[i][n] = m - i

        # If word1 is exhausted,
        # insert remaining characters from word2.
        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]

                else:
                    insert = dp[i][j + 1]
                    delete = dp[i + 1][j]
                    replace = dp[i + 1][j + 1]

                    dp[i][j] = 1 + min(
                        insert,
                        delete,
                        replace
                    )

        return dp[0][0]
        