class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # 棋盘的第一行与第一列
        row = 0
        col = 0
        for i in range(n):
            row |= board[0][i] << i
            col |= board[i][0] << i
        reverseRow = ((1 << n) - 1) ^ row
        reverseCol = ((1 << n) - 1) ^ col

        rowCnt = 0
        colCnt = 0
        for i in range(n):
            currRow = currCol = 0
            for j in range(n):
                currRow |= board[i][j] << j
                currCol |= board[j][i] << j
            # 检测每一行和每一列的状态是否合法
            if (currRow != row and currRow != reverseRow) or \
                    (currCol != col and currCol != reverseCol):
                return -1
            if currRow == row:
                rowCnt += 1  # 记录与第一行相同的行数
            if currCol == col:
                colCnt += 1  # 记录与第一列相同的列数

        if n % 2 == 0:
            if rowCnt == n // 2 and colCnt == n // 2:
                pass
            else:
                return -1

            r_ones = row.bit_count()
            c_ones = col.bit_count()
            if r_ones == n // 2 and c_ones == n // 2:
                pass
            else:
                return -1
        else:
            if (rowCnt == n // 2 or rowCnt == n // 2 + 1) and (colCnt == n // 2 or colCnt == n // 2 + 1):
                pass
            else:
                return -1
            r_ones = row.bit_count()
            c_ones = col.bit_count()
            if (r_ones == n // 2 or r_ones == n // 2 + 1) and (c_ones == n // 2 or c_ones == n // 2 + 1):
                pass
            else:
                return -1

        def getMoves(mask: int) -> int:
            ones = mask.bit_count()
            if n % 2 == 1:
                # 如果n为奇数
                if ones == n // 2:
                    # 偶数位变为 1 的最小交换次数
                    return ones - (mask & 0xAAAAAAAA).bit_count()
                else:
                    # 奇数位变为 1 的最小交换次数
                    return ones - (mask & 0x55555555).bit_count()
            else:
                # 如果n为偶数
                # 偶数位变为1的最小交换次数
                count0 = ones - (mask & 0xAAAAAAAA).bit_count()
                # 奇数位变为1的最小交换次数
                count1 = ones - (mask & 0x55555555).bit_count()
                return min(count0, count1)

        rowMoves = getMoves(row)
        colMoves = getMoves(col)
        return rowMoves + colMoves