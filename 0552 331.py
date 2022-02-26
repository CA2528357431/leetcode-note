class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder=="#":
            return True
        if preorder[0]=="#":
            return False
        li=preorder.split(",")
        cap=2
        for x in range(1,len(li)):
            if cap==0:
                return False
            cap-=1
            if li[x]!="#":
                cap+=2

        return cap==0