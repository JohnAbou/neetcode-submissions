class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(substring):
            return substring == substring[::-1]

        def dfs(start, curr):
            if start == len(s):
                ans.append(curr.copy())
                return

            for end in range(start, len(s)):
                substring = s[start:end+1]

                if isPalindrome(substring):
                    curr.append(substring)
                    dfs(end+1, curr)
                    curr.pop()

        dfs(0, [])
        return ans             