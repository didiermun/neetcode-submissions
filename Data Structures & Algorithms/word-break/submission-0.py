class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for end in range(1, len(s)+1):
            for start in range(end):
                if dp[start] and s[start:end] in words:
                    dp[end] = True


        return dp[len(s)]
        