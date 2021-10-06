class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # BFS
        '''
        nums = 0
        m = len(grid)
        n = len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y]=="1":
                    nums+=1
                    grid[x][y]="0"
                    cur = [[x,y]]
                    while cur:
                        neo = []
                        for li in cur:
                            xx = li[0]
                            yy = li[1]
                            for xxx,yyy in [(xx+1,yy),(xx-1,yy),(xx,yy+1),(xx,yy-1)]:
                                if xxx<0 or xxx>=m or yyy<0 or yyy>=n or grid[xxx][yyy]=="0":
                                    continue
                                else:
                                    neo.append([xxx,yyy])
                                    grid[xxx][yyy]="0"

                        cur = neo
        return nums
        '''

        # DFS
        def find(xx,yy):
            for xxx,yyy in [(xx+1,yy),(xx-1,yy),(xx,yy+1),(xx,yy-1)]:
                if xxx<0 or xxx>=m or yyy<0 or yyy>=n or grid[xxx][yyy]=="0":
                    continue
                else:
                    grid[xxx][yyy]="0"
                    find(xxx,yyy)

        nums = 0
        m = len(grid)
        n = len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y]=="1":
                    nums+=1
                    grid[x][y]="0"
                    find(x,y)

        return nums