class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        dic = {}
        stack = []
        for i in range(m-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            stack.append(nums2[i])
            if len(stack)>=2:
                dic[nums2[i]] = stack[-2]
        res = []
        for x in nums1:
            if x in dic:
                res.append(dic[x])
            else:
                res.append(-1)
        return res

    # 单调栈
    # https://leetcode-cn.com/problems/next-greater-element-i/solution/xia-yi-ge-geng-da-yuan-su-i-by-leetcode-bfcoj/