class MyCalendarTwo:

    def __init__(self):
        self.dic = SortedList()

    def book(self, start: int, end: int) -> int:
        self.dic[start] = self.dic.get(start, 0) + 1
        self.dic[end] = self.dic.get(end, 0) - 1

        cur = 0
        # ks = list(self.dic.keys())
        # ks.sort()

        for k in self.dic:
            v = self.dic[k]
            cur += v
            if cur>=3:
                self.dic[start] -= 1
                self.dic[end] += 1
                return False

        return True