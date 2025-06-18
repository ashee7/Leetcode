class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        sorted_nums=sorted(nums)
        # arr=[]
        # dif=0
        # res=[]
        # totaldif=0
        # for i in range(1,len(sorted_nums)+1):
        #     arr.append(sorted_nums[i-1])
        #     if i%3==0:
        #         if totaldif>k:
        #             return []
        #         res.append(arr)
        #         arr=[]
        #         totaldif=0
        #         continue
        #     dif=sorted_nums[i]-sorted_nums[i-1]
        #     totaldif+=dif
        # return res
        res=[]
        for i in range(0,len(nums),3):
            if (sorted_nums[i+2]-sorted_nums[i])>k:
                return []
            res.append(sorted_nums[i:i+3])
        return res