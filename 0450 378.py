class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            x, y = 0, n - 1
            num = 0
            while x < n and y >= 0:
                if matrix[x][y] <= mid:
                    x += 1
                    num += y + 1
                else:
                    y -= 1

            return num

        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            # 设有一个数字l+1不在matrix中，也符合check=k
            # 则其必然大于正确结果l
            # 最后会归到l
            if check(mid) >= k:
                r = mid
            else:
                l = mid + 1

        return l
