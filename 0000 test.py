class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = [set() for _ in range(9)]
        line = [set() for _ in range(9)]
        box = [[set(), set(), set()] for _ in range(3)]
        for x in range(9):
            for y in range(9):
                line[x].add(board[x][y])
                row[y].add(board[x][y])
                box[x // 3][y // 3].add(board[x][y])

        row = [set() for _ in range(9)]
        line = [set() for _ in range(9)]
        box = [[set(), set(), set()] for _ in range(3)]
        for x in range(9):
            for y in range(9):
                line[x].add(board[x][y])
                row[y].add(board[x][y])
                box[x // 3][y // 3].add(board[x][y])
        res = []
        def do(x, y):
            if x>8:

                neo = [r.copy() for r in board]

                return neo
            if board[x][y] == ".":
                for i in "123456789":
                    if (i not in row[y]) and (i not in line[x]) and (i not in box[x // 3][y // 3]):

                        board[x][y] = i

                        row[y].add(i)
                        line[x].add(i)
                        box[x // 3][y // 3].add(i)

                        yy = y+1
                        xx = x
                        if yy==9:
                            yy = 0
                            xx = x+1

                        do(xx,yy)

                        board[x][y] = "."

                        line[x].remove(i)
                        row[y].remove(i)
                        box[x // 3][y // 3].remove(i)
            else:
                y += 1
                if y == 9:
                    y = 0
                    x += 1
                do(x, y)


        x = do(0,0)
        print("return 的结果")
        print(x)

        print("do 外的输出")
        print(board)
sol = Solution()
sol.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])