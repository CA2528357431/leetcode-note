num = 262144

def isPowerOfTwo(n: int) -> bool:
    judge = (n & (n - 1)) == 0
    print(judge)

isPowerOfTwo(num)