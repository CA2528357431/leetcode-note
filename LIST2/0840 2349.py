from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.dic1 = {}
        self.dic2 = {}

    def change(self, index: int, number: int) -> None:
        if index not in self.dic1:
            self.dic1[index] = number
            if number not in self.dic2:
                self.dic2[number] = SortedList()
            self.dic2[number].add(index)
        else:
            oldnum = self.dic1[index]

            self.dic1[index] = number

            if number not in self.dic2:
                self.dic2[number] = SortedList()
            self.dic2[number].add(index)
            self.dic2[oldnum].remove(index)

    def find(self, number: int) -> int:
        if number not in self.dic2 or len(self.dic2[number]) == 0:
            return -1
        else:
            return self.dic2[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)