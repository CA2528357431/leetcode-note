
ps = [1,3,6,8,9,10]
def f(ps,p):
                l = 0
                r = len(ps)-1
                while l<r:
                    mid = (l+r)//2+1
                    if p<ps[mid]:
                        r = mid-1
                    elif ps[mid]<p:
                        l = mid
                print(ps[l])
f(ps,7)
