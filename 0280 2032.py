class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        ma = s1 | s2 | s3

        for x in ma:
            i = 0
            if x in s1:
                i += 1
            if x in s2:
                i += 1
            if x in s3:
                i += 1
            if i >= 2:
                res.append(x)
        return res