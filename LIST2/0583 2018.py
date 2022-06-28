class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        length = len(word)

        def do(i, j, cur, di):
            if cur == length:
                if i < 0 or i >= m or j < 0 or j >= n:
                    return True
                if board[i][j] == "#":
                    return True
                return False

            w = board[i][j]
            if w == " " or w == word[cur]:
                pass
            else:
                return False
            res = True
            if di == 0:
                res = do(i - 1, j, cur + 1, di)
            elif di == 1:
                res = do(i + 1, j, cur + 1, di)
            elif di == 2:
                res = do(i, j - 1, cur + 1, di)
            elif di == 3:
                res = do(i, j + 1, cur + 1, di)

            return res

        for i in range(length - 1, m):
            for j in range(n):
                ii = i + 1
                jj = j
                if ii < 0 or ii >= m or jj < 0 or jj >= n:
                    pass
                elif board[ii][jj] == "#":
                    pass
                else:
                    continue
                if do(i, j, 0, 0):
                    return True
        for i in range(m - length + 1):
            for j in range(n):
                ii = i - 1
                jj = j
                if ii < 0 or ii >= m or jj < 0 or jj >= n:
                    pass
                elif board[ii][jj] == "#":
                    pass
                else:
                    continue
                if do(i, j, 0, 1):
                    return True
        for i in range(m):
            for j in range(length - 1, n):
                ii = i
                jj = j + 1
                if ii < 0 or ii >= m or jj < 0 or jj >= n:
                    pass
                elif board[ii][jj] == "#":
                    pass
                else:
                    continue
                if do(i, j, 0, 2):
                    return True
        for i in range(m):
            for j in range(n - length + 1):
                ii = i
                jj = j - 1
                if ii < 0 or ii >= m or jj < 0 or jj >= n:
                    pass
                elif board[ii][jj] == "#":
                    pass
                else:
                    continue
                if do(i, j, 0, 3):
                    return True
        return False
