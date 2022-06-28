class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.dic = {}
        for i in range(len(arr)):
            n = arr[i]
            if n not in self.dic:
                self.dic[n] = []
            self.dic[n].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.dic:
            return 0
        cur = self.dic[value]
        if left > cur[-1] or right < cur[0]:
            return 0

        cur = self.dic[value]
        res = 0

        l = 0
        r = len(cur) - 1

        while l < r:
            mid = (l + r) // 2
            if cur[mid] < left:
                l = mid + 1
            else:
                r = mid
        ll = l

        l = 0
        r = len(cur) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if right < cur[mid]:
                r = mid - 1
            else:
                l = mid
        rr = l

        return rr - ll + 1