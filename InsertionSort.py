def InsertionSort(l):
    for i in range (1,len(l)):
        x=l[i]
        j=i-1
        while j>=0 and x<l[j]:
            l[j+1]=l[j]
            j=j-1
        print(j)
        l[j+1]=x

l=[20,5,40,60,10,30]
InsertionSort(l)
print(*l)