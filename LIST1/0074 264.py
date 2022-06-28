import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        # 堆排序

        '''
        if n == 1:
            return 1
        used = {1}
        heap = [1]
        for _ in range(n-1):
            cur = heapq.heappop(heap)
            for x in (cur*2,cur*3,cur*5):
                if x not in used:
                    used.add(x)
                    heapq.heappush(heap,x)

        return  heapq.heappop(heap)
        '''
        # 事实上，我们并不需要对整个序列进行排序，需求仅仅是最小值
        # 因此，我们选取堆排序来加快速度


        # 动态规划

        if n == 1:
            return 1
        li = [1]*n
        p5 = 0
        p3 = 0
        p2 = 0

        for x in range(1,n):
            neo2 = li[p2]*2
            neo3 = li[p3]*3
            neo5 = li[p5]*5
            neo = min(neo2,neo3,neo5)
            if neo==neo5:
                p5+=1
            if neo==neo3:
                p3+=1
            if neo==neo2:
                p2+=1
            li[x] = neo
        return li[-1]