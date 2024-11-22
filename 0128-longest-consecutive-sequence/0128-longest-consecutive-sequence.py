class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset=set(nums)
        longest=0
        for num in nums:
            if num-1 not in numset:
                d=1
                while num+d in numset:
                    d+=1
                longest=max(longest,d)
            
        return longest

