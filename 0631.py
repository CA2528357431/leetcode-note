class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        d1 = list(s1-s2)
        d2 = list(s2-s1)
        return [d1,d2]