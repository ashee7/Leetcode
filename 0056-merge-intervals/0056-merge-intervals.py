class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=(lambda x: x[0]))
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            start1,end1=result[-1]
            start2,end2=intervals[i]
            if start2<=end1:
                result.pop()
                result.append([min(start1,start2),max(end1,end2)])
            else:
                result.append(intervals[i])
        return result