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
    #print("bin",binary)

    exponent = -1
    for i in binary:
        if i != ".":
            exponent = exponent + 1
        else:
            break

    bias = 3
    exponent = exponent + bias
    #print("E",exponent)
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

    return E + M

def IEEE_to_Floating(EM):

    E = EM[:3]
    M = EM[3:]

    exponent = int(E,2)
    print(exponent)


    return decimal




decimal = float(input("Enter a floating-point number: "))
IEEE = Floating_to_IEEE(decimal)
print(IEEE)
decimalagain = IEEE_to_Floating(IEEE)
print(decimalagain)
