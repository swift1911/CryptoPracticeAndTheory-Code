from math import pow
from ext_ecuid import ext_euclid
import gmpy


def robin(p,q,B,x):
    n=p*q
    enp=(x*(x+B))%n
    print(enp)
    mp = pow(enp,(p+1)/4)%p
    mq = pow(enp,(q+1)/4)%q
    print(mp,mq)
    yp,_,_ = ext_euclid(p,q)
    yq,_,_ = ext_euclid(q,p)
    print(yp,yq)
    
    a = (yp*p*mq + yq*q*mp)%n
    b = n - int(a)
    c = (yp*p*mq - yq*q*mp)%n
    d = n - int(c)
    print(a,b,c,d)

    

if __name__ == "__main__":
    robin(199,211,1357,32767)