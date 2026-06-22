class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        hold = ""
        for i in range(0, len(s)):
            hold = s[i]
            border = min(i, len(s)-i-1)
            for j in range(1, border+1):
                if s[i-j] == s[i+j]:
                    hold = s[i-j] + hold + s[i+j]
                elif len(hold) > len(ans):
                    ans = hold
                    break
                else:
                    break
            if len(hold) > len(ans):
                ans = hold
        for i in range(0, len(s)-1):
            if s[i+1] != s[i]:
                continue
            hold = s[i] + s[i+1]
            border = min(i, len(s)-i-2)
            for j in range(1, border+1):
                if s[i-j] == s[i+j+1]:
                    hold = s[i-j] + hold + s[i+j+1]
                elif len(hold) > len(ans):
                    ans = hold
                    break
                else:
                    break
            if len(hold) > len(ans):
                ans = hold
        return ans
