class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # prefix,suffix=[0]*(len(nums)+1),[0]*(len(nums)+1)
        # for i in range(1,len(nums)+1):
        #     prefix[i]+=prefix[i-1]+nums[i-1]
        #     suffix[i]+=suffix[i-1]+nums[-i]

        # suffix=suffix[::-1]
        # prefix=prefix[1:]

        # ind1=prefix.index(max(prefix))
        # ind2=suffix[:-1].index(max(suffix[:-1]))
        # start=min(ind1,ind2)
        # end=max(ind1,ind2)
        # return sum(nums[start:end+1])
        
        res=nums[0]
        total=res

        # if len(nums)==1:
        #     return nums[0]

        for i in range(1,len(nums)):
            total=max(0,total)
            total+=nums[i]
            res=max(total,res)

        return res
