class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        n = len(stones)
        dic = {0: 0, 1: 0, 2: 0}
        res = 0
        j1 = True
        j2 = True

        num = 1

        for i in range(n):
            dic[stones[i] % 3] += 1
        copy = dic.copy()

        # 只看每个数字对3的余数即可
        # 余数0视作切换取石子的人，所以不需要考虑对和的影响


        # 分别考虑先手拿1、2
        # 1 fisrt
        if dic[0] % 2 == 1:
            # 如果0有奇数个，相当于先手拿两个
            if dic[1] >= 2:
                dic[1] -= 2
                res = 2

                if dic[2] >= dic[1]:
                    j1 = False
                else:
                    j1 = True
            else:
                j1 = False
        else:
            # 如果0有偶数个，相当于先手只拿一个
            if dic[1] >= 1:
                dic[1] -= 1
                res = 1

                if dic[1] >= dic[2]:
                    j1 = False
                else:
                    j1 = True
            else:
                j1 = False
        # 2 fisrt
        dic = copy
        if dic[0] % 2 == 1:
            if dic[2] >= 2:
                dic[2] -= 2
                res = 1

                if dic[1] >= dic[2]:
                    j2 = False
                else:
                    j2 = True
            else:
                j2 = False
        else:
            if dic[2] >= 1:
                dic[2] -= 1
                res = 2
                if dic[2] >= dic[1]:
                    j2 = False
                else:
                    j2 = True
            else:
                j2 = False

        return j1 or j2


