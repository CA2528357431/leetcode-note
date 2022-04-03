class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        for c in letters:
            if c>target:
                return c
        return letters[0]