class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        class Solution:
            def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                dicreq = {x: 0 for x in range(numCourses)}
                dicnxt = {x: [] for x in range(numCourses)}
                for tar, req in prerequisites:
                    dicreq[tar] += 1
                    dicnxt[req].append(tar)

                cur = [k for k in dicreq.keys() if dicreq[k] == 0]
                while cur:
                    neo = []
                    for kk in cur:
                        for ne in dicnxt[kk]:
                            dicreq[ne] -= 1
                            if dicreq[ne] == 0:
                                neo.append(ne)
                    cur = neo
                for y in dicreq.values():
                    if y:
                        return False

                return True