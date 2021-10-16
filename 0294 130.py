class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        clone = [x.copy() for x in board]

        def judge(x, y):
            clone[x][y] = "X"
            for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if xx < 0 or xx >= len(board) or yy < 0 or yy >= len(board[0]):
                    continue
                if clone[xx][yy] == "O":
                    judge(xx, yy)

        for x in range(len(board)):
            if clone[x][0] == "O":
                judge(x, 0)
            if clone[x][len(board[0]) - 1] == "O":
                judge(x, len(board[0]) - 1)
        for y in range(len(board[0])):
            if clone[0][y] == "O":
                judge(0, y)
            if clone[len(board) - 1][y] == "O":
                judge(len(board) - 1, y)

        for x in range(len(board)):
            for y in range(len(board[0])):
                if clone[x][y] == "O":
                    board[x][y] = "X"