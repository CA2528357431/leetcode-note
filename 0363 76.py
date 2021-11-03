class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 滑动窗口法
        '''
        l = 0
        r = 0
        tar = {}
        for c in t:
            tar[c] = tar.get(c, 0) + 1
        cur = {s[0]: 1}
        res = None
        while r < len(s):
            judge = True
            for k, v in tar.items():
                if k in cur and v <= cur[k]:
                    pass
                else:
                    judge = False
                    break
            if judge:
                if not res or res[1] - res[0] > r - l:
                    res = [l, r]
                cur[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r == len(s):
                    break
                cur[s[r]] = cur.get(s[r], 0) + 1

        if not res:
            return ""
        else:
            return s[res[0]:res[1] + 1]
        '''


        # 优化判定
        l = 0
        r = 0
        tar = {}
        for c in t:
            tar[c] = tar.get(c, 0) + 1
        res = None

        judge = len(tar)
        # 我们只需要知道还有几种字母没到要求

        while r <= len(s):
            if judge == 0:
                if not res or res[1] - res[0] > r - l:
                    res = [l, r]
                # 更新res
                if s[l] in tar:
                    if tar[s[l]] == 0:
                        judge += 1
                    # 某字母从满足要求到不满足
                    tar[s[l]] += 1

                l += 1
            else:
                if r == len(s):
                    break
                # r到队尾且当前不可能满足要求

                if s[r] in tar:
                    tar[s[r]] -= 1
                    if tar[s[r]] == 0:
                        judge -= 1
                    # 某字母从不满足要求到满足
                r += 1
        if not res:
            return ""
        else:
            return s[res[0]:res[1]]