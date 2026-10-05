class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        lowS = s.lower()

        while left < right:
            
            while left < right and not lowS[left].isalnum():
                left += 1
            
            while left < right and not lowS[right].isalnum():
                right -= 1 

            if lowS[left] != lowS[right]:
                return False
            
            left += 1
            right -= 1
        
        return True