class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        li = text.split()
        for i in range(len(li)-2):
            if li[i]==first and li[i+1]==second:
                res.append(li[i+2])
        return res