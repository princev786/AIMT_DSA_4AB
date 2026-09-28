lst = [9,10,5,7,12,6,15,2,12]
k = 3
max=0
curr=0
start = 0
end =0 

for i in range(0,k):
    curr+=lst[i]
if max<curr:
    max = curr
for i in range(k,len(lst)):
    curr -= lst[i-k]
    curr += lst[i]
    if curr>max:
        max = curr
        start = i-k+1
        end = i

print(max)
print(lst[start : end+1])