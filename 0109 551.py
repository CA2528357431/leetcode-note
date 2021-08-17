class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for x in s:
            if x=="A":
                l = 0

                a+=1
                if a>=2:
                    return False
            elif x=="L":
                l+=1
                if l>=3:
                    return False
            elif x=="P":
                l=0
        return True