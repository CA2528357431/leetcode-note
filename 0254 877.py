class Solution:
    def stoneGame(self, piles) -> bool:
        # 数学
        '''
        return True
        '''

        # 动态规划
        n = len(piles)

        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            mat[i][i] = piles[i]
        for length in range(2, n+1):
            for l in range(0, n - length+1):

                r = l + length - 1
                left = piles[l] - mat[l + 1][r]
                right = piles[r] - mat[l][r - 1]
                mat[l][r] = max(left, right)
        return mat[0][- 1]>0
