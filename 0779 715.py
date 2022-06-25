from sortedcontainers import SortedDict


class RangeModule:

    def __init__(self):
        self.intervals = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x != 0:
            start = x - 1
            if itvs_.values()[start] >= right:
                return
            if itvs_.values()[start] >= left:
                left = itvs_.keys()[start]
                itvs_.popitem(start)
                x -= 1

        while x < len(itvs_) and itvs_.keys()[x] <= right:
            right = max(right, itvs_.values()[x])
            itvs_.popitem(x)

        itvs_[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x == 0:
            return False

        return right <= itvs_.values()[x - 1]

    def removeRange(self, left: int, right: int) -> None:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x != 0:
            start = x - 1
            if (ri := itvs_.values()[start]) >= right:
                if (li := itvs_.keys()[start]) == left:
                    itvs_.popitem(start)
                else:
                    itvs_[li] = left
                if right != ri:
                    itvs_[right] = ri
                return
            elif ri > left:
                itvs_[itvs_.keys()[start]] = left

        while x < len(itvs_) and itvs_.keys()[x] < right:
            if itvs_.values()[x] <= right:
                itvs_.popitem(x)
            else:
                itvs_[right] = itvs_.values()[x]
                itvs_.popitem(x)
                break
