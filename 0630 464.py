class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        status = 1 << maxChoosableInteger
        mat = [-1] * status
        # i记录已经用过的数字
        # mat[i]表示used情况为i时，当前人能否必胜

        def dfs(used, desiredTotal):
            for i in range(maxChoosableInteger):
                cur = 1 << i
                if cur & used == 0:
                    # 如果i+1没被用
                    if desiredTotal <= i + 1:
                        mat[used] = 1
                        # 必胜
                        return True
                    if mat[cur | used] >= 0:
                        # 该情况计算过了
                        if mat[cur | used] == 0:
                            # 对方不能必胜
                            mat[used] = 1
                            return True
                    else:
                        # 该情况没计算过
                        if not dfs(cur | used, desiredTotal - i - 1):
                            # 对方不能必胜
                            mat[used] = 1
                            return True
            mat[used] = 0
            return False

        return dfs(0, desiredTotal)