class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left=0
        maxi=0
        k=set()
        right=0
        while right<len(s):
            if s[right] in k:
                while s[left]!=s[right] and left<right-1:
                    k.remove(s[left])
                    left+=1
                left+=1
            else: k.add(s[right])            
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi