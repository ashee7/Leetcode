class Solution:
    def maximumDifference(self,nums):
        max_dif=-1
        
        for i in range(len(nums)-1):
            max_right=max(nums[i+1:])
            if max_right-nums[i]>0:
                max_dif=max(max_right-nums[i],max_dif)
            print(max_dif)
            
        return max_dif
