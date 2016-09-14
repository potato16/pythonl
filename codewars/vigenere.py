class VigenereAutokeyCipher:
    def __init__(self,key, abc):
        self.key = key
        self.abc = abc
    def encode(self, text):
        tmp = ''
        i = 0
        for c in text:
            if c in abc:
                tmp += abc[(abc.index(c)+abc.index(key[i]))%len(abc)]
                i += 1
                if i >= len(key):
                    key = tmp
                    i = 0
            else:
                tmp += c
        return tmp
    def decode(self, text):
        tmp=''
        i=0
        for c in text:
            if c in abc:
                tmp += abc[(abc.index(c)-abc.index(key[i]))%len(abc)]
                i += 1
                if i >= len(key):
                    key = tmp
                    i = 0
            else:
                tmp +=c
        return tmp
key = 'password';
abc = 'abcdefghijklmnopqrstuvwxyz';

c = VigenereAutokeyCipher(key, abc);
print(c.encode('AAAAAAAAPASSWORDAAAAAAAA'))
print(c.decode('PASSWORDPASSWORDPASSWORD'))
