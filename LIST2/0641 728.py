class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def do(num):
            ori=num
            while num:
                a=num%10
                if a==0 or ori%a!=0:
                    return False
                num//=10
            return True
        return [x for x in range(left,right+1) if do(x)]