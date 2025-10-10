
## BINARY SEARCH PROBLEM

## 153. Find Minimum In Rotated Sorted Array


# Given an array nums, sorted in ascending order
# it is rorated n times(first number -> move to last)
# find the original first element of that arraay after being rotated




def findMin(nums):
    left, right = 0, len(nums) - 1 
    min_num_index = -1

    while left <= right: 
        mid = (left + right) // 2

        if nums[mid] <= nums[-1]:
            min_num_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return nums[min_num_index]



nums = [11,13,15,17]
print(findMin(nums))