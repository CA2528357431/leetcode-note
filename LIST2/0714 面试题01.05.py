class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first)<len(second):
            first,second = second,first
        n1 = len(first)
        n2 = len(second)
        if n1-n2>1:
            return False
        elif n1==n2:
            cnt = 0
            for i in range(n1):
                if first[i]!=second[i]:
                    cnt+=1
                    if cnt>1:
                        return False
            return True
        else:
            cnt = 0
            j = 0
            for i in range(n1):
                if j==n2:
                    return True
                if first[i]==second[j]:
                    j+=1
                else:
                    cnt+=1
                    if cnt>1:
                        return False
            return True