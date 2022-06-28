class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        li = [0]*(m*n)
        i = 0
        for s in range(m+n-1):
            up = max(0,s+1-n)
            down = min(m-1,s)
            if s%2==0:
                for x in range(down,up-1,-1):
                    y = s-x
                    li[i] = mat[x][y]
                    i+=1
            else:
                for x in range(up,down+1):
                    y = s-x
                    li[i] = mat[x][y]
                    i+=1
        return li