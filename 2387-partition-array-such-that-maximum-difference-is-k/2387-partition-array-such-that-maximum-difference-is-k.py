class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=1
        end=nums[0]+k
        for num in nums:
            if num>end:
                end=num+k
                res+=1
        return res