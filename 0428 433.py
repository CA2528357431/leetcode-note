class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        n = len(start)
        used = set()
        law = set(bank)
        base = ["A", "T", "C", "G"]
        curs = [list(start)]
        for time in range(n):
            neo = []
            for cur in curs:
                for i in range(n):
                    for re in base:
                        if cur[i] == re:
                            continue
                        ccur = cur.copy()
                        ccur[i] = re
                        string = "".join(ccur)

                        if string not in bank or string in used:
                            continue

                        if string == end:
                            return time + 1
                        used.add(string)
                        neo.append(ccur)
            curs = neo
        return -1