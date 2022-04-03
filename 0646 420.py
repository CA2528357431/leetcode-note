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
            change1 = 3 - categories
            change2 = 6 - n
            return max(change1, change2)
        elif n <= 20:
            change1 = 3 - categories
            change2 = 0
            cur = 1
            for i in range(1, n):
                if password[i - 1] == password[i]:
                    cur += 1
                else:
                    change2 += cur // 3
                    cur = 1
            change2 += cur // 3
            return max(change1, change2)
        else:
            change1 = n - 20
            change2 = 0
            sth = 0
            cur = 1
            for i in range(1, n):
                if password[i - 1] == password[i]:
                    cur += 1
                else:
                    if change1 > 0 and cur >= 3:
                        if cur % 3 == 0:
                            change1 -= 1
                            change2 -= 1
                        elif cur % 3 == 1:
                            sth += 1

                    change2 += cur // 3
                    cur = 1
            if change1 > 0 and cur >= 3:
                if cur % 3 == 0:
                    change1 -= 1
                    change2 -= 1
                elif cur % 3 == 1:
                    sth += 1
            change2 += cur // 3

            use2 = min(change2, sth, change1 // 2)
            change2 -= use2
            change1 -= use2 * 2

            use3 = min(change2, change1 // 3)
            change2 -= use3
            change1 -= use3 * 3
            return (n - 20) + max(change2, 3 - categories)