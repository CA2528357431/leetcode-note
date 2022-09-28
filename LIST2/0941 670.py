class Solution:
    def maximumSwap(self, num: int) -> int:
        li = list(str(num))
        n = len(li)
        res = [i for i in range(n)]

        for x in range(n - 2, -1, -1):
            if li[x] <= li[res[x + 1]]:
                res[x] = res[x + 1]

        for x in range(n):
            tar = res[x]
            if tar == x:
                continue
            if li[tar] == li[x]:
                continue

            li[tar], li[x] = li[x], li[tar]
            break

        return int("".join(li))