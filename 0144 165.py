class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        # 直观

        '''
        li1 = version1.split(".")
        li2 = version2.split(".")
        p1 = 0
        p2 = 0
        while p1 < len(li1) and p2 < len(li2):

            num1 = int(li1[p1])
            num2 = int(li2[p2])

            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            else:
                p1 += 1
                p2 += 1
        if p1 == len(li1) and p2 < len(li2):

            while p2 < len(li2):
                num2 = int(li2[p2])
                if num2 > 0:
                    return -1
                else:
                    p2 += 1
            return 0
        elif p1 < len(li1) and p2 == len(li2):
            while p1 < len(li1):
                num1 = int(li1[p1])
                if num1 > 0:
                    return 1
                else:
                    p1 += 1
            return 0
        else:
            return 0
        '''

        # 内存优化

        p1 = 0
        p2 = 0
        while p1 < len(version1) and p2 < len(version2):
            num1 = 0
            num2 = 0
            while p1 < len(version1) and version1[p1] != ".":
                num1 = num1 * 10 + int(version1[p1])
                p1 += 1
            while p2 < len(version2) and version2[p2] != ".":
                num2 = num2 * 10 + int(version2[p2])
                p2 += 1
            print(p1,p2)
            if num1<num2:
                return -1
            elif num1>num2:
                return 1
            else:
                p1+=1
                p2+=1

        if p1 >= len(version1) and p2 >= len(version2):
            return 0
        elif p1 >= len(version1):
            while p2<len(version2):
                if version2[p2] != "." and version2[p2] != "0":
                    return -1
                else:
                    p2+=1
            return 0
        else:
            while p1<len(version1):
                if version1[p1] != "." and version1[p1] != "0":
                    return 1
                else:
                    p1+=1
            return 0
sol = Solution()
a = sol.compareVersion("1.01","1.01.1")
print(a)
