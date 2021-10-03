class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=m*n:
            return []
        res = [[0]*n for _ in range(m)]
        for i in range(m*n):
            x = i//n
            y = i%n
            res[x][y]=original[i]
        return res