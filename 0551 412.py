class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[str(x) for x in range(1,n+1)]
        for x in range(1,n+1):
            if x%15==0:
                res[x-1]="FizzBuzz"
            elif x%3==0:
                res[x-1]="Fizz"
            elif x%5==0:
                res[x-1]="Buzz"
        return res