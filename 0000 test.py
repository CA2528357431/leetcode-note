import os

path=r'E:\leetcode'
files=os.listdir(path)
neo = {}
for s in files:
    ss = s[5:-3]
    if ss.isdecimal():
        if ss in neo:
            print(s)
        neo[ss]=0
