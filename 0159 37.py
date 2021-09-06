class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        '''        
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

                for r in board:
                    res.append(r.copy())

                return
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
        do(0,0)
        for x in range(9):
            for y in range(9):
                board[x][y] = res[x][y]
        '''

        '''
        为什么这个函数return之后是none？
        对fun进行递归，fun1调用出fun1-1、fun1-2、fun1-3，我们return的仅仅是fun1-2，而我们接受到的结果实际上是fun1的return
        
        为什么会便会原样？
        如上文所提及，我们仅仅return了fun1-2，fun1以及其之前的递归正常进行，其回溯将结果board回溯成了原样
        
        
        
                   3   3  3   3
                     2      2
                         1
                我们return的是一个3，接受的却是1的结果         
                我们return了一个3，但其底层的1，2仍会进行，将board回溯成原样
        
        '''







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

        # 防止结果被回溯清空
        judge = False

        def do(x, y):
            nonlocal judge
            if x>8:
                judge = True
                return

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

                        # 防止结果被回溯清空
                        if judge:
                            return


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