class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])

        def check(x, y):
            if board[x][y] == ".":
                return 0
            board[x][y] = "."

            xx = x
            while xx + 1 < m and board[xx + 1][y] == "X":
                board[xx + 1][y] = "."
                xx += 1

            yy = y
            while yy + 1 < n and board[x][yy + 1] == "X":
                board[x][yy + 1] = "."
                yy += 1
            return 1

        res = 0
        for x in range(m):
            for y in range(n):
                res += check(x, y)
        return res