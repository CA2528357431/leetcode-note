class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # dp
        '''
        n = len(s)
        if n == 0: return 0
        dp = [0] * (n+1)
        res = 0
        for i in range(1,n):
            if s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i+1] = dp[i+1 - 2] + 2
                elif s[i - 1] == ")" and i-1 - dp[i+1 - 1] >= 0 and s[i-1 - dp[i+1 - 1]] == "(":
                    dp[i+1] = dp[i+1 - 1] + 2 + dp[i+1-1 - dp[i+1 - 1] - 1]
            res = max(dp[i+1],res)
        return res
        '''
        # https://leetcode-cn.com/problems/longest-valid-parentheses/solution/dong-tai-gui-hua-si-lu-xiang-jie-c-by-zhanganan042/

        '''
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i - stack[-1])
        return res
        '''
        # https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/


        # 计数器

        res = 0

        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            else:
                r += 1
                if l < r:
                    l = 0
                    r = 0
                elif l == r:
                    res = max(res, l * 2)

        l = 0
        r = 0
        for i in range(len(s))[::-1]:
            if s[i] == ")":
                r += 1
            else:
                l += 1
                if r < l:
                    l = 0
                    r = 0
                elif l == r:
                    res = max(res, l * 2)
        return res

        # https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/