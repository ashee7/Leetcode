class Solution:
    def possibleStringCount(self, word: str) -> int:
        last=None
        res=1
        for char in word:
            if char==last:
                res+=1
            else:
                last=char

        return res