# how many decimal digits till we take the frac to
# for whole numbers like 4,5 etc nothing is getting saved in binfractional
# max minimum value
decimal = float(input())

def decimal_to_binary(decimal):

    # separating  two sides of decimal.
    wholenum = int(decimal)
    fractionalnum = decimal - wholenum

    binwhole = bin(wholenum)[2:]

    binfractional = ''
    while fractionalnum != 0:
        fractionalnum = fractionalnum*2
        bit = int(fractionalnum)
        binfractional += str(bit)
        fractionalnum -= bit

    binary = binwhole + '.' + binfractional

    return binary, binwhole,binfractional     # i am not inting them since 1001.001 me frac part 1 hojaega instead of 001


binary, binwhole, binfractional = decimal_to_binary(decimal)
print(binary, binwhole, binfractional)


exponent = -1
for i in binary:
    if i != ".":
        exponent = exponent + 1
    else:
        break
bias = 3
exponent = exponent + bias
E = bin(exponent)[2:]
print(E)

# to print P
binarylist = list(binary)
binarylist.remove(".")
binarylist.insert(1,".")
P = "".join(binarylist)
print(P)

mantissa = binarylist[2:7]
M = "".join(mantissa)
print(M)

finale = E+M
print(E+M)





