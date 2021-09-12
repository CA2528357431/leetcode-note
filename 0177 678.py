class Solution:
    def checkValidString(self, s: str) -> bool:
        le = []
        st = []
        for char in range(len(s)):
            if s[char]=="(":
                le.append(char)
            elif s[char]=="*":
                st.append(char)
            else:
                if not le and not st:
                    return False
                elif le:
                    le.pop()
                else:
                    st.pop()
        while le and st:
            lenum = le.pop()
            stnum = st.pop()
            if lenum>stnum:
                return False
        if le:
            return False
        else:
            return True