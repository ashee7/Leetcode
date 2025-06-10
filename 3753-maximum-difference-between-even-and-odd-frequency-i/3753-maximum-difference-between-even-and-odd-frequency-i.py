class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        freqs=sorted(c.values())
        evens=[]
        odds=[]
        for num in freqs:
            if num%2==0:
                evens.append(num)
            else:
                odds.append(num)
                
        return odds[-1]-evens[0]

