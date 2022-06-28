import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        res = 0
        heap = []
        i = 0
        while i<len(apples):
            while heap and heap[0][0]<=i:
                heapq.heappop(heap)
            if apples[i]:
                heapq.heappush(heap,[i+days[i],apples[i]])
            if heap:
                res+=1
                heap[0][1]-=1
                if heap[0][1]==0:
                    heapq.heappop(heap)
            i+=1
        while heap:
            while heap and heap[0][0]<=i:
                heapq.heappop(heap)
            if not heap:
                break
            buck = heapq.heappop(heap)
            if buck[1]+i<=buck[0]:
                i = buck[1]+i
                res+=buck[1]
            else:
                res+=buck[0]-i
                i = buck[0]
        return res
