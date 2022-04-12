class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def get(c):
            return ord(c)-ord("A")+1
        li = []
        cur = 0
        for c in columnTitle:
            cur = cur*26+get(c)
        return cur