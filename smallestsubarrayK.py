lst=[10,9,2,17,21,3,9]
k=25
l=0
sum=0
minlength =math.inf

for r in range(0,len(lst)):
    sum+=lst[r]

    while sum>k:
        minlength = min(minlength,r-l+1)
        sum-=lst[l]

print(minlength)

