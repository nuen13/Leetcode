
def decrypt(code, k):
    decryptedCode = []
    right = 0 

    for left in range(0, len(code)):
        if k > 0:
            right = left - k
        elif k < 0:
            right = left + k
        else: 
            for i in range(0, len(code)):
                decryptedCode.append(0)
            return decryptedCode

        temp = 0
        for i in range(min(left, right), max(left, right)):
            print(i)
            temp += code[i]

        decryptedCode.append(temp)

    return decryptedCode





code = [1, 2, 3, 4]
k = 3

print(decrypt(code, k))
# ## code = [12,10,16,13]