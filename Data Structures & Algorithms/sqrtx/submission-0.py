class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        # 9 sqrt(9) = 3
        # (0 + 9) / 2 = 4.5 == 
        while l <= r:
            m = (l + r) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1

        return r

        