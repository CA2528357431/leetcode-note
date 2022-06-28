class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        s1 = set()
        s2 = set(list(target))
        for w in stickers:
            s1 = s1 | set(list(w))
        if len(s2 - s1) != 0:
            return -1

        def index(c):
            return ord(c) - ord("a")

        def getli(word):
            tar = [0] * 26
            for c in word:
                tar[index(c)] += 1
            return tar

        def getkey(li):
            s = 0
            for i in range(26):
                s = s * 26 + li[i]
            return s

        def minus(tar, use):
            neo = tar.copy()
            for i in range(26):
                neo[i] = max(tar[i] - use[i], 0)
            return neo

        stickerlis = [getli(w) for w in stickers]

        cur = [getli(target)]
        s = {getkey(cur[0])}
        step = 0
        while True:
            if 0 in s:
                return step
            nxt = []
            for c in cur:
                for li in stickerlis:
                    neo = minus(c, li)
                    k = getkey(neo)
                    if k not in s:
                        s.add(k)
                        nxt.append(neo)

            cur = nxt
            step += 1


