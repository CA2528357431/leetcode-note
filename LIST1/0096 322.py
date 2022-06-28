class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [999999999] * (amount + 1)
        res[0] = 0

        for x in range(1, len(res)):
            for y in coins:
                if x - y >= 0:
                    res[x] = min(res[x - y] + 1, res[x])
        if res[-1] == 999999999:
            return -1
        else:
            return res[-1]