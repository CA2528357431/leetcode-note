class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        total = len(nums1) + len(nums2)
        p1 = 0
        p2 = 0
        cur = None
        la = None
        while p1 + p2 < total // 2 + 1:
            if p1 == 0 and p2 > 0:
                la = nums2[p2 - 1]
            elif p1 > 0 and p2 == 0:
                la = nums1[p1 - 1]
            elif p1 > 0 and p2 > 0:
                la = max(nums1[p1 - 1], nums2[p2 - 1])

            if p2 == len(nums2) :
                cur = nums1[p1]
                p1 += 1
            elif p1 == len(nums1):
                cur = nums2[p2]
                p2 += 1
            elif (nums1[p1] < nums2[p2]):
                cur = nums1[p1]
                p1 += 1
            elif nums1[p1] >= nums2[p2]:
                cur = nums2[p2]
                p2 += 1
        if total % 2 == 1:
            return cur
        else:
            return (cur + la) / 2
        '''
        l1 = len(nums1)
        l2 = len(nums2)

        def find(x, i1, i2):
            if i1 == l1:
                return nums2[i2 + x - 1]
            if i2 == l2:
                return nums1[i1 + x - 1]
            if x == 1:
                return min(nums1[i1], nums2[i2])

            delta = x // 2
            ii1 = min(l1 - 1, i1 + delta - 1)
            ii2 = min(l2 - 1, i2 + delta - 1)

            if nums1[ii1] < nums2[ii2]:
                return find(x - (ii1 - i1 + 1), ii1 + 1, i2)
            else:
                return find(x - (ii2 - i2 + 1), i1, ii2 + 1)

        if (l1 + l2) % 2 == 1:
            return find((l1 + l2) // 2 + 1, 0, 0)
        else:
            l = find((l1 + l2) // 2, 0, 0)
            r = find((l1 + l2) // 2 + 1, 0, 0)

            return (l + r) / 2