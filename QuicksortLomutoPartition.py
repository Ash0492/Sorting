def lomuto(arr,l,h):
    pivot=arr[h]
    i=l-1

    for j in range(l,h):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1

def qs(arr,l,h):
    if l<h:
        p=lomuto(arr,l,h)
        qs(arr,l,p-1)
        qs(arr,p+1,h)

arr=[8,4,7,9,3,10,5]
qs(arr,0,6)
print(*arr)


