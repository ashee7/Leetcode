class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        schars=[0]*26
        tchars=[0]*26
        for i in range(len(s)):
            schars[ord(s[i])-ord('a')]+=1
            tchars[ord(t[i])-ord('a')]+=1
        
        return tchars==schars
