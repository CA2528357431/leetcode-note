class Solution:
    def minOperations(self, logs: List[str]) -> int:
        heap = 0
        for x in logs:
            if x=="../":
                heap-=1
                if heap<0:
                    heap = 0
            elif x=="./":
                pass
            else:
                heap+=1
        return heap