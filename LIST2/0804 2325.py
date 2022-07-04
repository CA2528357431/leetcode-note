class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        i = 0
        dic = {}
        dic[" "] = " "
        for c in key:
            if c in dic:
                continue
            dic[c] = chr(i + ord("a"))
            i += 1

        li = [dic[x] for x in message]
        return "".join(li)