class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False

        dic1 = {}

        dic2 = {}

        for x in s1:
            if x in dic1:
                dic1[x] += 1
            else:
                dic1[x] = 1
        for y in range(len(s1) - 1):
            if s2[y] in dic2:
                dic2[s2[y]] += 1
            else:
                dic2[s2[y]] = 1

        i = 0

        while i <= len(s2) - len(s1):

            if s2[i + len(s1) - 1] in dic2:
                dic2[s2[i + len(s1) - 1]] += 1
            else:
                dic2[s2[i + len(s1) - 1]] = 1

            if dic2 == dic1:
                return True
            else:
                dic2[s2[i]] -= 1
                if dic2[s2[i]] == 0:
                    dic2.pop(s2[i])
                i += 1

        return False

# 滑动的 +1、-1过程问题：
# -1问题无所谓，但当i到最后时，i + len(s1) 超过了index范围
# 解决方法是拆分+1，将其放到下一次循环开始
# 此题用dic不用list是因为不需要顺序
# 用dic不用set是因为s1可重复
# 注意dic[x]=0是应直接pop除去
