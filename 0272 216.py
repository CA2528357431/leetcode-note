class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def deep(start,cur):
            if start==10:
                if len(path) == k and cur==n:
                    res.append(path.copy())
                return
            deep(start+1,cur)

            path.append(start)
            deep(start+1,cur+start)
            path.pop()
        deep(1,0)
        return res