class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        evens,odds=[],[]
        for num in c.values():
            if num%2==0:evens.append(num)
            else:odds.append(num)

        return max(odds)-min(evens)