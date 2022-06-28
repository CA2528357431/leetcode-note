class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        li = sentence.split()
        for i in range(len(li)):
            w = li[i]
            if w[0] == "$" and w[1:].isdigit():
                num = int(w[1:])
                num = num * (100 - discount) / 100
                neo = "$" + ("%.2f" % num)
                li[i] = neo
        return " ".join(li)
