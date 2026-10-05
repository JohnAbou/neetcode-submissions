class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingToOpen = {']':'[',')':'(','}':'{'}

        for c in s:
            if c in closingToOpen:
                if stack and stack[-1] == closingToOpen[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False
        