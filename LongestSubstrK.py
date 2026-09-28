str = ['a','a','b','c','b','a','c']
k = 2
maxlen =0
l=0
dict = {}

for r in range(0,len(str)):
    curr = str[r]
    if curr not in dict.keys():
        dict[curr]=1
    else:
        dict[curr]+=1

    if len(dict)<=k:
        maxlen = max(maxlen,r-l+1)
    while len(dict)>k and l<r:
        dict[str[l]] -=1
        l += 1
        if dict[str[l]]==0:
            del dict[str[l]]

print(maxlen)

