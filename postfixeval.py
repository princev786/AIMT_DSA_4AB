s = "232/7*9%+8-"
res =0
st=[]

for i in range(0,len(s)):
    if s[i].isdigit():
        st.append(int(s[i]))
    else:
        first = st.pop()
        second = st.pop()
        match(s[i]):
            case '+':
                st.append(first+second)
                break
            case '-':
                st.append(second-first)
                break
            case '*':
                st.append(second*first)
                break
            case '/':
                st.append(second//first)
                break
            case '%':
                st.append(second%first)
                break
print(st.pop())

    