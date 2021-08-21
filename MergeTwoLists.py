def MergeTwoLists(a,b):
    res=[]
    i=j=0
    m=len(a)
    n=len(b)

    while i<m and j<n:
        if a[i]<b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1

    while i<m:
        res.append(a[i])
        i+=1

    while j<n:
        res.append(b[j])
        j+=1

    return res

a=[10,15]
b=[5,6,6,30,40]
print(*MergeTwoLists(a,b))

