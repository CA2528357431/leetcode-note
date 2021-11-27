class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        count = 0
        mark = -1

        for i in range(len(s)):
            if s[i] != goal[i]:
                if count == 0:
                    count = 1
                    mark = i
                elif count == 1:
                    if s[mark] == goal[i] and s[i] == goal[mark]:
                        count = 2
                    else:
                        return False
                else:
                    return False
        return count == 2 or count == 0 and len(list(s)) != len(set(s))