class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts=Counter(nums)
        countskeys=sorted(counts.keys())
        total=0
        for i in range(len(countskeys)-1):
            mini=countskeys[i]
            maxi=countskeys[i+1]

            if maxi-mini==1:
                total=max(total,counts[mini]+counts[maxi])
                
        return total
