class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for s in operations:
            if s[1]=="+":
                res+=1
            elif s[1]=="-":
                res-=1
        return res