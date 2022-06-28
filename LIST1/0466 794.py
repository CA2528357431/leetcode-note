class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        def judge(p):
            win = False
            for i in range(3):
                judge = board[i][0] == p and board[i][1] == p and board[i][2] == p or board[0][i] == p and board[1][
                    i] == p and board[2][i] == p
                if judge:
                    win = True
            judge = board[0][0] == p and board[1][1] == p and board[2][2] == p or board[0][2] == p and board[1][
                1] == p and board[2][0] == p
            if judge:
                win = True
            return win

        countx = 0
        counto = 0
        for string in board:
            for c in string:
                if c == "X":
                    countx += 1
                elif c == "O":
                    counto += 1
        if counto > countx or countx - counto > 1:
            return False

        return not (counto == countx - 1 and judge('O') or counto == countx and judge('X'))
        # o赢，则x放不了下一个，数量一样
        # x赢，则o放不了下一个，数量一样