class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        sortednums=sorted(nums)
        res=1
        end=sortednums[0]+k
        for num in sortednums:
            print(num,end,res)
            if num<=end:
                continue
            else:
                end=num+k
                res+=1
            
        return res