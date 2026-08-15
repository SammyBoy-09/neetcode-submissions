class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        ans = 0
        clen = 0
        for num in nums:
            if (num - 1) not in snums:
                clen = 0
                i = 0
                while True:
                    if (num + i) in snums:
                        clen += 1
                        i += 1
                    else:
                        break
            ans = max(ans, clen)

        return ans     