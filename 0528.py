class Bitset:

    def __init__(self, size: int):
        self.li = [0] * size
        self.n = size
        self.c = 0
        self.fl = False

    def fix(self, idx: int) -> None:
        if not self.fl:
            if self.li[idx] == 0:
                self.c += 1
            self.li[idx] = 1
        else:
            if self.li[idx] == 1:
                self.c += 1
            self.li[idx] = 0

    def unfix(self, idx: int) -> None:
        if not self.fl:
            if self.li[idx] == 1:
                self.c -= 1
            self.li[idx] = 0
        else:
            if self.li[idx] == 0:
                self.c -= 1
            self.li[idx] = 1

    def flip(self) -> None:
        if self.fl:
            self.fl = False
        else:
            self.fl = True
        self.c = self.n - self.c

    def all(self) -> bool:
        if self.c == self.n:
            return True
        else:
            return False

    def one(self) -> bool:
        if self.c > 0:
            return True
        else:
            return False

    def count(self) -> int:
        return self.c

    def toString(self) -> str:
        li = [""] * self.n
        for i in range(self.n):
            neo = self.li[i]
            add = ""
            if self.fl == True:
                if neo == 0:
                    add = "1"
                else:
                    add = "0"
            else:
                add = str(neo)
            li[i] = add
        return "".join(li)