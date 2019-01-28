import math
from rsa_param import gcd

elem=2
mod=11

print('original elem :  ',end='')
for i in range(0,mod-1):
    if gcd(i,mod-1)==1:
        print(int(math.pow(2,i)%mod),end=' ')