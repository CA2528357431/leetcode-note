class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        if len(points)==1:
            return 1

        count = 1
        points.sort(key=lambda x:x[1])
        # 保证已经处理过的数据不会对后面产生影响

        curs,cure = points[0]
        for i in range(1,len(points)):
            s,e = points[i]
            if s>cure:
                curs,cure = s,e
                count+=1
            else:
                curs = max(curs,s)
                cure = min(cure,e)
        return count