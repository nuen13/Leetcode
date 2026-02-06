'''

'''



# Given an array of nums 
# Return largest P -> parameter of a triangle formed three of these length 
# If it is impossible to form a triangle return 0 


## P = a + b + c
## To make a triangle 
## a + b > c
## a + c > b
## b + c > a 

## input 
# nums = [2, 1, 2]
nums =[1,2,1,3,10, 4, 5]
1, 1, 2, 3, 4, 5, 10 
7 
## output 
# paramater of the possible triangle 
p = 0 


## process
# Make sure that it is able to form a triangle then add it together 


def largestPerimeter(nums):

    for i in range(7 - 1, 1, -1):
        print(i)

    return p


p = largestPerimeter(nums)
print(p)