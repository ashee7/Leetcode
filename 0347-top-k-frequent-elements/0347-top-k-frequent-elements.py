class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        arr=[[] for _ in range(max(count.values())+1)]
        for key,value in count.items():
            arr[value].append(key)
        res=[]
        j=-1
        while len(res)<k:
            res.extend(arr[j])
            j-=1
        return res