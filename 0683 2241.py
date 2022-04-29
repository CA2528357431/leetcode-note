class ATM:

    def __init__(self):
        self.li = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.li[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        dol = [500, 200, 100, 50, 20]
        res = [0] * 5
        for i in range(5):
            num = min(amount // dol[i], self.li[4 - i])
            amount -= num * dol[i]
            res[i] += num
        if amount != 0:
            return [-1]
        else:
            res.reverse()
            for i in range(5):
                self.li[i] -= res[i]

            return res

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)