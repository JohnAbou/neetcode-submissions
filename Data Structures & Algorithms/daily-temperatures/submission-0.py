class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackT, stackI = stack.pop()
                ans[stackI] = index - stackI
            stack.append([temperature, index])
        return ans