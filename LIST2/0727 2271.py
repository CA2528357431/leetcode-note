class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:

        tiles.sort(key=lambda x: x[0])
        n = len(tiles)
        ii = 0
        res = -1

        cur = [0] * n
        cur[0] = tiles[0][1] - tiles[0][0] + 1
        for i in range(1, n):
            cur[i] += cur[i - 1] + (tiles[i][1] - tiles[i][0] + 1)
        for i in range(n):
            s, e = tiles[i]
            start = s
            end = start + carpetLen - 1
            while ii < n and end >= tiles[ii][0]:
                ii += 1
            neo = 0
            if i > 0:
                neo -= cur[i - 1]
            if ii >= 2:
                neo += cur[ii - 2]
            neo += (min(end, tiles[ii - 1][1]) - tiles[ii - 1][0] + 1)
            res = max(res, neo)
        return res
