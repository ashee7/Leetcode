class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif=set()
        for i,num in enumerate(nums):
            if target-num in dif:
                return [nums.index(target-num),i]
            dif.add(num)
