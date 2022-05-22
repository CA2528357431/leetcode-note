class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        def cmparechar(a,b):
            if dic[a]<dic[b]:
                return -1
            elif dic[a]>dic[b]:
                return 1
            else:
                return 0
        def cmpareword(a,b):
            for i in range(min(len(a),len(b))):
                j = cmparechar(a[i],b[i])
                if j!=0:
                    return j
            if len(a)<len(b):
                return -1
            elif len(a)>len(b):
                return 1
            return 0

        for i in range(len(words)-1):
            if cmpareword(words[i],words[i+1])==1:
                return False
        return True