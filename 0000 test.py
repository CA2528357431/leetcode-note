import heapq

a = {'a':1,'b':2}
b = {'b':2,'a':1}
dic = {1:13,2:55,0:12,5:99}
li = [(-dic[x],x) for x in dic]
heapq.heapify(li)
print(li)