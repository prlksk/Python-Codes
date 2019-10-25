import eulerlib
import math
import time
once=time.time()
pliste=eulerlib.prime_generator(10**8)
print(pliste(13))
def is_prime(a):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, sqrt(x) + 1, 2):
            if x % i == 0:
                return False
        return True

def func(p):
    for i in range(1,p):
        if (8*i+3)%p==0:
            return i

toplam=0
for p in pliste:
        toplam=toplam+func(p)        

print(toplam)
sonra=time.time()
print("time: {}".format(str(sonra-once)[0:7]))
