class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        ml = height[left]
        mh = height[right]
        while left < right:
            if height[left] < height[right]:
                ml = max(height[left], ml)
                ans += ml - height[left]
                left += 1
            else:
                mh = max(height[right], mh)
                ans += mh - height[right]
                right -= 1

        return ans
