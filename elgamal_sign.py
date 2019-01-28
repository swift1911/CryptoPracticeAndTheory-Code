from square_and_mutl import square_and_multiply
from math import gcd
import gmpy


def elgamal_sign_sol(p,alpha,beta,msg):
    for i in range(p):
        if square_and_multiply(alpha,i,p)==beta:
            a=i
    print('a=',a)
    for i in range(p):
        y=square_and_multiply(a,i,p)
        if y==23972 and gcd(i,p-1)==1:
            print('k=',i)
            print('y=',y)
            m=gmpy.invert(i,p-1)
            print('m=',m)
            theta=((msg[0]-a*y)*m)%(p-1)
            print(theta)



if __name__ == "__main__":
    elgamal_sign_sol(31847,5,25703,[8990,31415])