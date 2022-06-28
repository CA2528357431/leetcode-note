class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        li = s.split()
        cur = -999
        for x in li:
            if x.isnumeric():
                neo = int(x)
                if neo<=cur:
                    return False
                else:
                    cur = neo
        return True