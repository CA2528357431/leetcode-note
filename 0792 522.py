class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda x: -len(x))

        def find(a, b):
            if len(a) > len(b):
                return False
            i = 0
            for c in a:
                while i < len(b) and b[i] != c:
                    i += 1
                if i == len(b):
                    return False
                else:
                    i += 1
            return True

        n = len(strs)
        for i in range(n):
            judge = False
            for j in range(n):
                if i == j:
                    continue
                if find(strs[i], strs[j]):
                    judge = True
                    break
            if not judge:
                return len(strs[i])
        return -1
    # 为什么最长特殊序列一定是strs的元素，而非其子序列？
    # 如果某子序列是独一无二的，则其所属的字符串一定也是独一无二的
