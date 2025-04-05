class Solution:
    def romanToInt(self, s: str) -> int:
        extend = {
            'I': 1,
            'Q': 4,
            'V': 5,
            'W': 9,
            'X': 10,
            'E': 40,
            'L': 50,
            'R': 90,
            'C': 100,
            'T': 400,
            'D': 500,
            'Y': 900,
            'M': 1000
        }
        s_extend = s.replace('IV', 'Q').replace('IX', 'W').replace('XL', 'E').replace('XC', 'R').replace('CD', 'T').replace('CM', 'Y')
        result = 0
        for char in s_extend:
            result += extend[char]
        return result
