class node:
    def __init__(self, i, li):
        self.li = li
        self.i = i

    def __lt__(self, other):
        if -self.li[self.i] < -other.li[other.i]:
            return True
        if -self.li[self.i] == -other.li[other.i] and self.i < other.i:
            return True
        return False


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:

        n = len(floor)
        if numCarpets * carpetLen >= n:
            return 0
        cnt = 0
        li = [0] * n
        for i in range(n):
            if floor[i] == "1":
                cnt += 1
                li[i] = 1
        if cnt <= numCarpets:
            return 0
        if cnt == n:
            return n - numCarpets * carpetLen

        def do(i, li):
            l = i
            r = min(n - 1, i + carpetLen - 1)
            res = 0
            for j in range(l, r + 1):
                if li[j] == 1:
                    res += 1
            return res

        have = [0] * n
        for i in range(n):
            have[i] = do(i, li)

        heap = [node(i, have) for i in range(n)]

        heapq.heapify(heap)

        while have[heap[0].i] and numCarpets:

            numCarpets -= 1
            j = heap[0].i
            for i in range(j, min(n, j + carpetLen)):
                li[i] = 0

            for i in range(max(0, j - carpetLen + 1), min(n, j + carpetLen)):
                have[i] = do(i, li)
            heapq.heapify(heap)

        return sum(li)



