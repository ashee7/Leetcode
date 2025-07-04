class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=(lambda x: x[0]))
        result=[intervals[0]]
        for start2,end2 in intervals[1:]:
            start1,end1=result[-1]
            if start2<=end1:
                result.pop()
                result.append([min(start1,start2),max(end1,end2)])
            else:
                result.append([start2,end2])

        return result