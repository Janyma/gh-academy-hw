def unique(s):
    letters= list(s)
    a={}
    for i in letters:
        if i in a:
            k=a[i]
            a[i]+=1
        else:
            a[i]=1
    for i, key in enumerate(letters):
        if a[key]==1:
            
            return i
        else:
            continue
    return -1
    



print(unique("alllamb"))