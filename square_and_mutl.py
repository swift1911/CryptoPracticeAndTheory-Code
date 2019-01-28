
def square_and_multiply(x,c,n):
    binary=[]
    while c!=0:
        binary.append(c%2)
        c=c//2
    z=1
    binary.reverse()
    for i in binary:
        z=(z*z)%n
        if i==1:
            z=(z*x)%n
    return z


if __name__ == "__main__":
    print(square_and_multiply(9726,3533,11413))