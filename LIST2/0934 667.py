class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:

        res = [i for i in range(1, n - (k + 1) + 1)]
        l = n - (k + 1) + 1
        r = n

        while l < r:
            res.append(l)
            l += 1
            res.append(r)
            r -= 1
        if l == r:
            res.append(l)

        return res