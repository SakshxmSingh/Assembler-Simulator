def Floating_to_IEEE(decimal):
    if((0.25 <= decimal <= 15.75) or (decimal == 0 ))== False:
        return "Floating point out of range"
    if (decimal == 0 ):
        return "00000000"

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

    #DECIMAL TO BINARY CONVERSION COMPLETE
    
    #CALCULATING THE EXPONENT E, FIRST THREE BITS OF OUR IEEE

    if int(binary[0]) == 1:
        exponent = -1
        for i in binary:
            if i != ".":
                exponent = exponent + 1
            else:
                reference = binary.index(i)
                break

        bias = 3
        exponent = exponent + bias
        E = bin(exponent)[2:]
        #print("E",exponent)

    elif int(binary[0]) == 0:

        exponent = -1
        for i in binary:
            if i != "1":
                exponent = exponent + 1
            else:
                reference = binary.index(i)
                break

        #print(exponent)
        exponent = exponent*-1
        bias = 3
        exponent = exponent + bias        
        E = bin(exponent)[2:]
        #print("E",exponent)

    if len(E) == 1:
        E = "00" + E
    if len(E) == 2:
        E = "0" + E
    if len(E) > 3:
        return("exponent overflow")
    
    #print(E,"E",exponent)
    #print("ref",reference)

    # FINDING MANTISSA
    M = binary[reference+1:reference+6]
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
    #print(M)

    # CASE 1: E is 111
    if int(E) == 111:
        if int(M) == 0:
            return "infinity"
        else:
            return "not a number"
        
    #CASE 2" E is 000
    elif int(E) == 0:
        if int(M) == 0:
            return "00000000"
        else:
            return "not a number"
        
    #CASE 3: E is something betwwen 000 and 111
    else:
        return E + M






decimal = float(input())
IEEE = Floating_to_IEEE(decimal)
print(IEEE)