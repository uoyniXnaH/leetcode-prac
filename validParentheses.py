class Solution:
    units = ["()", "[]", "{}"]
    
    def __init__(self):
        self.i = 0
    
    @staticmethod
    def cut(s, i):
        return s[:i] + s[i+2:]
    
    def isValid(self, s):
        print(s)
        if len(s) <= 2:
            return s in self.units
        if len(s) < self.i + 2:
            return False
        if s[self.i] + s[self.i + 1] in self.units:
            new_s = self.cut(s, self.i)
            self.i -= 1
            return self.isValid(new_s)
        else:
            self.i += 1
            return self.isValid(s)
