import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        final=[]
        j=0
        for i in range(k,len(nums)+1):
            final.append(self.XSum(nums[j:i],x))
            j+=1
        return final

    def XSum(self,a,k):
        total = 0
        counts = [0]*50
        for value in a:
            counts[value-1] += 1
        top_k = list(sorted(counts))[-k:]
        # print(top_k)
        for i in range(1,len(counts)+1):
            if counts[-i] in top_k:
                # print(counts[-i],(50-i+1))
                total += counts[-i]*(50-i+1)
                top_k.remove(counts[-i])
                
        return total