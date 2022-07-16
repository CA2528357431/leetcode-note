class WordFilter:

    def __init__(self, words: List[str]):
        pre = {}
        post = {}
        n = len(words)
        for i in range(n):
            w = words[i]
            cur = pre
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur[""] = i
        for i in range(n):
            w = words[i][::-1]
            cur = post
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur[""] = i

        self.pre = pre
        self.post = post

    def f(self, pref: str, suff: str) -> int:
        pre = set()
        post = set()

        cur = self.pre
        for c in pref:
            if c not in cur:
                return -1
            cur = cur[c]
        li = [cur]
        while li:
            nxt = []
            for node in li:
                for k, v in node.items():
                    if k == "":
                        pre.add(v)
                    else:
                        nxt.append(v)
            li = nxt

        cur = self.post
        for c in suff[::-1]:
            if c not in cur:
                return -1
            cur = cur[c]
        li = [cur]
        while li:
            nxt = []
            for node in li:
                for k, v in node.items():
                    if k == "":
                        post.add(v)
                    else:
                        nxt.append(v)
            li = nxt

        res = post & pre
        if not res:
            return -1
        return max(res)

    # Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)