class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        s=s[::-1]
        total=0
        res=0

        for i in range(len(s)):

            if s[i]=='1':
                total+=2**i
                if total>k:
                    break
                res+=1
            print(total)

        return res+s.count('0')
