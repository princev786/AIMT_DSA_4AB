lst=[10,5,1,6,7,3]
res=list(lst)
st = [] #stack

for i in range(len(lst)-1,-1,-1):
    while len(st)!=0 and st[len(st)-1]<=lst[i]:
        st.pop()

    if len(st)==0:
        res[i] = -1
    else:
        res[i] = st[len(st)-1]

    st.append(lst[i])
print(res)
    


