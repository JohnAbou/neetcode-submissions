class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, number in enumerate(nums):
            if index > 0 and number == nums[index-1]:
                continue
            
            left = index + 1
            right = len(nums) - 1

            while left < right:
                if number + nums[left] + nums[right] < 0:
                    left += 1

                elif number + nums[left] + nums[right] > 0:
                    right -= 1
                
                else:
                    res.append([number, nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left+=1

        return res

