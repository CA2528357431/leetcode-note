class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # 2-->死到活
        # 3-->活到死
        # 即用自制状态标记这个细胞 原来死活 以及 之后的死活

        def deal(x, y):
            count = 0
            for xx, yy in (
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1),
            (x + 1, y + 1)):
                if 0 <= xx < m and 0 <= yy < n:
                    if board[xx][yy] in (1, 3):
                        count += 1
            return count

        for x in range(m):
            for y in range(n):
                count = deal(x, y)
                if board[x][y] == 1:
                    if count < 2 or count > 3:
                        board[x][y] = 3
                    else:
                        board[x][y] = 1
                else:
                    if count == 3:
                        board[x][y] = 2
                    else:
                        board[x][y] = 0
        for x in range(m):
            for y in range(n):
                if board[x][y] == 2:
                    board[x][y] = 1
                elif board[x][y] == 3:
                    board[x][y] = 0