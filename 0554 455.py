class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        an = 0
        s.sort()
        g.sort()
        cookie_r = 0
        for x in g:
            while cookie_r < len(s):
                if s[cookie_r] >= x:
                    an += 1
                    cookie_r += 1
                    break
                cookie_r += 1

        return an
