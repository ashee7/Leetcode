class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        for i in range(0,len(s),k):
            if (i+k)<=len(s):
                res.append(s[i:i+k])
            else:
                add=fill*(k-(len(s)%k))
                res.append(s[i:]+add)
            
        return res