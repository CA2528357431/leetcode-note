class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start =0
        res = 0
        li = set()
        for i in range(len(s)):
            while s[i] in li:
                li.remove(s[start])
                start+=1
            li.add(s[i])

            res = max(res,len(li))
        return res


    # 滑动窗口法
    # 检验重复用set