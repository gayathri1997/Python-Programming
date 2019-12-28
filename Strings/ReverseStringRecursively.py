def revStrRecursive(st, start, end):
    if start >= end:
        return
    else:
        st[start], st[end] = st[end], st[start]
        revStrRecursive(st, start+1, end-1)

st = list('gayathri')
revStrRecursive(st, 0, len(st)-1)
print("".join(st))
