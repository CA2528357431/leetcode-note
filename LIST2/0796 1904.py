class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        sli = loginTime.split(":")
        eli = logoutTime.split(":")

        sh = int(sli[0])
        sm = int(sli[1])
        eh = int(eli[0])
        em = int(eli[1])

        if eh < sh or eh == sh and em < sm:
            eh += 24

        if sm == 0:
            sm = 0
        elif sm <= 15:
            sm = 15
        elif sm <= 30:
            sm = 30
        elif sm <= 45:
            sm = 45
        else:
            sm = 0
            sh += 1

        if em < 15:
            em = 0
        elif em < 30:
            em = 15
        elif em < 45:
            em = 30
        else:
            em = 45

        minute = 60 * eh + em - 60 * sh - sm
        return max(minute // 15, 0)