def  binary_search(arr,target):
    left,right=0,len(arr)-1
    
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
           return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
sorted_list=[1,3,5,7,9,11,12,13,15,17]
target=int(input("enter the seach position:"))
result=binary_search(sorted_list,target)
if result!=-1:
    print("found index at",result)
else:
    print("not found index")