class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def do(n):
            if n == 1:
                return 0
            el = (do(n - 1) + k) % n
            return el

        return do(n) + 1
# https://leetcode-cn.com/problems/find-the-winner-of-the-circular-game/solution/by-huang-bin-bin-7-zvh1/
