class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        low = 0
        up = 0
        cur = 0
        for num in differences:
            cur+=num
            low = min(low,cur)
            up = max(up,cur)
        res = (upper-lower)-(up-low)+1
        return max(res,0)