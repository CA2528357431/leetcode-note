class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = set()
        cur = 0

        for i in range(16):
            cur = cur + (1 << (2 * i))

            s.add(cur)
            s.add(cur << 1)

        return n in s
