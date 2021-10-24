class Solution:
    def shoppingOffers(self, price, special, needs) -> int:
        real = []
        n = len(price)
        for s in special:
            su = 0
            for i in range(n):
                su += price[i] * s[i]
            if s[-1] < su:
                real.append(s.copy())

        # 就是组合问题
        # 以 礼包、单品 为主键遍历

        total = 99999999

        def do(ip, cost, cur):
            if ip == len(real):
                nonlocal total
                for i in range(n):
                    cost += (needs[i] - cur[i]) * price[i]
                total = min(total, cost)
                return

            do(ip + 1, cost, cur.copy())
            sp = real[ip]
            while True:
                judge = True
                for i in range(n):

                    cur[i] += sp[i]
                    if cur[i] > needs[i]:
                        judge = False
                        break

                if not judge:
                    break
                cost += sp[-1]
                do(ip + 1, cost, cur.copy())

        do(0, 0, [0] * n)
        return total