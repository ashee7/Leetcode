class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=defaultdict(set)
        rows=defaultdict(set)
        boxes=defaultdict(set)

        for r in range(9):
            for c in range(9):
                element=board[r][c]
                if element!='.':
                    if element in rows[r] or element in cols[c] or element in boxes[(r//3,c//3)]:
                        return False
                    
                    rows[r].add(element)
                    cols[c].add(element)
                    boxes[(r//3,c//3)].add(element)
        return True

                
