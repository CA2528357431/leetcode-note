class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        def find(c):
            i = s.find(c)
            j = s.find(c,i+1)
            return j-i-1
        for i in range(26):
            c = chr(i+ord("a"))
            if c not in s:
                continue
            x = find(c)
            if x==distance[i]:
                continue
            else:
                return False
        return True