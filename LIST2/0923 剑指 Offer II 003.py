class Solution:
    def countBits(self, n: int) -> List[int]:
        def cnt(x):
            res = 0
            while x:
                x = x&(x-1)
                res+=1
            return res
        res = [cnt(x) for x in range(n+1)]
        return res


