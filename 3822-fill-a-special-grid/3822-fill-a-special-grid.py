class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        if n==0:
            return [[0]]
        cnum=0
        grid=[[0]*(2**n) for _ in range(2**n)]

        def update(top, bottom, left, right,grid):
            nonlocal cnum

            if abs(top-bottom)==1 and abs(left-right)==1:
                grid[top][right]=cnum
                cnum+=1
                grid[bottom][right]=cnum
                cnum+=1
                grid[bottom][left]=cnum
                cnum+=1
                grid[top][left]=cnum
                cnum+=1
                return 

            update(top,(bottom+top)//2,((right+left)//2)+1,right,grid)
            update(((top+bottom)//2)+1,bottom,((right+left)//2)+1,right,grid)
            update(((top+bottom)//2)+1,bottom,left,(right+left)//2,grid)
            update(top,(bottom+top)//2,left,(right+left)//2,grid)

        update(0,(2**n)-1,0,(2**n)-1,grid)
        return grid
            