class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        dic = {}
        for x, y in relations:
            if y not in dic:
                dic[y] = [x]
            else:
                dic[y].append(x)

        n = len(time)
        end = [-1] * (n + 1)

        def find(x):
            if x not in dic:
                end[x] = time[x - 1]
                return end[x]
            preend = -1
            for p in dic[x]:
                if end[p] == -1:
                    end[p] = find(p)
                preend = max(preend, end[p])
            end[x] = preend + time[x - 1]
            # 递归的同时更新数据
            return end[x]

        for x in range(1, n + 1):
            find(x)
        return max(end)