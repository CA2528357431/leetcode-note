arr = [7,4,5,1,2,3,6,9,8,0,11,-3,5,9]


def quick(l, r):
    i = l
    j = r
    x = arr[l]
    while i < j:
        while i < j and arr[j] >= x:
            j -= 1
        arr[i] = arr[j]

        while i < j and arr[i] <= x:
            i += 1
        arr[j] = arr[i]
    arr[i] = x
    return i


def sort(l, r):
    if l >= r:
        return
    mid = quick(l, r)
    sort(l, mid - 1)
    sort(mid + 1, r)



sort(0,len(arr)-1)

print(arr)

