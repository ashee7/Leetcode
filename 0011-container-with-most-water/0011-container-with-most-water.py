class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        most=0
        while i!=j:
            if min(height[i],height[j])*(j-i)>most:
                most=min(height[i],height[j])*(j-i)
            if height[i]<height[j]:
                    i+=1
            else:j-=1
        return most