class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        digit_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wyxz"
        }

        result = []
        combination = []

        def backtrack(index):
            if index == len(digits):
                result.append("".join(combination))
                return


            digit = digits[index]
            for char in digit_letters[digit]:
                combination.append(char)
                backtrack(index + 1)
                combination.pop()

        backtrack(0)

        return result
        