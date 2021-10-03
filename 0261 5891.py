class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean*(m+n)
        total = total-sum(rolls)
        if total>n*6 or total<n*1:
            return []
        res = [total//n for _ in range(n)]
        re = total%n
        for i in range(re):
            res[i]+=1
        return res