def binary_search(nums,target):
    low=0
    high=len(nums)-1 
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]==target):
            return mid
        elif(target>nums[mid]):
            low=mid+1
        elif(target<nums[mid]):
            high=mid-1
    return -1
nums=list(map(int,input().split()))
target=int(input())
print(binary_search(nums,target))
