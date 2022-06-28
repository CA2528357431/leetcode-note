class Solution:
    def reverseWords(self, s: str) -> str:
        li = reversed(s.split(" "))
        return " ".join([x for x in li if x])