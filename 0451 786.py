# 堆排序
'''
class num:
    def __init__(self, arr, i, j):
        self.i = i
        self.j = j
        self.arr = arr

    def __lt__(self, other):
        return self.arr[self.i] * other.arr[other.j] < self.arr[self.j] * other.arr[other.i]


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        cur = None

        for i in range(1, n):
            heapq.heappush(heap, num(arr, 0, i))

        for _ in range(k):
            cur = heappop(heap)
            if cur.i + 1 < cur.j:
                heapq.heappush(heap, num(arr, cur.i + 1, cur.j))

        return [arr[cur.i], arr[cur.j]]

'''

# 双指针
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l = 0
        r = 1
        n = len(arr)
        while l < r:
            mid = (l + r) / 2
            count = 0
            res = None

            i = 0
            # 分子指针
            for j in range(1, n):
                # 分母指针
                while arr[i] / arr[j] < mid:
                    if not res or res[0] / res[1] < arr[i] / arr[j]:
                        res = [arr[i], arr[j]]
                    i += 1
                # 如果 旧i/j<mid，则 新i/j<旧i/j<mid
                count += i
            # 统计过程复杂度为n

            if count == k:
                return res
            elif count < k:
                l = mid
            elif count > k:
                r = mid