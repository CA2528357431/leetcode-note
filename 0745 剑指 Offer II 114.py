class Solution:
    def alienOrder(self, words) -> str:
        dic = {}
        for w in words:
            for c in w:
                if c not in dic:
                    dic[c] = set()


        n = len(words)
        for i in range(n):
            w1 = words[i]
            for j in range(i+1,n):
                w2 = words[j]
                ind = 0
                while ind<len(w1) and ind<len(w2):
                    c1 = w1[ind]
                    c2 = w2[ind]
                    if c1!=c2:
                        for c in dic:
                            if c1 == c or c1 in dic[c]:
                                dic[c].add(c2)
                        break
                    else:
                        ind+=1
                if ind==len(w2) and len(w1)>len(w2):
                    return ""

        li = []
        while dic:
            ch = ""
            for c in dic:
                if len(dic[c])==0:
                    li.append(c)
                    ch = c
                    break
            if not ch:
                return ""
            dic.pop(ch)
            for cc in dic:
                if c in dic[cc]:
                    dic[cc].remove(c)


        return "".join(li)[::-1]