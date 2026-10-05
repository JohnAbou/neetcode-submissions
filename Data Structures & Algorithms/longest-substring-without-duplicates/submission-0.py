class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        wind = set()

        for r in range(len(s)):
            while s[r] in wind:
                wind.remove(s[l])
                l += 1
            
            wind.add(s[r])
            ans = max(ans, len(wind))

        return ans