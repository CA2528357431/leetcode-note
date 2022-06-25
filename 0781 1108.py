class Solution:
    def defangIPaddr(self, address: str) -> str:
        li = list(address)
        for i in range(len(li)):
            if li[i] == ".":
                li[i] = "[.]"
        return "".join(li)
