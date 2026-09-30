def mergesort(lst,p,r):
    if p<r:
        q = p+(r-p)//2
        mergesort(lst,p,q)
        mergesort(lst,q+1,r)
        merge(lst,p,q,r)

def merge(lst,p,q,r):
    left=[]
    right=[]
    for i in range(p,q+1):
        left.append(lst[i])
    for j in range(q+1,r+1):
        right.append(lst[j])

    i,j,k=0,0,p
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            lst[k] = left[i]
            i+=1
        else:
            lst[k] = right[j]
            j+=1
        k+=1
    while i<len(left):
        lst[k] = left[i]
        k+=1
        i+=1
    while j<len(right):
        lst[k] = right[j]
        k+=1
        j+=1


lst = [25,1,84,56,1,5,10]
mergesort(lst,0,len(lst)-1)
print(lst)