class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        dic = [0] * (n + 1)
        for x, y in edges:
            dic[x] += 1
            dic[y] += 1

        for i in range(n + 1):
            if dic[i] == n - 1:
                return i