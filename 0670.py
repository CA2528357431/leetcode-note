class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        s = set()
        for x,y,r in circles:
            dis = r*r
            for xx in range(x-r,x+r+1):
                for yy in range(y-r,y+r+1):
                    de = (x-xx)**2+(y-yy)**2
                    if de<=dis:
                        s.add((xx,yy))
        return len(s)