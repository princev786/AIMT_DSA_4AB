lst = [10,2,-2,-20,10]
k=-10
c=0
sum=0
dict = {0:1}

for r in range(0,len(lst)):
    sum += lst[r]
    if sum-k in dict.keys():
        c += dict[sum-k]
    if sum not in dict.keys():
        dict[sum]=1
    else:
        dict[sum]+=1

print(c)

