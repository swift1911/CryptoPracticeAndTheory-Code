from math import pow
import gmpy
from square_and_mutl import square_and_multiply

def ecc_sol(p):
    for i in range(p):
        m=(pow(i,3)+i+1)%p
        if square_and_multiply(m,(p-1)//2,p)==1:
            z=pow(m,(p+1)//4)
            y1=z%p
            y2=-z%p
            print(i,m,y1,y2)
    
def divide_mod(m,n,p):
    return ((m%p)*(gmpy.invert(n,p)))%p 

def ecc_plus(p,q,z):
    if p!=q:
        numd=divide_mod((q[1]-p[1]),(q[0]-p[0]),z)
        x3= (pow(numd,2)-p[0]-q[0])%z
        y3= (numd*(p[0]-x3)-p[1])%z
        print(x3,y3)
        return (int(x3),int(y3))
    else:
        numd=divide_mod(3*pow(p[0],2)+1,2*p[1],z)
        x3=(pow(numd,2)-p[0]-q[0])%z
        y3=(numd*(p[0]-x3)-p[1])%z
        return (int(x3),int(y3))


def ecc_mult(p,z,m):
    result = ()
    for i in range(m):
        result = ecc_plus(p,p,z)
    return result
    

if __name__ == "__main__":
    ecc_sol(19)
    ecc_plus((2, 7), (13, 11),19)
    print(ecc_mult((2,7),11,2))