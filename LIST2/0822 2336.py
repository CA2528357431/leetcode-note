from sortedcontainers import SortedDict


class SmallestInfiniteSet:

    def __init__(self):
        self.res = SortedDict()
        self.res[1] = 1000

    def popSmallest(self) -> int:
        k = self.res.keys()[0]
        v = self.res[k]
        if k == v:
            self.res.pop(k)
        else:
            self.res.pop(k)
            self.res[k + 1] = v

        return k

    def addBack(self, num: int) -> None:
        li = self.res.keys()

        if li[0] > num:
            k = li[0]
            v = self.res[k]
            if num + 1 == k:
                self.res.pop(k)
                self.res[num] = v
            else:
                self.res[num] = num
            return

        l = 0
        r = len(li) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if li[mid] <= num:
                l = mid
            else:
                r = mid - 1
        k = li[l]
        v = self.res[k]
        if num <= v:
            return
        elif num == v + 1:
            self.res[k] += 1
            if l == len(li) - 1:
                return
            kk = li[l + 1]
            vv = self.res[kk]
            if num + 1 == kk:
                self.res.pop(kk)
                self.res[k] = kk



        else:
            self.res[num] = num
            if l == len(li) - 1:
                return
            kk = li[l + 1]
            vv = self.res[kk]
            if num + 1 == kk:
                self.res.pop(kk)
                self.res[num] = kk

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)