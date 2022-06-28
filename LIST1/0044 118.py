class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        else:
            i=1
            res = [[1]]
            while i<numRows:
                i+=1
                res.append([1]*i)
                for x in range(1,i-1):
                    res[i-1][x] = res[i-2][x]+res[i-2][x-1]
            return res