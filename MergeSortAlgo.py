def MergeSortAlgo(a,low,mid,high):
    left=a[low:mid+1]
    right=a[mid+1:high+1]
    i=j=0
    k=low
    m=len(left)
    n=len(right)
    while i<m and j<n:
        if left[i]<right[j]:
            a[k]=left[i]
            i=i+1
            k=k+1
        else:
            a[k]=right[j]
            j=j+1
            k=k+1

    while i<m:
        a[k]=left[i]
        i=i+1
        k=k+1

    while j<n:
        a[k]=right[j]
        j=j+1
        k=k+1

def merge(arr,l,r):
    if r>l:
        mid=(l+r)//2
        merge(arr,l,mid)
        merge(arr,mid+1,r)
        MergeSortAlgo(arr,l,mid,r)

arr=[10,5,30,15,7]

merge(arr,0,4)
print(*arr)
