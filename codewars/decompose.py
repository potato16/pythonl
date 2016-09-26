def decompose(n):
    n = deform(n)
    i = 2
    bag = []
    tmp = n.split('/')
    tmpa = int(tmp[0]) // int (tmp[1])
    if tmpa >0:
        bag.append(str(tmpa))
        tmp[0]=str(int(tmp[0])-tmpa*int(tmp[1]))
        n = tmp[0]+'/'+tmp[1]
    while True:
        if tmp[0] == '0':
            return bag
        b = str(1)+'/'+str(i)
        tmp = truphanso(n,b)
        
        if ispositive(tmp):
            bag.append(b)
            print(bag,tmp,n,b)
            n = tmp
            #This is where 'i' show how thing work faster
        else:
            i+=1
def truphanso(a,b):
    tmp = a.split('/')
    a1 = int(tmp[0])
    b1 = int(tmp[1])
    tmp = b.split('/')
    c1= int(tmp[0])
    d1 = int(tmp[1])
    return str(a1*d1-c1*b1)+'/'+str(b1*d1)
def ispositive(n):
    tmp = n.split('/')
    a = int(tmp[0])
    return True if a >= 0 else False
def deform(n):
    if '/' not in n:
        if '.' not in n:
            return n+'/1'
        else:
            return n.replace('.','')+'/'+str(10**(len(n)-1-n.index('.')))
    return n
def gdc(a,b):#a>b 
    if b == 0:
        return a
    return gdc(b,a%b)
#print(truphanso('19/46','1/2'))
print(gdc(82600,16))
#print(gdc(16,82600))
#print(decompose('0.66'))
