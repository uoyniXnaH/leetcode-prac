class Solution:    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        shortest_str = min(strs, key=len)
        if shortest_str == "":
            return ""
        shortest_len = len(shortest_str)
        if self.isCommonPrefix(strs, shortest_str):
            return shortest_str
        else:
            return self.recursiveFindCommonPrefix(shortest_str, strs, shortest_len//2, 0, shortest_len+1)

    def isCommonPrefix(self, strs: list[str], prefix: str) -> bool:
        for char in strs:
            if not char.startswith(prefix):
                return False
        return True
    
    def recursiveFindCommonPrefix(self, candidate: str, strs: list[str], current: int, last_pass: int, last_fail: int) -> str:
        if last_fail - last_pass == 1:
            return candidate[0:last_pass]
        if self.isCommonPrefix(strs, candidate[0:current]):
            return self.recursiveFindCommonPrefix(candidate, strs, (current+last_fail)//2, current, last_fail)
        else:
            return self.recursiveFindCommonPrefix(candidate, strs, (last_pass+current)//2, last_pass, current)