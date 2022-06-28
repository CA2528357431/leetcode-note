class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        li = [[] for _ in range(101)]
        for x, y in rectangles:
            li[y].append(x)
        for l in li:
            l.sort()
        nn = len(points)
        res = [0] * nn

        def find(li, tar):
            if not li:
                return 0
            if li[-1] < tar:
                return 0
            if li[0] >= tar:
                return len(li)
            n = len(li)
            l = 0
            r = n - 1
            while l < r:
                mid = (l + r) // 2
                if li[mid] < tar:
                    l = mid + 1
                else:
                    r = mid
            return n - l

        for i in range(nn):
            x, y = points[i]
            cnt = 0
            for yy in range(y, 101):
                d = find(li[yy], x)
                cnt += d
            res[i] = cnt
        return res