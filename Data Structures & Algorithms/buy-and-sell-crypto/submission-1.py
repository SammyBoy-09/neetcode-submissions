class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = float("inf")

        for p in prices:
            if p < buy:
                buy = p

            else:
                ans = max(ans, (p-buy))

        return ans
        