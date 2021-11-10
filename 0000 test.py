def clean(li):
    while True:
        for i in range(len(li) - 2):
            if li[i] == li[i + 1] and li[i + 1] == li[i + 2]:
                cur = li[i]
                while i<len(li) and li[i]==cur:
                    li.pop(i)
                break
        else:
            return
li = [3,3,1,1,1,3,3,4,5]
clean(li)
print(li)