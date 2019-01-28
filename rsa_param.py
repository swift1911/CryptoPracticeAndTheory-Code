
from ext_ecuid import *
import random
import gmpy
a=680261
b=678709

def gcd(a,b):
    if a<b:
        a,b=b,a

    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def rsa_para(p,q):
    f=(p-1)*(q-1)
    flist=[]
    for i in range(2,f):
        if gcd(i,f)==1:
           flist.append(i)
    b = 17
    a=gmpy.invert(b,f)
    return (f,b),(p,q,a)

if __name__ == "__main__":
    print(rsa_para(67,89))


