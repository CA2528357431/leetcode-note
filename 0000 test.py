n = 3
def find(cur, i):
    if i == n:
        print(cur)
        return
    find(cur, i + 1)

    cur[i] = True
    find(cur, i + 1)
    cur[i] = False

find([False]*3,0)