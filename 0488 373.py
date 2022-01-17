class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l1 = len(nums1)
        l2 = len(nums2)

        def find(mid):
            num = 0
            a1 = 0
            a2 = l2 - 1
            while a1 < l1 and a2 >= 0:
                neo = nums1[a1] + nums2[a2]
                if neo > mid:
                    a2 -= 1
                else:
                    a1 += 1
                    num += a2 + 1
            return num

        l = nums1[0] + nums2[0]
        r = nums1[l1 - 1] + nums2[l2 - 1]
        while l < r:
            mid = (l + r) // 2
            re = find(mid)
            if re >= k:
                r = mid
            else:
                l = mid + 1

        limit = l
        res = []
        total = k
        # 先放小于
        for num1 in nums1:
            if num1 + nums2[0] > limit:
                break
            for num2 in nums2[:total]:
                if num1 + num2 < limit:
                    res.append([num1, num2])
                    total -= 1
                    if total == 0:
                        return res
        # 再找等于
        for num1 in nums1:
            if num1 + nums2[0] > limit:
                break
            for num2 in nums2:
                if num1 + num2 == limit:
                    res.append([num1, num2])
                    total -= 1
                    if total == 0:
                        return res
        return res

    # 参考升序矩阵