## 217. COntains Duplicates



## ----- ##
# Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element is distinct.
## ----- ##

# INPUT
nums = [1, 2, 3, 5, 1]

def checkDup(nums):
    if len(set(nums)) == len(nums): 
        return False
    else: 
        return True
    
a = checkDup(nums)
print(a)


## ----- ##
## 4 built-in data type: Set, List, Tuple, Dictionary

# Set -> used to store data 
exampleSet = {""}