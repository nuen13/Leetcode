


def happyNumber(n):
    def returnNextNumber(num: int) -> int:
            num = str(num)
            ssum = 0
            for n in num:
                ssum += (int(n) * int(n))
            return ssum

    hashtable = dict()

    while n != 1:
        if n in hashtable:
            return False
        else:
            hashtable[n] = 1
            print(hashtable)
        n = returnNextNumber(n)
        print(n)
    
    return True

n = 123
print(happyNumber(n))