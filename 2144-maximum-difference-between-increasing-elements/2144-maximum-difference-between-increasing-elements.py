class Solution:
    def maximumDifference(self,nums):
        max_dif=-1
        cur_min=nums[0]
        for i in range(1,len(nums)):
            if cur_min<nums[i]:
                max_dif=max(max_dif,nums[i]-cur_min)
            else:
                cur_min=nums[i]
    
        return max_dif
