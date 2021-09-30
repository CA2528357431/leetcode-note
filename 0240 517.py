class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        '''
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        ave = total // n

        times = 0

        passage = [0] * n
        for i in range(1, n):
            passage[i] = machines[i - 1] + passage[i - 1]
        for i in range(n):
            tol = max(i * ave - passage[i], 0)
            tor = max((n - i - 1) * ave - (total - passage[i] - machines[i]), 0)
            times = max(tol + tor, times)
        return times
        '''

        # 优化内存
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        ave = total // n

        times = 0
        passage = 0

        for i in range(n):
            tol = max(i * ave - passage, 0)
            tor = max((n - i - 1) * ave - (total - passage - machines[i]), 0)
            # 向左向右输送的个数
            times = max(tol + tor, times)
            passage += machines[i]

        return times

    # https://leetcode-cn.com/problems/super-washing-machines/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-mzqia/
