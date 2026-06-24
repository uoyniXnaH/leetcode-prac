class Solution:
    def reverse(self, x: int) -> int:
        if x > 2147483647 or x < -2147483648:
            return 0
        x_abs = x if x > 0 else abs(x)
        n = f"{x_abs}"
        n = n[::-1]
        res = int(n)
        if res > 2147483647:
            return 0
        if x < 0:
            res = -res
        return res