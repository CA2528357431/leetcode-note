class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for x in range(1,rowIndex+1):
            neo = [1]*(x+1)
            for y in range(1,x):
                neo[y] = res[y]+res[y-1]
            res = neo
        return res