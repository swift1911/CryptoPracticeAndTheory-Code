# from ecc import ecc_mult
# from math import gcd

# def ecdsa(alpha,a,p,k):
#     beta=ecc_mult(alpha,p,a)
#     print(beta)

#     for i in range(p-1):
#         if gcd(i,p-1)
#     u,v=beta
#     r=u%p
    

# if __name__ == "__main__":
#     ecdsa((2,6),54,127,75)
from square_and_mutl import *
from ecc import divide_mod

def dsa(p,q,alpla,a,k):
    beta=4567
    sha1=22
    y=square_and_multiply(alpla,k,p)%q
    sita=divide_mod((sha1+a*y),k,q)
    print(y,sita)

    e1=divide_mod(sha1,sita,q)
    e2=divide_mod(y,sita,q)
    print(e1,e2)

    yt = ((square_and_multiply(alpla,e1,p)*square_and_multiply(beta,e2,p))%p)%q
    print(yt)
if __name__ == "__main__":
    dsa(7879,101,170,75,50)