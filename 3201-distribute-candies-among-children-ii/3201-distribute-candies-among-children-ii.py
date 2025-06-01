class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count=0
        for i in range(min(limit,n)+1):
            if n-i>limit*2:
                continue
            count+=min(limit,n-i)-max(0,n-i-limit)+1
        return count