
import numpy as np
import gmpy
from square_and_mutl import *


def dencrypt(en,a,n):
    plain=square_and_multiply(int(en),a,n)
    for i in range(26):
        for j in range(26):
            for k in range(26):
                m1=26*26*i
                m2=26*j
                m3=k
                if m1+m2+m3==plain:
                    print(chr(i+97)+chr(j+97)+chr(k+97),end='')

def rsa_sol(n,b,sec):
    divideList= divPrime(n)
    p,q=divideList[0],divideList[1]
    f=(p-1)*(q-1)
    a=gmpy.invert(b,f)
    print(a)
    sec_list=sec.split(' ')
    for i in sec_list:
        dencrypt(i,a,n)
    print('')

def rsa_en(p,q,b,plain):
    f=(p-1)*(q-1)
    n=p*q
    a=gmpy.invert(b,f)
    print(a)
    en = square_and_multiply(plain,b,n)
    print(en)
    pl = square_and_multiply(7,a,n)
    print (pl)




def divPrime(num):
    lt = []
    while num != 1:
        for i in range(2, int(num+1)):
            if num % i == 0: 
                lt.append(i)
                num = num / i
                break
    return lt
 


if __name__ == "__main__":
    n=31313
    b=4913
    sec='''6340 8309 14010 8936 27358 25023 16481 25809 23614 7135 24996 30590 27570 26486 30388 9395
27584 14999 4517 12146 29421 26439 1606 17881 25774 7647 23901 7372 25774 18436 12056 13547
7908 8635 2149 1908 22076 7372 8686 1304 4082 11803 5314 107 7359 22470 7372 22827 15698
30317 4685 14696 30388 8671 29956 15705 1417 26905 25809 28347 26277 7897 20240 21519 12437
1108 27106 18743 24144 10685 25234 30155 23005 8267 9917 7994 9694 2149 10042 27705 15930
29748 8635 23645 11738 24591 20240 27212 27486 9741 2149 29329 2149 5501 14015 30155 18154
22319 27705 20321 23254 13624 3249 5443 2149 16975 16087 14600 27705 19386 7325 26277 19554
23614 7553 4734 8091 23973 14015 107 3183 17347 25234 4595 21498 6360 19837 8463 6000 31280
29413 2066 369 23204 8425 7792 25973 4477 30989'''
    rsa_sol(n,b,sec.replace('\n',''))
    rsa_en(67,89,17,4239)
