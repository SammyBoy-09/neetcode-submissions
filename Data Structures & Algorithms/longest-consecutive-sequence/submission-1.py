class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        ans = 0
        clen = 0
        for num in nums:
            if (num - 1) not in snums:
                clen = 1
                cnum = num
                while (cnum + 1) in snums:
                    clen += 1
                    cnum += 1
            ans = max(ans, clen)

        return ans     