def removeElement(nums, val):
        j=0
        for i in range(len(nums)):
            
            if nums[j]==val:
                nums.remove(nums[j])
                j-=1
            j+=1
        return nums
print(removeElement([3,2,2,3], 3))