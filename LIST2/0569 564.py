class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if l == 1:
            return str(int(n) - 1)
        pre = int(n[:(l + 1) // 2])

        up = 10 ** l + 1
        low = 10 ** (l - 1) - 1
        li = [up, low]
        for i in range(-1, 2):
            pp = pre + i
            todo = pp
            if l % 2 == 1:
                todo = todo // 10
            while todo:
                pp = pp * 10 + todo % 10
                todo = todo // 10
            if pp != int(n):
                li.append(pp)
        neo = [abs(x - int(n)) for x in li]

        i = 0
        for ii in range(1, len(li)):
            if neo[ii] < neo[i] or neo[ii] == neo[i] and li[ii] < li[i]:
                i = ii

        return str(li[i])