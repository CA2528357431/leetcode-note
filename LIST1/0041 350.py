class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = {}
        for x in nums1:
            if x not in dic1:
                dic1[x]=1
            else:
                dic1[x]+=1
        dic2 = {}
        for x in nums2:
            if x not in dic2:
                dic2[x]=1
            else:
                dic2[x]+=1
        res = []
        for x in dic1:
            if x in dic2:
                num = min(dic1[x],dic2[x])
                for _ in range(num):
                    res.append(x)
        return res