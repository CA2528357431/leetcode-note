class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = {}
        for x in nums:
            dic[x] = dic.get(x,0)+1
        li = list(dic.keys())
        li.sort(key=lambda x:(dic[x],-x))
        res = []
        for x in li:
            neo = [x]*dic[x]
            res.extend(neo)
        return res