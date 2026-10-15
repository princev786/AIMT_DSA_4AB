def quicksort(lst,p,r):
    if p<r:
        pidx = partition(lst,p,r)
        quicksort(lst,p,pidx-1)
        quicksort(lst,pidx+1,r)

def partition(lst,p,r):
    i=p-1
    pivot = lst[r]
    for j in range(p,r):
        if lst[j]<=pivot:
            temp = lst[i+1]
            lst[i+1] = lst[j]
            lst[j] = temp
            i+=1
    temp = lst[i+1]
    lst[i+1] = pivot
    lst[r] = temp
    return i+1


lst = [12,5,7,1,10,3,21]
quicksort(lst,0,len(lst)-1)
print(lst)