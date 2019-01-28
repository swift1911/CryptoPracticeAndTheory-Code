from __future__ import division
from fractions import gcd
import string
import numpy as np
def shift(l1,n1):
    return l1[n1:] + l1[:n1]
num = dict(zip(xrange(0,26),string.ascii_lowercase))
A = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]
a9=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=('KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST').lower()
a=list(a)
a1=a
c=0
d=[]
k=1
while k<=10:
    a1 = np.roll(a1,1)
    for i,j in zip(a,a1):
        if i==j:
            c+=1
    print 'Number of coincidences for',k,'shift is:',c
    d.append(c)
    k+=1
    c=0


L=max(d)
print 'Maximum number of coincidence(L):',L
L=d.index(L)
L+=1
L1=sorted(set(d))[-2]#for the second highest number in the list
print 'Second highest number of coincidence(L1):',L1
L1=d.index(L1)
L1+=1
L2=sorted(set(d))[-3]#for the third highest number in the list
print 'Third highest number of coincidence:(L2)',L2
L2=d.index(L2)
L2+=1
lth=[L,L1,L2]
print '\n'+'Possible key lengths are:',L,',',L1,',',L2
d1=gcd(L,L1)
d1=gcd(d1,L2)
print 'gcf of all above shifts:',d1
in1=0
while in1<=2:
    L=lth[in1]
    print '\n'+'Take',L,'as key length'
    z=[[]for x1 in range(0,L)]
    v1=0
    while v1<L:
        for i2 in range(v1,len(a),L):
           z[v1].append(a[i2])
        v1+=1
    v1=0
    Array=[]
    while v1<L:
        W=[]
        for charc in a9:
            b1 = z[v1].count(charc)
            b1 = b1/26
            b1 = round(b1,7)
            W.append(b1)
        I =24
        J=[]
        t=0
        while I>=0:
            B= shift(A,t)
            K = np.dot(W,B)
            K = round(K,6)
            J.append(K)
            I -= 1
            t+=1
        Max1=max(J)#for highest number in the list
        F = [D for D, E in enumerate(J) if E==Max1]# retrieve the index of the maximum number
        F[0]=((26-F[0])%26)
        key=num[F[0]].upper()
        Array.append(key)
        S1=[]
        for character in z[v1]:#loop for getting deciphered numbers
            number = ord(character) - 97
            number = ((number - F[0])%26)
            S1.append(number)
        a2=[]
        for id2 in S1:# loop for number to alphabet mapping
            a2.append(num[id2])
        z[v1]=a2
        v1+=1
    print 'The Encryption Key:',''.join(Array)    

    v1=0
    var=0
    D1=[]
    vv=int(len(a)/L)
    while var<vv:
        while v1<L:
            D1.append(z[v1][var])
            v1+=1
        var+=1
        v1=0
    v1=0
    while v1<(len(a)%L):
        D1.append(z[v1][var])
        v1+=1
    print '\n'+'Your plain Text:'
    print ''.join(str(elm) for elm in D1)
    in1+=1