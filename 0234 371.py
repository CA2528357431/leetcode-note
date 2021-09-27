class Solution:
    def getSum(self, a: int, b: int) -> int:
        toint = 2 ** 32
        pos = 0x7FFFFFFF


        # 本体没什么意义，理解这两行即可
        up = ((a & b) << 1) % toint
        car = (a ^ b) % toint

        # sth%int 是为了转变成32位整数
        # 正数%int<=pos 负数%int>pos

        if up & car == 0:
            res = up | car
            if res <= pos:
                return res
            else:
                return ~((res % (pos + 1)) ^ pos)

        else:
            return self.getSum(up, car)

        # https://leetcode-cn.com/problems/sum-of-two-integers/solution/liang-zheng-shu-zhi-he-by-leetcode-solut-c1s3/
