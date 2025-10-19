from collections import defaultdict


def majorityElement(nums):
        n = len(nums)
        m=defaultdict(int)
        for num in nums:
            m[num]+=1

        n=n//2

        for key, value in m.items():
            if value>n:
                return key
        return 0

print(majorityElement([3,5,2,5,7,7,7,9,7,7,7,7]))

        