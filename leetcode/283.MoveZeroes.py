





def moveZeroes(nums):
    l, r = 0, 1

    while r < len(nums) :
        if nums[l] == 0:
            if nums[r] == 0:
                r += 1
            else: 
                nums[l], nums[r] = nums[r], nums[l]
                r += 1
                l += 1
        else:
            l += 1 
            r += 1 
    return nums

nums = [1, 0, 1]
print(moveZeroes(nums))