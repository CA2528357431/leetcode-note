class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)

    # 第i个灯泡，开关的次数为因数的个数
    # a是i的i因数，则i/a必然也是，成对出现
    # 因此亮灯———奇数个因数———有一个因数不成对————可完全平方
    # 因此即求1-n完全平方数的个数

    # https://leetcode-cn.com/problems/bulb-switcher/solution/deng-pao-kai-guan-by-leetcode-solution-rrgp/