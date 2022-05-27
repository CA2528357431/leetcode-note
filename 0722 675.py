class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if forest[0][0]==0:
            return -1
        dic = {1:(0,0)}
        nums = [1,]
        m = len(forest)
        n = len(forest[0])
        for i in range(m):
            for j in range(n):
                num = forest[i][j]
                if num not in [0,1]:
                    dic[num] = (i,j)
                    nums.append(num)
        nums.sort()

        def find(ax,ay,bx,by):
            used = [[False]*n for _ in range(m)]
            cur = [(ax,ay)]
            used[ax][ay] = True
            step = 0
            while cur:
                nxt = []
                for x,y in cur:
                    if x==bx and y==by:
                        return step
                    for xx,yy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                        if xx<0 or xx>=m or yy<0 or yy>=n or forest[xx][yy]==0 or used[xx][yy]:
                            continue
                        used[xx][yy] = True
                        nxt.append((xx,yy))
                step += 1
                cur = nxt
            return -1
        cur = 0
        t = len(nums)
        for i in range(1,t):
            p = nums[i-1]
            px,py = dic[p]
            c = nums[i]
            cx,cy = dic[c]
            neo = find(px,py,cx,cy)
            if neo<0:
                return -1
            cur+=neo
        return cur





