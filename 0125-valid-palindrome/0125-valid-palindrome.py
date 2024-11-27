import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern=r'[a-z0-9]+'
        matches=re.findall(pattern,s.lower())
        st="".join(matches)
        return st==st[::-1]
