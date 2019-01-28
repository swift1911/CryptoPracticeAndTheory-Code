def hill_en(message, key, decrypt = False):
    from math import sqrt
    n = int(sqrt(len(key)))
    if n * n != len(key):
        raise Exception("Invalid key length, should be square-root-able like")

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # print "[ALPHA LENGTH]: ", len(alpha)
    tonum = dict([(alpha[i], i * 1) for i in range(len(alpha))])

    # Construct our key matrix
    keylist = []
    for a in key:
        keylist.append(tonum[a])

    keymatrix = [] 
    for i in range(n):
        keymatrix.append(keylist[i * n : i * n + n])

    from numpy import matrix
    from numpy import linalg

    keymatrix = matrix(keymatrix).round().T

    if decrypt:
        determinant = linalg.det(keymatrix).round()
        print "[DETERMINANT]", determinant
        if determinant == 0:
            raise Exception("Determinant ZERO, CHANGE THE KEY!")
        elif determinant % len(alpha) == 0:
            raise Exception("Determinant divisible by ALPHA LENGTH, CHANGE THE KEY!")

        inverse = []
        keymatrix =  matrix(keymatrix.getI() * determinant).round()

        invdeterminant = 0
        for i in range(10000):
            if (determinant * i % len(alpha)) == 1:
                invdeterminant = i
                break

        print "[INVERTED DETERMINANT]", invdeterminant

        for row in keymatrix.getA() * invdeterminant:
            newrow = []
            for i in row:
                newrow.append( i.round() % len(alpha) )
            inverse.append(newrow)
        
        keymatrix = matrix(inverse)

        # print "DECIPHERING: ", message
    else:
    #   print "[ENCIPHERING]: ", message
        pass

    print "[MATRIX]\n", keymatrix

    out = ''
    for i in range(len(message) / n):
        lst = matrix( [[tonum[a]] for a in message[i * n:i * n + n]] )
        result = keymatrix * lst
        out += ''.join([alpha[int(result.A[j][0]) % len(alpha)] for j in range(len(result))])
    
    return out

if __name__ == "__main__": 
    key = "BERLXPMCJ"
    msg = "thanksgiving"
    cipherText = hill(msg, key)
    print(cipherText)
    print "CIPHERED TEXT: |%s|\n" % cipherText
    decipherText = hill(cipherText, key, True)
    print "DECIPHERED TEXT: |%s|\n" % decipherText
    if( msg == decipherText ):
        print "CORRECT"
    else:
        print "INCORRECT"