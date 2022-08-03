class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        l12 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        l13 = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
        l23 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2

        li = [l12, l13, l23]
        li.sort()

        if li[-1] == 0:
            return False

        if li[0] + li[1] != li[2]:
            return False
        if li[0] != li[1]:
            return False

        if l23 == li[2]:
            p1, p3 = p3, p1
        elif l13 == li[2]:
            p2, p3 = p3, p2

        l14 = (p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2
        l24 = (p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2

        if l14 + l24 != li[2]:
            return False
        if l14 != l24:
            return False
        return True