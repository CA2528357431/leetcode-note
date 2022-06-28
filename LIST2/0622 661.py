class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                num=0
                s=0
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if x>=0 and x<m and y>=0 and y<n:
                            num+=1
                            s+=img[x][y]
                ans[i][j]=s//num
        return ans

