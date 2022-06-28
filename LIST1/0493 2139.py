class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        def do(tar,dou):
            if dou>0:
                if tar>1:
                    if tar%2==0:
                        return do(tar//2,dou-1)+1
                    else:
                        return do(tar//2,dou-1)+2
                else:
                    return 0
            return tar-1
        return do(target,maxDoubles)