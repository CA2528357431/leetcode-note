class DetectSquares:

    def __init__(self):
        self.dic = {}

    def add(self, point: List[int]) -> None:
        neo = (point[0], point[1])
        if neo in self.dic:
            self.dic[neo] += 1
        else:
            self.dic[neo] = 1

    def count(self, point: List[int]) -> int:
        res = 0

        for key, value in self.dic.items():
            a, b, c, d = 0, 0, 0, 0
            num = value
            if key[0] == point[0]:
                length = abs(key[1] - point[1])

                if length > 0:
                    if (key[0] + length, key[1]) in self.dic and (point[0] + length, point[1]) in self.dic:
                        a = num * self.dic[(key[0] + length, key[1])] * self.dic[(point[0] + length, point[1])]
                    if (key[0] - length, key[1]) in self.dic and (point[0] - length, point[1]) in self.dic:
                        b = num * self.dic[(key[0] - length, key[1])] * self.dic[(point[0] - length, point[1])]

            if key[1] == point[1]:
                length = abs(key[0] - point[0])
                if length > 0:
                    if (key[0], key[1] + length) in self.dic and (point[0], point[1] + length) in self.dic:
                        c = num * self.dic[(key[0], key[1] + length)] * self.dic[(point[0], point[1] + length)]
                    if (key[0], key[1] - length) in self.dic and (point[0], point[1] - length) in self.dic:
                        d = num * self.dic[(key[0], key[1] - length)] * self.dic[(point[0], point[1] - length)]

            res += (a + b + c + d)

        return int(res / 2)

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)