def twoSum(nums, target):
        a = {}
        for i in range(len(nums)):
            if target-nums[i] in a:
                return i, a[target-nums[i]]
            else:
                a[nums[i]]= i

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    result = twoSum(nums, target)
    print(result)