class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        do = ["","/",""]
        for x in range(2,n+1):
            for y in range(1,x):
                if gcd(x,y)==1:
                    do[0] = str(y)
                    do[2] = str(x)
                    res.append("".join(do))
        return res