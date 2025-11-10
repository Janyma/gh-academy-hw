
def rotate(nums, k):
    a=[0 for _ in nums]
    for i in range(len(nums)):
        a[i]=nums[i]
    #a=nums
    b=0
    for i in range(k+1, len(nums)):
        nums[b]=a[i]
        b+=1
    for j in range(k+1):
        nums[b]=a[j]
        b+=1
    return nums

print(rotate([1,2,3,4,5,6,7], 3))        
        