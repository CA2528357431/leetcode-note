class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = set()
        for li in paths:
            dic.add(li[0])
        for li in paths:
            if li[1] not in dic:
                return li[1]