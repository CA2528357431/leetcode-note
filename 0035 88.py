class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        '''
        if n == 0:
            return
        nums1[m] = nums2.pop()

        for i in range(0, m)[::-1]:
            if nums1[i] > nums1[i + 1]:
                nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]
            else:
                break

        self.merge(nums1, m + 1, nums2, n - 1)
        '''

        # 双指针

        '''
        if n == 0:
            return
        neo = []
        p = 0
        q = 0
        while p<m and q<n:
            if nums1[p]<nums2[q]:
                neo.append(nums1[p])
                p+=1
            else:
                neo.append(nums2[q])
                q+=1
        neo.extend(nums1[p:m])
        neo.extend(nums2[q:n])
        nums1[:] = neo
        '''

        # 或许可以节约空间


        if n == 0:
            return
        p = m-1
        q = n-1
        i = m+n-1
        while p>=0 and q>=0:
            if nums1[p]<nums2[q]:
                nums1[i] = nums2[q]
                q-=1
            else:
                nums1[i] = nums1[p]
                p-=1
            i-=1
        if q>=0:
            for x in range(q+1):
                nums1[x] = nums2[x]
