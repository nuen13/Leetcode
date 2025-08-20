## input = [1, 3, 0]


nums =  [0, 1]


def missingNum(nums):

    expectedSum = sum(range(len(nums) + 1))
    actualSum = sum(nums)

    missingNum = expectedSum - actualSum

    return missingNum

a = missingNum(nums)

print(a)
