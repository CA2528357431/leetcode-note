class Solution:
    def minimumTime(self, s: str) -> int:
        '''
        n = len(s)

        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            c = s[i - 1]
            if c == "1":
                pre[i] = pre[i - 1] + 1
            else:
                pre[i] = pre[i - 1]

        b = 0
        res = n

        for i in range(n):
            a = 2 * pre[i + 1] - i
            b = min(b, i - 2 * pre[i])

            res = min(n - 1 + b + a, res)
        return res
        '''


        # 滚动优化
        n = len(s)

        res = n
        # 最坏就是全删除

        pre = 0
        for i in range(n):
            b = min(b, i - 2 * pre)
            if s[i]=="1":
                pre += 1
            a = 2 * pre - i
            res = min(n - 1 + b + a, res)
        return res