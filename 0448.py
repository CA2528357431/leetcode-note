class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        meetings.sort(key=lambda x: (x[-1], x[0]))
        # 先用time进行时间排序，随后用x排序，便于区分组别

        neodic = {}
        for x, y, time in meetings:
            if time not in neodic:
                neodic[time] = []
            for s in neodic[time]:
                if x in s or y in s:
                    s.add(x)
                    s.add(y)
                    break
            else:
                neodic[time].append({x, y})

        used = {0, firstPerson}

        for time in neodic:
            for s in neodic[time]:
                if len(s & used) != 0:
                    for c in s:
                        used.add(c)

        return list(used)
