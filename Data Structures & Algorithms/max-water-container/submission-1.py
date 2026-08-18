class Solution:
    def maxArea(self, heights: List[int]) -> int:
        gmax = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            h = min(heights[i], heights[j])
            gmax = max(h * (j - i), gmax)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return gmax

        