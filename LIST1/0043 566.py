class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        p = 0
        q = 0
        re = [[0]*c for _ in range(r)]
        for x in range(r):
            for y in range(c):
                re[x][y] = mat[p][q]
                q+=1
                if q==len(mat[0]):
                    q = 0
                    p+=1
        return re