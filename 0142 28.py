class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def check(needle):
            res = [0]*len(needle)
            par = 1
            now = 0
            while par<len(needle):
                if needle[par]==needle[now]:
                    now += 1
                    res[par] = now
                    par += 1
                else:
                    if now>0:
                        now = res[now-1]
                    else:
                        par+=1
            return res
        ne = check(needle)
        s = 0
        l = 0
        while s<len(needle) and l<len(haystack):
            if needle[s]==haystack[l]:
                l+=1
                s+=1
            else:
                if s>0:
                    s = ne[s-1]
                else:
                    l+=1
        if s==len(needle):
            return l-s
        else:
            return-1