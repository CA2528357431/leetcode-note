class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def cnt(num):
            t = 0
            for i in range(1,m+1):
                st = min(n,num//i)
                t+=st
            return t
        l = 1
        r = m*n
        while l!=r:
            mid = (l+r)//2
            res = cnt(mid)
            if res<k:
                l = mid+1
            else:
                r = mid
        return l
    # 涉及元素极多做不到遍历的二维矩阵里的第K小都可以用二分猜答案的套路，转化为“给定一个数，求矩阵中有多少个数比这个数小”，进而实现二分查找
    # https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/solution/dong-tu-yan-shi-by-xiaohu9527-3k7s/