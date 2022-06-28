# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        # (rand_X() - 1) × Y + rand_Y() ==> 可以等概率的生成[1, X * Y]范围的随机数
        # https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/cong-zui-ji-chu-de-jiang-qi-ru-he-zuo-dao-jun-yun-/

        '''
        while True:
            a1 = rand7()
            a2 = rand7()
            res = (a1-1)*7+a2
            # 1-49
            if res<=40:
                # return (res-1)//4+1
                return res%10+1
        '''

        while True:
            a1 = rand7()
            a2 = rand7()
            res = (a1 - 1) * 7 + a2
            # 1-49
            if res <= 40:
                # return (res-1)//4+1
                return res % 10 + 1

            # 抛弃9个太多
            a3 = rand7()
            res = (res - 1) * 7 + a3
            # 1-63
            if res <= 60:
                return res % 10 + 1

            # 抛弃三个。。优化
            a4 = rand7()
            res = (res - 1) * 7 + a4
            # 1-21
            if res <= 20:
                return res % 10 + 1
            # 只抛弃一个，行吧

