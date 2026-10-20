class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        characters = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def dfs(i, curr):
            if i == len(digits):
                ans.append(curr)
                return

            letters = characters[digits[i]]
            for letter in letters:
                dfs(i+1, curr+letter)

        if digits:
            dfs(0, "")

        return ans


