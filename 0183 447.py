class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0

        for x, y in points:
            dic = {}
            for xx, yy in points:
                dis = (x - xx) * (x - xx) + (y - yy) * (y - yy)
                if dis not in dic:
                    dic[dis] = 1
                else:
                    res += dic[dis] * 2
                    dic[dis] += 1
        return res