class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a,b,c=points
        if a[0]==b[0]==c[0] or a[1]==b[1]==c[1]:
            return False
        dx1=a[0]-b[0]
        dx2=a[0]-c[0]
        dy1=a[1]-b[1]
        dy2=a[1]-c[1]
        return dx1*dy2!=dx2*dy1