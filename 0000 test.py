def gettime(l,time,change):
    res = 0
    for i in range(l):
        res += time
        if i!=l-1:
            if (res // change) % 2 == 1:
                res = (res // (2 * change) + 1) * (2 * change)
    return res
x = gettime(3,3,2)
print(x)