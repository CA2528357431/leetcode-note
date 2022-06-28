class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        def get(w, l):
            com = gcd(w, l)
            return (w // com, l // com)

        def c2(n):
            return n * (n - 1) // 2

        dic = {}
        for w, l in rectangles:
            neo = get(w, l)
            if neo not in dic:
                dic[neo] = 0
            dic[neo] += 1

        res = 0
        for k in dic:
            v = dic[k]
            res += c2(v)

        return res

