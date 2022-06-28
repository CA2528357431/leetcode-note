import os

path=r'E:\leetcode\LIST2\readme.txt'
with open(path,"w") as f:
    for i in range(800,1001):
        s = f"## {i}.\n* \n\n"


        f.write(s)