class Solution:    
    def isPalindrome(self, x: int) -> bool:
        x_str = f"{x}"
        rts_x = x_str[::-1]
        return x_str == rts_x