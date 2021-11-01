class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {'q':0, 'w':0, 'e':0, 'r':0, 't':0, 'y':0, 'u':0, 'i':0, 'o':0, 'p':0,
               'a':1, 's':1, 'd':1, 'f':1, 'g':1, 'h':1, 'j':1, 'k':1, 'l':1,
               'z':2, 'x':2, 'c':2, 'v':2, 'b':2, 'n':2, 'm':2}
        res = []
        for word in words:
            a = dic[word[0].lower()]
            ok = True
            for c in word[1:]:
                if a != dic[c.lower()]:
                    ok = False
                    break
            if ok == True:
                res.append(word)
        return res