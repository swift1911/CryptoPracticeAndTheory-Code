import math

def hashh2(input_list,mod):
    sum = 0
    for i in input_list:
        sum+=math.pow(i,2)
    return sum%mod


a=[189,632,900,722,349]

print(hashh2(a,989))