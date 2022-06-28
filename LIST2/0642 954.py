class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        dic = {}
        for n in arr:
            if n>=0 and n%2==0 and n//2 in dic:
                neo = n//2
                dic[neo]-=1
                if dic[neo]==0:
                    dic.pop(neo)
            elif n<0 and n*2 in dic:
                neo = n*2
                dic[neo]-=1
                if dic[neo]==0:
                    dic.pop(neo)

            else:
                if n not in dic:
                    dic[n] = 0
                dic[n]+=1
        return len(dic)==0