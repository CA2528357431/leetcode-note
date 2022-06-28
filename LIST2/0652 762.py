class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def get(x):
            cnt = 0
            for i in range(20):
                ch = 1 << i
                if ch & x:
                    cnt += 1
            return cnt

        li = {2, 3, 5, 7, 11, 13, 17, 19}
        cnt = 0

        for x in range(left, right + 1):
            # if get(x) in li:
            # 用内置的
            if x.bit_count() in li:
                cnt += 1
        return cnt
