import os
path = "E:\leetcode"
datanames = os.listdir(path)
li1 = []
li2 = []
for i in datanames:
    if "test" in i:
        continue
    if "py" not in i:
        continue
    if " " not in i:
        continue
    num = i[5:-3]
    if num.isdecimal():
        li1.append(int(num))
    else:
        li2.append(num)
li1.sort()
li2.sort()
print(li1)
print(li2)