class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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