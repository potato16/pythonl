def power_sumDigTerm(n):
    #the mu
    #tu **2 -->
    #break when **2>= 10**2
    #    return None # n-th term of the sequence, each term is a power of the sum of its digits
    i = 0 # n-th
    m = 2 #number digit
    while True:
        p = 2
        _flag = True
        while True:
            for a in range(2,9*m):
                tmp = a**p
                if tmp < 10**m:
                    tmpadd = 0
                    for c in str(tmp):
                        tmpadd += int(c)
                if tmpadd == a:
                    print(tmp)
                    i += 1
                    if i == n:
                        return tmp
                else:
                    _flag = False
                    break
                
            p +=1
        m +=1
power_sumDigTerm(4)
