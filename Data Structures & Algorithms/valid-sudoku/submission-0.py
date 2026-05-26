class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        for row in range(9):
            seen = set() #()默认是tuple（不可变），这里要用set，因为要检查是否重复
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        for col in range(9):
            seen = set() #这是作用域，Python不会把上一个seen带到下一个循环
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        for square in range(9): #在找第几个3*3方块
            seen = set()
            for i in range(3): #方块内部的第几行
                for j in range(3): #内部的第几列
                    # 0 1 2
                    # 3 4 5
                    # 6 7 8
                    row = (square//3)*3+i # //3是判断在第几行
                    col = (square%3)*3+j # *3是为了变成其在整个棋盘上的坐标（每个方块长宽都是3）
                    # +i是为了在方块内部移动（*3是找到方块的起点）
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True