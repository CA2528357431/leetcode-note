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


        heapq.heapify(arr)
        res = [0]*k
        for x in range(k):
            res[x] = heapq.heappop(arr)
        return res   


