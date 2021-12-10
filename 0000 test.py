import random
import time
random.seed(time.time())
with open("data.txt","w") as f:
    for i in range(40):
        x = random.randint(-100,100)
        f.write(str(x)+",")
li = "aaa"
li.lower()