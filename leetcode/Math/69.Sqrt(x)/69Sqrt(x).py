class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left+1 < right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return int(mid)
            elif mid * mid > x:
                right = mid
            else:
                left = mid
        return int(left-1) if left * left > x else int(left)
        