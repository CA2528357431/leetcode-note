class Solution:
    def change(self, amount: int, coins):


        '''
        res = [0] * (amount + 1)
        res[0] = 1
        for x in range(1, len(res)):
            for coin in coins:
                if x - coin >= 0:
                    res[x] += res[x - coin]
            print(res)
        '''

        res = [0] * (amount + 1)
        res[0] = 1
        for coin in coins:
            for x in range(1, len(res)):
                if x - coin >= 0:
                    res[x] += res[x - coin]
            print(res)

        return res[-1]


# 0098 377 排列
# '''中，遍历金额，求得的是排列

# 遍历coins 得到的是组合
# 每遍历一个coin，都代表该硬币可用

# [1，2，5] 遍历到2 代表只能用1、2

# https://leetcode-cn.com/problems/coin-change-2/solution/dai-ma-sui-xiang-lu-518-ling-qian-dui-hu-q7gm/