def removeDuplicates(nums):
    j=0
    for i in range(1, len(nums)):
        if(nums[j]!=nums[i] ):
            j+=1
            nums[j]=nums[i]
    return j+1
    
        


print(removeDuplicates([1,2,4,5,5,5,6,6,7]))