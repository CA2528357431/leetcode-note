class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        li = list(word)
        index = -1
        for i in range(len(word)):
            if word[i]==ch:
                index = i
                break
        if i<0:
            return word
        for i in range(0,index//2+1):
            li[i],li[index-i] = li[index-i],li[i]
        return "".join(li)