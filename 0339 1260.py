class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        def swap(xx, yy):
            i = xx * n + yy - k
            x, y = i // n % m, i % n
            return (x, y)

        neo = [x.copy() for x in grid]
        for xx in range(m):
            for yy in range(n):
                xxx, yyy = swap(xx, yy)
                neo[xx][yy] = grid[xxx][yyy]
        return neo
