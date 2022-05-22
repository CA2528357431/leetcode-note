class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        res = max(special[0]-bottom,top-special[-1])
        n = len(special)
        for i in range(1,n):
            res = max(res,special[i]-special[i-1]-1)
        return res