class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:

        stockPrices.sort(key=lambda x: x[0])
        n = len(stockPrices)

        if n == 1:
            return 0
        if n == 2:
            return 1

        cnt = 1
        predy = (stockPrices[1][1] - stockPrices[0][1])
        predx = (stockPrices[1][0] - stockPrices[0][0])
        a = math.gcd(predx, predy)
        predy //= a
        predx //= a
        for i in range(2, n):
            prex, prey = stockPrices[i - 1]
            curx, cury = stockPrices[i]
            curdy = (cury - prey)
            curdx = (curx - prex)
            a = math.gcd(curdx, curdy)
            # 直接除法不行
            curdy //= a
            curdx //= a
            if curdx == predx and curdy == predy:
                continue
            else:
                predx = curdx
                predy = curdy
                cnt += 1
        return cnt