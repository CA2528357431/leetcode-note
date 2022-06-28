import os

path=r'E:\leetcode\LIST4\readme.txt'
with open(path,"w") as f:
    for i in range(1001,1501):
        s = f"## {i+500}.\n* \n\n"


        f.write(s)