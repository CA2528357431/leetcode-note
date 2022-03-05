class Solution:
    def countPoints(self, rings: str) -> int:
        if not rings:
            return 0
        dic={}
        for i in range(len(rings)//2):
            n=rings[i*2]
            c=rings[i*2+1]
            if c not in dic:
                dic[c]=set()
            dic[c].add(n)
        cur=0
        for c in dic:
            if len(dic[c])==3:
                cur+=1
        return cur