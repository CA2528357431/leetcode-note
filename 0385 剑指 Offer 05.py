class Solution:
    def replaceSpace(self, s: str) -> str:
        li = list(s)
        for i in range(len(s)):
            if li[i]==" ":
                li[i] = "%20"
        return "".join(li)