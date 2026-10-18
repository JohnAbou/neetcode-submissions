class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(curr):
            if len(nums) == len(curr):
                ans.append(curr.copy())
                return

            for i in nums:
                if i not in curr:
                    curr.append(i)
                    dfs(curr)
                    curr.pop()

        dfs([])
        return ans