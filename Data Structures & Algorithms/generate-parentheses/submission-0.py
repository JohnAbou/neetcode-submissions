class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(curr, opened, closed):
            if opened == n and closed == n:
                ans.append(curr)
                return

            if opened < n:
                dfs(curr + "(", opened + 1, closed)

            if closed < opened:
                dfs(curr + ")", opened, closed + 1)

        dfs("", 0, 0)
        return ans