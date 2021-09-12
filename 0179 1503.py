class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        lt = 0
        if left:
            l = max(left)
            lt = l
        rt = 0
        if right:
            r = min(right)
            rt = n-r
        return max(lt,rt)
    # 其实碰不碰都没关系