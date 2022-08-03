class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        li=list(set(arr))
        li.sort()
        dic={}
        for i in range(len(li)):
            dic[li[i]]=1+i
        return [dic[i] for i in arr]