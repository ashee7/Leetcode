class Solution:
    def climbStairs(self, n: int) -> int:
        s=list()
        s.append(1) # base case when 1 step only remains
        s.append(2) # base case when 2 steps remain
        if n<2:
            return s[n-1]
        for _ in range(3,n+1):
            s.append(s[-1]+s[-2])
        
        return s[-1]