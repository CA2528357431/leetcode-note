class Solution:
    def reorderSpaces(self, text: str) -> str:
        li = [x for x in text.split() if x]
        cnt = 0
        for c in text:
            if c==" ":
                cnt+=1
        if len(li)==1:
            return li[0]+" "*cnt
        a = cnt//(len(li)-1)
        b = cnt%(len(li)-1)
        s = (" "*a).join(li) + " "*b
        return s