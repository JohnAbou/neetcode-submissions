class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(i, curr, number):
            if number == target:
                ans.append(curr.copy())
                return

            if number > target or i >= len(candidates):
                return

            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                
                curr.append(candidates[j])
                dfs(j+1, curr, number + candidates[j])

                curr.pop()
                prev = candidates[j]

        dfs(0, [], 0)
        return ans