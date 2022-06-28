class Solution:
    def numWays(self, n: int) -> int:
        la = 0
        cur = 1

        for i in range(n):
            la, cur = cur, la + cur

        return cur % 1000000007