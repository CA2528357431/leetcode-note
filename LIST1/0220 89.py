class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0,1]
        f = self.grayCode(n-1)
        l = f.copy()
        l.reverse()
        for i in range(len(l)):
            l[i]+=2**(n-1)
        return f+l

    # 简单递归
    # https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/