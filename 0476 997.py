class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dicout = set()
        dicin = [0]*(n+1)
        for x,y in trust:
            dicout.add(x)
            dicin[y]+=1
        for i in range(1,n+1):
            if i not in dicout and dicin[i]==n-1:
                return i
        return -1