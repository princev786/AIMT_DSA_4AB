lst = [2,1,3,2,1]
k = 6
maxlen=0
l=0
sum=0

for r in range(0,len(lst)):
    sum += lst[r]
    while sum>k:
        sum -= lst[l]
        l+=1
    if sum<=k:
        maxlen = max(maxlen,r-l+1)

print(maxlen)
