lst = [1,0,1,0,0,0,1,1,0,0,0,0]
maxcount = 0
count=0

for i in range(0,len(lst)):
    if lst[i]==0:
        count+=1
    elif count!=0:
        maxcount = Math.max(maxcount,count)
        count =0

maxcount = Math.max(maxcount,count)
print(maxcount)
