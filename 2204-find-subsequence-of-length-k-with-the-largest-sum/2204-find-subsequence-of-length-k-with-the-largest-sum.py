class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        numsdict=Counter(sorted(nums,reverse=True)[:k])
        res=[]
        for num in nums:
            if num in numsdict and numsdict[num]>0:
                res.append(num)
                numsdict[num]-=1
                if len(res)==k:
                    return res
        return res
