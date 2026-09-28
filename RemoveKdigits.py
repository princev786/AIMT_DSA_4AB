s= "72351986"
k = 3
st = []

if k>=len(s):
    print("0")
    exit()
else:
    for c in s:
        while k>0 and len(st)!=0 and st[len(st)-1]>c:
            st.pop()
            k-=1
        st.append(c)
    
