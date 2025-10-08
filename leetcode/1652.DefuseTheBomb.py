
def decrypt(code, k):
    n = len(code)
    decryptedCode = [0] * n

    right = 0 

    if k == 0: 
        return decryptedCode
    elif k > 0:
        k = - k 
    
    for left in range(0, n):
        for i in range(min(left, right), max(left, right)):
            decryptedCode[left] += code[i]

    return decryptedCode
    

code = [5,2,2,3,1]

k = 3

print(decrypt(code, k))
# ## code = [12,10,16,13]