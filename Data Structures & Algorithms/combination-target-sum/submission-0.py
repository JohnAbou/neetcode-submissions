class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, curr, number):
            if number == target:
                ans.append(curr.copy())
                return
            
            if number > target or i >= len(nums):
                return

            curr.append(nums[i])
            dfs(i, curr, number + nums[i])

            curr.pop()
            dfs(i+1, curr, number)

        dfs(0, [], 0)
        return ans