class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:

        # 堆排序
        '''
        if k==0:
            return []

        source = [-x for x in arr[:k]]
        heapq.heapify(source)
        for i in range(k,len(arr)):
            if arr[i]<-source[0]:
                heapq.heapreplace(source,-arr[i])
        for i in range(k):
            source[i] = -source[i]

        return source
        '''

        '''
        heapq.heapify(arr)
        res = [0]*k
        for x in range(k):
            res[x] = heapq.heappop(arr)
        return res   
        '''


        # 快排思路
        def quick(l, r):
            i = l
            j = r
            x = arr[l]
            while i < j:
                while i < j and arr[j] >= x:
                    j -= 1
                arr[i] = arr[j]

                while i < j and arr[i] <= x:
                    i += 1
                arr[j] = arr[i]
            arr[i] = x
            return i
        def sort(l,r):
            if l>=r:
                return
            mid = quick(l,r)
            if mid>k-1:
                sort(l,mid-1)
            elif mid<k-1:
                sort(mid+1,r)
            else:
                return
        sort(0,len(arr)-1)
        return arr[0:k]

