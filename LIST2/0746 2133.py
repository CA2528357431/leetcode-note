class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            s = set()
            for j in range(n):
                num = matrix[i][j]
                if num in s:
                    return False
                s.add(num)
        for i in range(n):
            s = set()
            for j in range(n):
                num = matrix[j][i]
                if num in s:
                    return False
                s.add(num)
        return True