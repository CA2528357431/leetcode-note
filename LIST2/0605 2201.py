class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        mat = [[False] * n for _ in range(n)]
        for x, y in dig:
            mat[x][y] = True

        def judge(lx, ly, rx, ry):
            res = True
            for x in range(lx, rx + 1):
                for y in range(ly, ry + 1):
                    if not mat[x][y]:
                        return False
            return True

        res = 0
        for lx, ly, rx, ry in artifacts:
            if judge(lx, ly, rx, ry):
                res += 1
        return res