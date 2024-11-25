class Solution:
    
            
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def complement(arr):
            res=''
            for i in arr:
                if i=='1':res+='0'
                else:res+='1'
            return res
            
        d={}
        for row in matrix:
            row=''.join([str(i) for i in row])
            comp=complement(row)
            if row not in d.keys() and comp not in d.keys():
                d[row]=1
            elif row in d.keys():
                d[row]+=1
            elif comp in d.keys():
                d[comp]+=1
        return max(d.values())

        