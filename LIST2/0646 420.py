class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        lower = 0
        upper = 0
        digit = 0
        for ch in password:
            if ch.islower():
                lower = 1
            elif ch.isupper():
                upper = 1
            elif ch.isdigit():
                digit = 1

        categories = lower + upper + digit

        if n < 6:
            cate = 3 - categories
            add = 6 - n
            return max(cate, add)
        elif n <= 20:
            cate = 3 - categories
            change = 0
            cur = 1
            for i in range(1, n):
                if password[i - 1] == password[i]:
                    cur += 1
                else:
                    change += cur // 3
                    cur = 1
            change += cur // 3
            return max(cate, change)
        else:
            dele = n - 20
            change = 0
            res0 = 0
            res1 = 0
            cur = 1
            for i in range(1, n):
                if password[i - 1] == password[i]:
                    cur += 1
                else:
                    if cur >= 3:
                        if cur % 3 == 0:
                            res0 += 1
                        elif cur % 3 == 1:
                            res1 += 1
                    change += cur // 3
                    cur = 1
            if cur >= 3:
                if cur % 3 == 0:
                    res0 += 1
                elif cur % 3 == 1:
                    res1 += 1
            change += cur // 3

            use1 = min(res0, dele)
            change -= use1
            dele -= use1

            use2 = min(res1, dele // 2)
            change -= use2
            dele -= use2 * 2

            use3 = dele // 3
            change -= use3
            dele -= use3 * 3

            cate = 3 - categories

            return (n - 20) + max(change, cate)
        # https://leetcode-cn.com/problems/strong-password-checker/solution/qiang-mi-ma-jian-yan-qi-by-leetcode-solu-4fqx/