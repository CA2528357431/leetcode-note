class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        n = len(prices)

        def do(i):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    return prices[i] - prices[j]
            return prices[i]

        return [do(i) for i in range(n)]