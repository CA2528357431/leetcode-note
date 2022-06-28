class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        mat = [0] * 51
        for x, y in ranges:
            mat[x] += 1
            if y < 50:
                mat[y + 1] -= 1

        for i in range(1, 51):
            mat[i] += mat[i - 1]

        for i in range(left, right + 1):
            if mat[i] == 0:
                return False
        return True