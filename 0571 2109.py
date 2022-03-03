class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        li=[]
        pre=0
        for n in spaces:
            li.append(s[pre:n])
            pre=n
        li.append(s[pre:])
        return " ".join(li)