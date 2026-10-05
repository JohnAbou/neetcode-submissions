class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                ans = min(nums[left], ans)
                break

            m = (left + right) // 2 
            
            if nums[m] >= nums[left]:
                left = m + 1
                ans = min(ans, nums[m])
            
            else:
                right = m - 1
                ans = min(ans, nums[m])
        return ans