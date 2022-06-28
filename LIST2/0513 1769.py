class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        n = len(boxes)
        s1 = [0] * n
        s2 = [0] * n

        num = 0
        if boxes[0] == "1":
            num = 1
        for i in range(1, n):
            s1[i] = s1[i - 1] + num
            if boxes[i] == "1":
                num += 1

        num = 0
        if boxes[n - 1] == "1":
            num = 1
        for i in range(n - 2, -1, -1):
            s2[i] = s2[i + 1] + num
            if boxes[i] == "1":
                num += 1

        for i in range(n):
            s1[i] += s2[i]
        return s1