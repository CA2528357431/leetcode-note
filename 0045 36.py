class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        line = {}
        row = {}
        box = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
        for y in range(len(board[0])):
            for x in range(len(board[0])):
                if board[y][x]!=".":
                    if board[y][x] not in line:
                        line[board[y][x]] = set()
                    if board[y][x] not in row:
                        row[board[y][x]] = set()

                    if y not in line[board[y][x]]:
                        line[board[y][x]].add(y)
                    else:
                        return False

                    if x not in row[board[y][x]]:
                        row[board[y][x]].add(x)
                    else:
                        return False

                    if board[y][x] not in box[y//3][x//3]:
                        box[y//3][x//3].add(board[y][x])
                    else:
                        return False
        return True
