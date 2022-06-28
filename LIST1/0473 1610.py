class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        same = 0
        angles = []
        for x, y in points:
            if x == location[0] and y == location[1]:
                same += 1
            else:
                neo = math.atan2(y - location[1], x - location[0])
                angles.append(neo)
        angles.sort()
        n = len(angles)
        anglesP = [x + 2 * math.pi for x in angles]
        angles = angles + anglesP
        angle = angle / 180 * math.pi

        res = 0
        r = 0
        for l in range(n):
            while angles[r] - angles[l] <= angle:
                r += 1
            res = max(res, r - l)
        return res + same

# 其实就是首尾相连的滑动窗口