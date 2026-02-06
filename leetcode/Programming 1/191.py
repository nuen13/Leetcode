
'''
    NOTE: 
        + convert int -> binary: bin(n) (string)
        + type(something) -> check type


'''
# given a positive number n 
# convert it to binary 
# return number of '1' in its binary number 



## input: n (int) -> positive
n = 11

## output (n)
output = 0


## process
## Way 1:

# def hammingWeight(n):

#     binN = bin(n)
#     output = 0

#     for one in binN:
#         if one == "1":
#             output += 1


#     return output



## Way 2: Copy 
def hammingWeight(n):
        res = 0

        for i in range(32):
            if (n >> i) & 1:
                res += 1

        return res



## Understand it as - Python always stored decimal in BINARY 
## so it just use the binary form when needed
## and using >> it will use binary form 

## Lay it out as 0000 0000 0000 0000 0000 0000 0000 0000
## n = 11
## 0000 0000 0000 0000 0000 0000 0000 1011
## if (n >> i) & 1 -> This is like run through all binary -> if it = 1 (& 1) + 1




## Show result 
output = hammingWeight(n)
print(output)