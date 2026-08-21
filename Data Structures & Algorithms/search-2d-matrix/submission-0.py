class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = sum(matrix, [])

        l = mid = 0
        h = len(m) - 1

        while l <= h:
            mid = (l + h) // 2
            if m[mid] == target:
                return True
            elif m[mid] > target:
                h -= 1
            else:
                l += 1

        return False