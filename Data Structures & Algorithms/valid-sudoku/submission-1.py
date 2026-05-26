class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #hashset: validate entire board in one single pass
        #-> for each cell, check if digit已经存在于same row/col/3*3 box
        cols = defaultdict(set) #为什么defaultdict括号里还要加set
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r//3,c//3)]): #这里是判断格子属于哪个3*3小方块，得到的是3*3方块的编号
                    return False
                
                cols[c].add(board[r][c]) 
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True