class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def do(i, j, n, word):
            if board[i][j] == word[n]:
                if n == len(word) - 1:
                    return True
                rem = board[i][j]
                board[i][j] = ""
                for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ii < len(board) and 0 <= jj < len(board[0]):
                        res = do(ii, jj, n + 1, word)
                        if res:
                            return True
                board[i][j] = rem
                return False
            else:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if do(i, j, 0, word):
                    return True
        return False