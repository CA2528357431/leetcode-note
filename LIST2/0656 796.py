class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in s*2 and len(s)==len(goal)