class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        req = {x: 0 for x in range(numCourses)}
        nxt = {x: [] for x in range(numCourses)}

        for x, y in prerequisites:
            req[x] = req[x] + 1
            nxt[y].append(x)

        res = []
        cur = [x for x in range(numCourses) if req[x] == 0]
        while cur:
            res.extend(cur)
            neo = []
            for k in cur:
                for kk in nxt[k]:
                    req[kk] -= 1
                    if req[kk] == 0:
                        neo.append(kk)
            cur = neo
        if len(res) == numCourses:
            return res
        else:
            return []