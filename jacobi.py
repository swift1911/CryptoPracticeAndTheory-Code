
from rsa_param import gcd

def jacobi(a,b):
    sysbol=1
    while a>=2:
        if a<b:
            sysbol*=switch(a,b)
            a,b=b,a
        a=a%b
        while a%2!=1 and a>2:
            a=a//2
    a,b=b,a
    if a==2:
        if b%8 in (3,5):
            return -1*sysbol
        else:
            return sysbol
    else:
        return 1


def switch(m,n):
    if m%4==m%4==3:
        return -1
    else:
        return 1

if __name__ == "__main__":
    print(jacobi(20964,1987))