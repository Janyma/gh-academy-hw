def singleNumber(nums):
    ans=0
    for i in range(len(nums)):
        ans^=nums[i]
    return ans

print(singleNumber([2,2,4,5,4]))


        