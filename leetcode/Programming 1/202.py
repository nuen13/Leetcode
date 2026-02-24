"""
Docstring for leetcode.Programming 1.202
    NOTE:
        - string to int: int(n)
        - int to string: str(n)

"""

##### ------ 202. Happy Number ------ ######
# Determined if a number is happy:
# 1. Starting with the sum of the 2 number squared 
# 2. Repeat the process until it equal to 1


## Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

## Example 2:

# Input: n = 2
# Output: false


"""
UNDERSTAND:
    - n cant be neg 
    - if sum of all component in n = 1 -> True 
    - if sum of all component in n = to a number that already happen -> recurrent -> Flase


"""


##--- INPUT -> int
n = 7

## --- OUTPUT -> bool
happy = False 

## --- Process
## Way 1: 
def isHappy(n):
    existList = []
    

    while True:
        nString = str(n)
        total = 0 
        for i in range(0, len(nString)):
            total += int(nString[i]) * int(nString[i])
        if total == 1:
            return True 
        else:
            if total in existList:
                return False
            else: 
                n = total
                existList.append(total)

       

    


## --- Return
output = isHappy(n)
print(output)



