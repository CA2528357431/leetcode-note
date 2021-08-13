class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        res = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]

        for x in range(0,len(word1)+1):
            res[0][x]=x
        for x in range(0,len(word2)+1):
            res[x][0]=x

        for x in range(1,len(word2)+1):
            for y in range(1,len(word1)+1):
                change = res[x-1][y-1]
                a = res[x][y-1]+1
                b = res[x-1][y]+1
                if word1[y-1]!=word2[x-1]:
                    change+=1
                res[x][y] = min(change,a,b)
        return res[-1][-1]

    # 最后一步有三种可能

    # 向word1插入
    # 插入的是word2最后一位（插入别的也行，但不好思考）
    # 匹配word1和word2[:-1]

    # 向word1删除
    # 删除的是word1最后一位（删除别的也行，但不好思考）
    # 匹配word1[:-1]和word2

    # 向word1改变
    # 匹配word1[:-1]和word2[:-1]