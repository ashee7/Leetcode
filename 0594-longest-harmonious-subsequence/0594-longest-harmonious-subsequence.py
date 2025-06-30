class Solution:
    def findLHS(self, nums: List[int]) -> int:
        sortnums=sorted(nums)

        # countskeys=sorted(counts.keys())
        # total=0
        # for i in range(len(countskeys)-1):
        #     mini=countskeys[i]
        #     maxi=countskeys[i+1]

        #     if maxi-mini==1:
        #         total=max(total,counts[mini]+counts[maxi])
                
        # return total
        
        total=0
        i,j=0,0
        while i <len(sortnums):
            if sortnums[i]-sortnums[j]>1:
                j+=1
            else:
                if sortnums[i]-sortnums[j]==1:
                    total=max(total,i-j+1)
                i+=1
        return total