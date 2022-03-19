class Solution:
    def longestWord(self, words: List[str]) -> str:
        dic = {}
        for w in words:
            cur = dic
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur[""] = None

        def judge(tree, w):
            cur = tree
            for c in w:

                if c in cur:
                    cur = cur[c]
                    if "" not in cur:
                        return False
                else:
                    return False
            return True

        cur = -1
        for i in range(len(words)):
            if len(words[i]) == 1:
                cur = i
                break
        if cur < 0:
            return ""
        for i in range(len(words)):
            w = words[i]
            if judge(dic, w) and ((len(w) == len(words[cur]) and w < words[cur]) or (len(w) > len(words[cur]))):
                cur = i

        return words[cur]
