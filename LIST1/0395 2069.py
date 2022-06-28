class Robot:

    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.width = width
        self.height = height

    def move(self, num: int) -> None:

        num = num % (2 * self.width + 2 * self.height - 4)
        # 优化距离

        if self.x == 0 and self.y == 0:
            self.dir = 3
        # 只要在 0，0 点，则除了从未move的状态，方向必然向下
        # 若想拥有普遍性，必须在move到 0，0 时调整朝向
        # 比如2*2的矩阵，move(4), 那么此时方向应该时南，但若不调整，头部朝向为右，错误

        while True:
            if self.dir == 0 and self.x + num >= self.width:
                num = num - (self.width - 1 - self.x)
                self.x = self.width - 1
                self.dir = 1
            elif self.dir == 1 and self.y + num >= self.height:
                num = num - (self.height - 1 - self.y)
                self.y = self.height - 1
                self.dir = 2
            elif self.dir == 2 and self.x - num < 0:
                num = num - (self.x - 0)
                self.x = 0
                self.dir = 3
            elif self.dir == 3 and self.y - num < 0:
                num = num - (self.y - 0)
                self.y = 0
                self.dir = 0
            else:
                break
        if self.dir == 0:
            self.x += num
        elif self.dir == 1:
            self.y += num
        elif self.dir == 2:
            self.x -= num
        elif self.dir == 3:
            self.y -= num

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.dir == 0:
            return "East"
        elif self.dir == 1:
            return "North"
        elif self.dir == 2:
            return "West"
        elif self.dir == 3:
            return "South"