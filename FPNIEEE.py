def Floating_to_IEEE(decimal):
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
    print("bin",binary)

    #BINARY completed here.
    

    exponent = -1
    for i in binary:
        if i != ".":
            exponent = exponent + 1
        else:
            break

    bias = 3
    exponent = exponent + bias
    print("E",exponent)
    E = bin(exponent)[2:]

    if len(E) == 1:
        E = "00" + E
    if len(E) == 2:
        E = "0" + E
    if len(E) > 3:
        return("exponent overflow")
    #print("E",E)

    # To print P
    binary_list = list(binary)
    binary_list.remove(".")
    binary_list.insert(1, ".")
    P = "".join(binary_list)

    #print("P",P)

    mantissa = binary_list[2:7]
    M = "".join(mantissa)

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

def IEEE_to_Floating(EM):

    if EM.isdigit() == False:
        return "expected an IEEE format"
    else: 
        E = EM[:3]
        M = EM[3:]

        exponent = int(E,2)
        exponent = exponent - 3
        print(exponent)

        P = "1." + EM[3:]
        print(P)

        Plist = list(P)
        Plist.remove(".")
        
        Plist.insert(exponent+1,".")
        binary = "".join(Plist)
        print(binary)

        point = binary.find('.')

        if point == -1:
            point = len(binary)

        intDecimal = 0
        fracDecimal = 0
        twos = 1

        for i in range(point-1, -1, -1):
            intDecimal += ((ord(binary[i]) - ord('0')) * twos)
            twos *= 2

        twos = 2

        for i in range(point + 1, len(binary)):
            fracDecimal += ((ord(binary[i]) - ord('0')) / twos)
            twos *= 2.0

        decimal = intDecimal + fracDecimal

        return decimal




decimal = float(input("Enter a floating-point number: "))
IEEE = Floating_to_IEEE(decimal)
print(IEEE)
decimalagain = IEEE_to_Floating(IEEE)
print(decimalagain)
