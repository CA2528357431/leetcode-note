class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) == 0 or len(changed) % 2 == 1:
            return []

        changed.sort()
        dic = {}
        res = []
        for x in changed:
            if x / 2 in dic:
                dic[x / 2] -= 1
                if dic[x / 2] == 0:
                    dic.pop(x / 2)
                res.append(int(x / 2))
            else:
                if x not in dic:
                    dic[x] = 1
                else:
                    dic[x] += 1
        if dic:
            return []
        return res