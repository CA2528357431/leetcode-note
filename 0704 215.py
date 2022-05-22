class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # 基于quicksort
        '''
        def do(l,r):

            if l==r:
                return nums[l]
            stand = nums[l]
            j = l+1
            for i in range(l+1,r+1):
                if nums[i]>stand:
                    nums[j],nums[i] = nums[i],nums[j]
                    j+=1
            j-=1
            nums[j], nums[l] = nums[l], nums[j]
            if j==k-1:
                return stand
            elif j<k-1:
                return do(j+1,r)
            else:
                return do(l,j-1)
        return do(0,len(nums)-1)
        '''
        heap = []
        for x in nums:
            heapq.heappush(heap,-x)
        for i in range(k-1):
            heapq.heappop(heap)
        return -heap[0]