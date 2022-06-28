class Solution:
    def originalDigits(self, s: str) -> str:
        c = {}
        for ch in "abcdefghijklmnopqrstuvwxyz":
            c[ch] = 0
        for ch in s:
            c[ch] += 1

        cnt = [0] * 10
        cnt[0] = c["z"]
        cnt[2] = c["w"]
        cnt[4] = c["u"]
        cnt[6] = c["x"]
        cnt[8] = c["g"]

        cnt[3] = c["h"] - cnt[8]
        cnt[5] = c["f"] - cnt[4]
        cnt[7] = c["s"] - cnt[6]

        cnt[1] = c["o"] - cnt[0] - cnt[2] - cnt[4]

        cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]

        li = []
        for x in range(10):
            li.append(str(x) * cnt[x])

        return "".join(li)