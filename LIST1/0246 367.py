class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        cur = 1
        while cur * cur < num:
            cur += 1
        return cur * cur == num
        '''

        # 牛顿迭代
        if num == 1:
            return True
        cur = num // 2
        while cur * cur > num:
            cur = (cur + num // cur) // 2
        return cur * cur == num
