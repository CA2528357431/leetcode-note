class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        tas = {}
        for x in target:
            tas[x] = tas.get(x,0)+1

        ars = {}
        for x in arr:
            ars[x] = ars.get(x,0)+1

        if len(tas)!=len(ars):
            return False
        for k in tas:
            if k in ars and ars[k]==tas[k]:
                continue
            else:
                return False
        return True