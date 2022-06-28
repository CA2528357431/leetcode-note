class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mat = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        def get(c):
            return ord(c)-ord("a")
        se = set()
        for w in words:
            li = []
            for c in w:
                neo = mat[get(c)]
                li.append(neo)
            s = "".join(li)
            se.add(s)
        return len(se)