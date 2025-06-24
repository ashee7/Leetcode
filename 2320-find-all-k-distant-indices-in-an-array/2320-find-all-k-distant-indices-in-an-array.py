class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res=list()
        for i in range(len(nums)):
            if nums[i]==key:
                res+=list(range(max(0,i-k),min(len(nums),i+k+1)))
        
        return list(set(res))