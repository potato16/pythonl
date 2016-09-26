#Rule:
#s: string to be coded
# shift: initial shift
#coded to 5 part
#

def moving_shift(s, shift):
    scoded=''
    for c in s:
        if c.islower():
            scoded+=chr((ord(c)-ord('a')+shift)%26+ord('a'))
        elif c.isupper():
            scoded+=chr((ord(c)-ord('A')+shift)%26+ord('A'))
        else:
            scoded+=c
        shift +=1
    chunks,chunk_size = len(scoded), len(scoded)//5
    if len(scoded)%5 !=0:
        chunk_size+=1
    return [scoded[i:i+chunk_size] for i in range(0,chunks,chunk_size)]
def demoving_shift(s, shift):
    scoded = ''.join(s)
    sdecoded = ''
    for c in scoded:
        if c.islower():
            sdecoded += chr((ord(c)-ord('a')-shift)%26 + ord('a'))
        elif c.isupper():
            sdecoded += chr((ord(c)-ord('A')-shift)%26 + ord('A'))
        else:
            sdecoded +=c
        shift +=1
    return sdecoded

#test
s=moving_shift("I should have known that you would have a perfect answer for me!!!",1)
print(demoving_shift(s,1))
