from square_and_mutl import square_and_multiply
import gmpy
from ecc import divide_mod

def elgamal(p,alpha,beta):
    for i in range(p):
        if square_and_multiply(alpha,i,p)==beta:
            #calc a
            print('a: ',end='')
            print(i)
            return i
    

def elgamal_sol(p,alpha,x,k,key):
    beta=square_and_multiply(alpha,key,p)
    print('beta:',beta)
    y1=square_and_multiply(alpha,k,p)
    y2=(x*square_and_multiply(beta,k,p))%p
    print('cipher result is:',end='')
    print((y1,y2))
    # y1=2
    # y2=141

    #plain=((y2%p)*gmpy.invert(square_and_multiply(y1,key,p),p))%p
    plain=divide_mod(y2,pow(y1,key),p)
    print(plain)


if __name__ == "__main__":
    key = elgamal(31847,7,18074)
    elgamal_sol(31847,7,389,511,key)
    #elgamal_sol(2579,2,1299,853,765)
    elgamal_sol(541,2,389,6,173)

    print(divide_mod(141,pow(2,173),541))