class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        # https://leetcode-cn.com/problems/perfect-rectangle/solution/tong-ge-lai-shua-ti-la-zhao-gui-lu-ji-ba-oszq/

        used = {}

        minx = 9999
        miny = 9999
        maxx = -1
        maxy = -1

        sumarea =0

        for x1,y1,x2,y2 in rectangles:
            minx = min(x1,minx)
            miny = min(y1,miny)
            maxx = max(x2,maxx)
            maxy = max(y2,maxy)
            for pos in [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]:
                if pos not in used:
                    used[pos] = 0
                used[pos]+=1
            sumarea+=(x2-x1)*(y2-y1)

        if sumarea!=(maxy-miny)*(maxx-minx):
            return False

        li = 0
        for pos in used:
            if used[pos]%2==1:
                li+=1
                if pos[0] != minx and pos[0]!=maxx:
                    return False
                if pos[1] != miny and pos[1]!=maxy:
                    return False
        if li==4:
            return True
        else:
            return False
