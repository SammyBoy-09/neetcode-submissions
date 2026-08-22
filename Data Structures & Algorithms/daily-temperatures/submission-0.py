class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        ans = [0] * len(temperatures)

        for i, curr in enumerate(temperatures):
            while stack and curr > temperatures[stack[-1]]:
                temp = stack.pop()

                ans[temp] = i - temp

            stack.append(i)

        return ans