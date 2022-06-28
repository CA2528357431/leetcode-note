class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        used = [[False] * n for _ in range(m)]

        def check(i, j, num):
            if board[i][j] != word[num]:
                return False
            else:
                if num == len(word) - 1:
                    return True

                used[i][j] = True
                for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ii < m and 0 <= jj < n and not used[ii][jj]:
                        neo = check(ii, jj, num + 1)
                        if neo:
                            return True
                used[i][j] = False
                return False

        for i in range(m):
            for j in range(n):
                judge = check(i, j, 0)
                if judge:
                    return True
        return False