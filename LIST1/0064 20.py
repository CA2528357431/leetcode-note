class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == "(" or x == "{" or x == "[":
                stack.append(x)
            elif x == ")" or x == "}" or x == "]":
                if not stack:
                    return False
                if x == ")":
                    if stack.pop()!="(":
                        return False
                elif x == "]":
                    if stack.pop()!="[":
                        return False
                else:
                    if stack.pop()!="{":
                        return False
        if stack:
            return False
        else:
            return True