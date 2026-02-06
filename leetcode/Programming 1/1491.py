
"""
    NOTE: 
        + max(array) and min() => O(n)
        + pop() 
            -> if pop() or pop(-1) => O(1)
            -> if pop(i) -> i is not first or last => O(n)
            - pop(index)
        + array.index(SOMETHING) => index 
            + not exist -> -1

"""



# Given an array of integer
# Find the mean of every number, excluding the highest and lowest number 


# input -> (array of number)
salary = [4000,3000,1000,2000]


# output -> double 
output = 0


# process 

## Way 1: 
# def average(salary):
#     mean = 0 

#     i =  1
#     salary.sort()
#     total = 0 
#     while i <= len(salary) - 2:
#         total += salary[i]
#         i += 1 

#     mean = total / (i - 1)


#     return mean 



# way 2: 
# def average(salary):

#     maxNum = max(salary)
#     minNum = min(salary)

#     output = 0 

#     for num in salary:
#         if num != maxNum and num != minNum:
#             output += num
    
#     output = output / (len(salary) - 2)

#     return output 





# Way 3: NO LOOP 
def average(salary):
    maxNum = max(salary)
    minNum = min(salary)

    salary.pop(salary.index(maxNum))
    salary.pop(salary.index(minNum))

    output = sum(salary) / len(salary)
    
    return output


output = average(salary);

print(output);