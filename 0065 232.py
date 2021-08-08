class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tail = []
        self.head = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.tail.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.head:
            return self.head.pop()
        else:
            while self.tail:
                self.head.append(self.tail.pop())
            return self.head.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.head:
            return self.head[-1]
        else:
            return self.tail[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.tail and not self.head:
            return True
        else:
            return False


# 为了高效的删除头元素,删除的时候要把tail转置的放入head,使头元素可以方便的删除
# 如果head空,头元素在tail[0]