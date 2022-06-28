class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # https://leetcode-cn.com/problems/longest-duplicate-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode-0i9rd/
        def get(i):
            return ord(s[i]) - ord("a")

        # Rabin-Karp法
        def check(mid):
            n = len(s)

            # 防止冲突，两个哈希------居然真会冲突

            num1 = 0
            num2 = 0
            for i in range(mid):
                num1 = (num1 * 997 + get(i)) % 1000000009
                num2 = (num2 * 1997 + get(i)) % 1000000007

            used = {(num1, num2)}
            al1 = pow(997, mid - 1, 1000000009)
            al2 = pow(1997, mid - 1, 1000000007)

            for i in range(1, n - mid + 1):
                num1 = ((num1 - get(i - 1) * al1) * 997 + get(i + mid - 1)) % 1000000009
                num2 = ((num2 - get(i - 1) * al2) * 1997 + get(i + mid - 1)) % 1000000007
                if (num1, num2) in used:
                    return i
                used.add((num1, num2))
            return -1

        l = 1
        r = len(s) - 1
        start = -1
        while l < r:
            mid = l + (r - l + 1) // 2
            re = check(mid)
            if re >= 0:
                l = mid
                start = re
            else:
                r = mid - 1

        re = check(l)
        if re >= 0:
            start = re
        if start < 0:
            return ""

        return s[start:start + r]