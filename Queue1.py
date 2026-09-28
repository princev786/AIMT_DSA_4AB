st1 =[]
st2 =[]

def enqueue(val):
    if len(st1)==0:
        if len(st2)==0:
            st1.append(val)
        else:
            while len(st2)!=0:
                st1.append(st2.pop())
            st1.append(val)
    else:
        st1.append(val)

def dequeue():
    if len(st2)==0:
        while len(st1)!=0:
            st2.append(st1.pop())
        return st2.pop()
    return st2.pop()
        
