class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        used = {}
        for c in arr:
            used[c] = used.get(c,0)+1
        for c in arr:
            if used[c]==1:
                count+=1
                if count==k:
                    return c
        return ""
