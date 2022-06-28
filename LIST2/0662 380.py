import random
class RandomizedSet:

    def __init__(self):
        self.li = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.dic[val] = len(self.li)
            self.li.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            i = self.dic[val]
            neo = self.li[-1]
            self.li[i] = self.li[-1]
            self.li.pop()
            self.dic[neo] = i
            self.dic.pop(val)
            return True
            # 交换位置删除

        else:
            return False

    def getRandom(self) -> int:
        x = random.choice(self.li)
        # 内置随机选择
        return x

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()