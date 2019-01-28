

r_list=[9,13,24,0,7,15,14,17,25,16,22,1,19,18,5,11,6,2,21,12,20,4,10,8,3,23]

print(len(r_list))

i="TPXCKGDXQXRHKDTFGGHOUTCDLFNVXDTHWXYXUWWXROCOHUC"

for item in i:
    print(chr(65+r_list.index(ord(item)-65)),end='')