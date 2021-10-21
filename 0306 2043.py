class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance.copy()

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        n = len(self.accounts)
        if 1 <= account1 <= n and 1 <= account2 <= n:
            if self.accounts[account1 - 1] >= money:
                self.accounts[account1 - 1] -= money
                self.accounts[account2 - 1] += money
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        n = len(self.accounts)
        if 1 <= account <= n:
            self.accounts[account - 1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        n = len(self.accounts)
        if 1 <= account <= n:
            if self.accounts[account - 1] >= money:
                self.accounts[account - 1] -= money
                return True
            else:
                return False
        else:
            return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)