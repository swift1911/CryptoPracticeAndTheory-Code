def ext_euclid(a, b):
     if b == 0:
         return 1, 0, a
     else:
         x, y, q = ext_euclid(b, a % b)
         x, y = y, (x - (a // b) * y)
         return x, y, q

if __name__=="__main__":
    r0,r1=11,7
    t,s,q = ext_euclid(r0,r1)
    print(t%r1)