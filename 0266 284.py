# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.cur = iterator
        self.have = self.cur.hasNext()
        self.nextitem = iterator.next()

        # 先保存当前位置的next、have，然后把iter后移
        # peek、have只返回next、have
        # next返回next还要后移iter，更新next、have

    def peek(self):
        return self.nextitem

    def next(self):
        ret = self.nextitem
        self.have = self.cur.hasNext()
        self.nextitem = self.cur.next()
        return ret

    def hasNext(self):
        return self.have

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].