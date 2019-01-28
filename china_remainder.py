import functools
def egcd(a, b):
    if 0 == b:
        return 1, 0, a
    x, y, q = egcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q

def chinese_remainder(pairs):
    remainder_list,mod_list  = [p[0] for p in pairs], [p[1] for p in pairs]
    mod_product = functools.reduce(lambda x, y: x * y, mod_list)
    mi_list = [mod_product//x for x in mod_list]
    print(mi_list,mod_list,mod_product)
    mi_inverse = [egcd(mi_list[i], mod_list[i])[0] for i in range(len(mi_list))]
    print(mi_inverse)
    x = 0
    for i in range(len(remainder_list)):
        x += mi_list[i] * mi_inverse[i] * remainder_list[i]
        x %= mod_product
    return x


if __name__=='__main__':
    print(chinese_remainder([(3, 29), (5, 37), (7, 43)]))