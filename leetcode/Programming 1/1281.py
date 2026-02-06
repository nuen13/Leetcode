
'''
    NOTE: 
        + // -> chia hết 234 // 10 = 23.4 -> làm tròn thành 23
        + % -> module -> lấy số dư -> 234 % 10 = 23 dư 4 > kết quả là 4

        


'''


# Given positive n 
# Return product(all digits) - sum(all digits)


## input - n(int) -> positive
n = 234


## output (int)
output = 0



## process

## WAY 1: 
# def subtractProductandSum(n):
    
#     stringNums = str(n)
#     prodNums = 1
#     sumNums = 0

#     for num in stringNums:
#         prodNums *= int(num)
#         sumNums += int(num)


    
#     return prodNums - sumNums 



## WAY 2:
def subtractProductandSum(n):

    output = n

    dsum = 0 
    dprod = 1

    while output > 0:
        digit = output % 10

        dsum += digit 
        dprod *= digit

        output = output // 10

    return dprod - dsum



output = subtractProductandSum(n)
print(output)