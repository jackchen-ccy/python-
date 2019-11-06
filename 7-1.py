
def crypt(source,key):
    from itertools import cycle
    result=''
    temp=cycle(key)
    for ch in source:
        result=result+chr(ord(ch)^ord(next(temp)))
    return result
source='Shangdong Institute of Business and Technology'
key='Cui chengyu'
print('Before Encrypted:'+source)
encrypted=crypt(source,key)
print('After Encrypted:'+encrypted)
decrypted=crypt(encrypted,key)
print('After Decrypted:'+decrypted)
