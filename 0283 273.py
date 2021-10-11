class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        bitdic = ["", "Thousand", "Million", "Billion"]
        numdic = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        tendic = {
            1: "Ten",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        neodic = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        nums = []
        while num:
            nums.append(num % 1000)
            num = num // 1000

        cur = []

        def handle(n, i):
            if n == 0:
                return
            if n >= 100:
                h = n // 100
                cur.append(numdic[h])
                cur.append("Hundred")
                n = n % 100
            if n == 0:
                pass
            elif 10 <= n < 20:
                cur.append(neodic[n])
            elif 1 <= n < 10:
                cur.append(numdic[n])
            else:
                t = n // 10
                cur.append(tendic[t])
                if n % 10 != 0:
                    cur.append(numdic[n % 10])
            if i != 0:
                cur.append(bitdic[i])

        for i in range(len(nums) - 1, -1, -1):
            handle(nums[i], i)

        return " ".join(cur)