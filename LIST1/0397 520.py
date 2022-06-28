class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<=1:
            return True

        judge = word[1].isupper()
        if judge and not word[0].isupper():
            return False

        for i in range(2,len(word)):
            if word[i].isupper()!=judge:
                return False
        return True