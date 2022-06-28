class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a = a % 1337
        n = len(b)
        res = 1
        for i in range(n):
            res = res ** 10
            app = (a ** b[i]) % 1337
            res = res * app % 1337

        return res

    # (a*b)%c=((a%c)*(b%c))%c
    # https://leetcode-cn.com/problems/super-pow/solution/you-qian-ru-shen-kuai-su-mi-suan-fa-xiang-jie-by-l/