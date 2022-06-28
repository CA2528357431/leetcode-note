class Solution:
    def simplifyPath(self, path: str) -> str:
        li = path.split("/")
        res = []
        for c in li:

            if c == "..":

                if res:
                    res.pop()
            elif c == "" or c == ".":
                pass
            else:
                res.append(c)

        p = "/" + "/".join(res)
        return p