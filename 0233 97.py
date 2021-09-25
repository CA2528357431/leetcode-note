class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        mat = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        mat[0][0] = True

        for x in range(1, len(s2) + 1):
            if s3[x - 1] == s2[x - 1] and mat[x - 1][0]:
                mat[x][0] = True
            else:
                break
        for x in range(1, len(s1) + 1):
            if s3[x - 1] == s1[x - 1] and mat[0][x - 1]:
                mat[0][x] = True
            else:
                break

        for x in range(1, len(s2) + 1):
            for y in range(1, len(s1) + 1):
                if mat[x - 1][y] and s2[x - 1] == s3[x + y - 1] or mat[x][y - 1] and s1[y - 1] == s3[x + y - 1]:
                    mat[x][y] = True
        return mat[-1][-1]