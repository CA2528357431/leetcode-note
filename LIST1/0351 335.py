class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:

        # 归纳交错的情况
        n = len(distance)
        for i in range(n):
            if i >= 3:
                if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                    return True

            if i == 4:
                if distance[i] >= (distance[i - 2] - distance[i - 4]) and distance[i - 1] == distance[i - 3]:
                    return True

            if i >= 5:
                if distance[i] >= (distance[i - 2] - distance[i - 4]) and distance[i - 2] >= distance[i - 4] and \
                        distance[i - 1] >= (distance[i - 3] - distance[i - 5]) and distance[i - 1] <= distance[i - 3]:
                    return True
        return False
        # https://leetcode-cn.com/problems/self-crossing/solution/lu-jing-jiao-cha-by-leetcode-solution-dekx/