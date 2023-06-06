def dec_to_bin_FI(decimal): # TAKES IN DECIMAL INPUT GIVES OUT BINARY OUTPUT
     # DECIMAL TO BINARY CONVERSION

    # Separating the whole number and fractional part of the decimal
    whole_num = int(decimal)
    fractional_num = decimal - whole_num

    # whole number part to binary
    bin_whole = bin(whole_num)[2:]

    # fractional part to binary
    bin_fractional = ''
    while fractional_num != 0:
        fractional_num = fractional_num * 2
        bit = int(fractional_num)
        bin_fractional += str(bit)
        fractional_num -= bit

    # Combine the whole number and fractional part
    binary = bin_whole + '.' + bin_fractional
    #print("bin",binary)
    return binary

def findM_FI(decimal): # TAKES IN DECIMAL INPUT GIVES OUT THE MANTISAA OD THAT DECIMAL INPUT
    binary = dec_to_bin_FI(decimal)

    # findinf position of 1 and the dot
    dotref = binary.find(".")
    oneref = binary.find("1")
    if oneref > dotref:
        binary = binary.replace(".","")
        oneref -= 1
        dotref -= 1
    elif oneref < dotref:
        binary = binary.replace(".","")
        dotref -= 1
    mantissa = binary[oneref+1:]
    M = mantissa[:5]

    if len(M) == 0:
        M = M + "00000"
    if len(M) == 1:
        M = M + "0000"
    if len(M) == 2:
        M = M + "000"
    if len(M) == 3:
        M = M + "00"
    if len(M) == 4:
        M = M + "0"
    if len(M) >= 5:
        pass

    # print("the mantissa is",M)
    return M

def findE_FI(decimal): # TAKES DECIMAL INPUT AND GIVES OUT EXPONENT (IEEE) FOR IT AS OUTPUT
    binary = dec_to_bin_FI(decimal)

    dotref = binary.find(".")
    oneref = binary.find("1")

    # calculating the exponent(E)
    if binary[0] == "0":
        exponent = dotref - oneref 
    if binary[0] == "1":
        exponent = dotref - oneref -1

    # print("exponent without bias 3 =",exponent)
    E = exponent + 3
    # print("exponent with bias 3 =",E)
    E = bin(E)[2:]

    if len(E) == 1:
        E = "00" + E
    if len(E) == 2:
        E = "0" + E
    if len(E) > 3:
        return("exponent overflow")
    # print("bin E",E)
    
    return E

def findIEEE_FI(decimal): # TAKES IN DECIMAL INPUT ANF GIVES OUT ITS 8 BIT ieee REPRESENTATION

    M = findM_FI(decimal)
    E = findE_FI(decimal)
    IEEE = E+M
    return IEEE

# decimal = float(input())
# IEEE = findIEEE_FI(decimal)
# print(IEEE)

def findE_IF(IEEE): # TAKES IN IEEE FORM AND GIVES OUT THE EXPONENT
    E = IEEE[:3]
    E = int(E,2)
    E = E - 3
    #print(E)
    return E
    

def findbin_IF(IEEE): # TAKES IEEE FORM AND GIVES OUT THE BINARY FORM
    E = findE_IF(IEEE)
    M = IEEE[3:]
    P = "1."+M
    P = "00000"+P
    #print(P)
    dotref = P.find(".")
    P = P[:dotref]+P[dotref+1:]
    #print(dotref)
    dotref = dotref + E
    #print(dotref)
    #print(P,"hehe")
    if IEEE[0] == "1":
        P = P[:dotref]+"."+P[dotref:]
    if IEEE[0] == "0":
        P = P[:dotref]+"."+P[dotref:]
    
    ##print(P)
    binval = float(P)
    binval = str(P)
    #print(binval)
    return binval

def bin_to_dec_IF(IEEE): # TAKES THE IEEE FORM AND GIVES OUT THE DECIMAL FORM
    binval = findbin_IF(IEEE)
    dotref = binval.find(".")
    fracpart = binval[dotref+1:]
    wholepart = binval[:dotref]
    #print(wholepart,fracpart)

    decwholepart = int(wholepart,2)
    #print(decwholepart)

    decfracpart= 0
    power = -1

    for digit in fracpart:
        decfracpart += int(digit) * (2 ** power)
        power -= 1
    #print(decfracpart)

    decima = float(decwholepart)+float(decfracpart)
    return str(decima)

# dec = bin_to_dec_IF(IEEE)

# print(dec)

def int_to_bin(integer):
    # DECIMAL TO BINARY CONVERSION 
    binary = bin(integer)[2:]
    return binary

def bin_to_int(binstr):
    # BINARY TO DECIMAL CONVERSION
    decimal = int(binstr,2)
    return decimal


