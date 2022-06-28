class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        res = 0
        n = len(properties)
        properties.sort(key=lambda x: (-x[0]))

        de = -1
        neode = properties[0][1]
        for i in range(1, n):
            a, d = properties[i]
            prea, pred = properties[i - 1]
            if a == prea:
                if d < de:
                    res += 1
                neode = max(neode, d)
            else:
                de = max(de, neode)
                neode = d
                if d < de:
                    res += 1

        return res