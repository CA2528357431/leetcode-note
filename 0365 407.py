class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])
        used = [[False] * n for _ in range(m)]

        queue = []

        # heapq.heappush(queue, (p, xxx))
        # 可以向堆中以p为key插入(p,xxx)

        for i in range(m):
            used[i][0] = True
            heapq.heappush(queue, (heightMap[i][0], [i, 0]))
            used[i][n - 1] = True
            heapq.heappush(queue, (heightMap[i][n - 1], [i, n - 1]))

        for i in range(1, n - 1):
            used[0][i] = True
            heapq.heappush(queue, (heightMap[0][i], [0, i]))
            used[m - 1][i] = True
            heapq.heappush(queue, (heightMap[m - 1][i], [m - 1, i]))

        # 先布满边界，然后从边界“最小”点向“内”搜索并更新边界，直到搜索完全部节点

        res = 0

        while queue:
            element = heapq.heappop(queue)
            # 拿出最小点

            minH = element[0]
            x, y = element[1]
            for (xx, yy) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= xx < m and 0 <= yy < n and used[xx][yy] == False:
                    used[xx][yy] = True

                    res += max(minH - heightMap[xx][yy], 0)
                    # 能否存水

                    heapq.heappush(queue, (max(heightMap[xx][yy], minH), [xx, yy]))
                    # 更新边界

        return res