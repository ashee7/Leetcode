class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned=set(banned)
        totalsum=0
        count=0
        for i in range(1,n+1):
            if i not in banned:
                totalsum+=i
                if totalsum>maxSum:
                    return count
                count+=1
        
        return count
                


        