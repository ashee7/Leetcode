class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def pro(arr):
            l=[1]
            for i in arr:
                l.append(l[-1]*i)
            return l
        prepro=pro(nums)
        sufpro=pro(nums[::-1])[::-1]
        res=[]
        for i in range(len(nums)):
            res.append(prepro[i]*sufpro[i+1])
        return res