class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pre = Node()
        self.length = 0
        self.tail = self.pre

    def getNode(self, index: int) -> int:
        cur = self.pre
        for _ in range(index + 1):
            cur = cur.next
        return cur

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1

        res = self.getNode(index)

        return res.value

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

        neo = Node(val)
        neo.next = self.pre.next
        self.pre.next = neo

        if self.length == 0:
            self.tail = neo

        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        neo = Node(val)

        self.tail.next = neo
        self.tail = neo

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if index <= 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index > self.length:
            pass

        else:
            neo = Node(val)
            head = self.getNode(index - 1)

            neo.next = head.next
            head.next = neo

            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index < 0 or index >= self.length:

            return
        elif index == 0:
            self.pre.next = self.pre.next.next
            if self.length == 1:
                self.tail = None
            self.length -= 1
        elif index == self.length - 1:
            neotail = self.getNode(self.length - 2)
            neotail.next = None
            self.tail = neotail
            self.length -= 1
        else:
            neo = self.getNode(index - 1)
            neo.next = neo.next.next
            self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)