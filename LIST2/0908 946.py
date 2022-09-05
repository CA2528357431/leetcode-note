class Solution:
    def validateStackSequences(self, push: List[int], pop: List[int]) -> bool:
        n = len(push)
        heap = []
        i = 0
        for p in pop:
            while (not heap or p != heap[-1]) and i < n:
                heap.append(push[i])
                i += 1
            if p != heap[-1]:
                return False
            else:
                heap.pop()

        return True