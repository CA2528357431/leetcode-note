class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(li):
            while True:
                for i in range(len(li) - 2):
                    if li[i] == li[i + 1] and li[i + 1] == li[i + 2]:
                        cur = li[i]
                        while i < len(li) and li[i] == cur:
                            li.pop(i)
                        break
                else:
                    return

        bds = [list(board)]
        res = 0

        hds = [{'R': 0, 'Y': 0, 'B': 0, 'G': 0, 'W': 0}]
        for c in hand:
            hds[0][c] += 1

        used = {board}

        while bds:
            neobds = []
            neohds = []

            for i in range(len(bds)):
                bd = bds[i]
                hd = hds[i]

                if not bd:
                    return res

                for color in hd:
                    if hd[color] == 0:
                        continue
                    for i in range(len(bd)):
                        nb = bd.copy()
                        nb.insert(i, color)

                        clean(nb)
                        if "".join(nb) in used:
                            continue
                        used.add("".join(nb))

                        neobds.append(nb)

                        nbdic = hd.copy()
                        nbdic[color] -= 1
                        neohds.append(nbdic)
            bds = neobds
            hds = neohds

            res += 1

        return -1
