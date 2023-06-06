import opcodes
from CONVERTME import int_to_bin, bin_to_int, bin_to_dec_IF, findIEEE_FI
from main import progCount
from main import regData
from main import memData
from RF import rf
from PC import pc
from MEM import mem

class ee:

    def execute(instruction):

        #type F
        if instruction[0:5] in opcodes.op_codes_F:
            temp_pc = progCount.pc+1
            return True, temp_pc                 # needs to be taken care of, what index to return when halt is encountered
        else:
            # need to implement the rest of the opcodes individually w.r.t. their respective instruction and how to execute them
            
            #-----------------------type A--------------------------------
            if instruction[0:5] in opcodes.op_codes_A:
                regA = instruction[10:13]
                regB = instruction[13:16]
                destination = instruction[7:10]

                
                # for addition
                if instruction[0:5] == '00000':
                    IntegerSum = bin_to_int((regData.registers[regA])) + (bin_to_int(regData.registers[regB])) 
                    BinarySum = int_to_bin(IntegerSum)
                    
                    temp_pc = progCount.pc+1

                    if len(BinarySum) > 16: #overflow
                        regData.registers['FLAGS'][-4] = '1'
                        regData.writeData(opcodes.regs[destination], '0000000000000000')
                        return False, temp_pc
    
                    BinarySum = BinarySum.zfill(16)
                    regData.writeData(opcodes.regs[destination], BinarySum)
                    
                    
                    return False, temp_pc
                
                # for subtraction
                if instruction[0:5] == '00001':
                    IntegerDifference = bin_to_int((regData.registers[regA])) - (bin_to_int(regData.registers[regB]))
                    temp_pc = progCount.pc+1

                    if IntegerDifference < 0:
                        regData.registers['FLAGS'][-4] = '1'
                        regData.writeData(opcodes.regs[destination], '0000000000000000')
                        return False, temp_pc

                    BinaryDifference = int_to_bin(IntegerDifference)
                    BinaryDifference = BinaryDifference.zfill(16)
                    regData.writeData(opcodes.regs[destination], BinaryDifference)
                    

                    return False, temp_pc

                # for multiplication
                if instruction[0:5] == '00110':
                    IntegerMult = bin_to_int((regData.registers[regA])) * (bin_to_int(regData.registers[regB])) 
                    BinaryMult = int_to_bin(IntegerMult)

                    temp_pc = progCount.pc+1

                    if len(BinaryMult) > 16: #overflow
                        regData.registers['FLAGS'][-4] = '1'
                        regData.writeData(opcodes.regs[destination], '0000000000000000')
                        return False, temp_pc

    
                    BinaryMult= BinaryMult.zfill(16)
                    regData.writeData(opcodes.regs[destination], BinaryMult)
                    
                    
                    return False, temp_pc
                
                # for bitwise XOR | working, has been tested
                if instruction[0:5] == '01010':
                    BinaryXOR=bin_to_int(regData.registers[regA]) ^ bin_to_int(regData.registers[regB])
                    BinaryXOR=str(int_to_bin(BinaryXOR))
                    temp_pc = progCount.pc+1

                    if len(BinaryXOR) > 16: #overflow
                        regData.registers['FLAGS'][-4] = '1'
                        regData.writeData(opcodes.regs[destination], '0000000000000000')
                        return False, temp_pc
    
                    BinaryXOR= BinaryXOR.zfill(16)
                    regData.writeData(opcodes.regs[destination], BinaryXOR)
                    
                    
                    return False, temp_pc
                
                # for bitwise OR | working, has been tested
                if instruction[0:5] == '01011':
                    BinaryOR=bin_to_int(regData.registers[regA]) | bin_to_int(regData.registers[regB])
                    BinaryOR=str(int_to_bin(BinaryXOR))
                    temp_pc = progCount.pc+1

                    if len(BinaryOR) > 16: #overflow
                        regData.registers['FLAGS'][-4] = '1'
                        regData.writeData(opcodes.regs[destination], '0000000000000000')
                        return False, temp_pc
    
                    BinaryOR= BinaryOR.zfill(16)
                    regData.writeData(opcodes.regs[destination], BinaryOR)

                    return False, temp_pc
                
                # for bitwise AND
                if instruction[0:5] == '01100':
                    BinaryAND=bin_to_int(regData.registers[regA]) & bin_to_int(regData.registers[regB])
                    BinaryAND=str(int_to_bin(BinaryXOR))
                    temp_pc = progCount.pc+1

                    if len(BinaryAND) > 16: #overflow
                        regData.registers['FLAGS'][-4] = '1'
                        regData.writeData(opcodes.regs[destination], '0000000000000000')
                        return False, temp_pc

    
                    BinaryAND= BinaryAND.zfill(16)
                    regData.writeData(opcodes.regs[destination], BinaryAND)
                    
                    
                    return False, temp_pc
                
                # for fraction addition
                if instruction[0:5]=='10000':
                    FractionSum = bin_to_dec_IF(regData.registers[regA][8:]) + bin_to_dec_IF(regData.registers[regB][8:])
                    temp_pc = progCount.pc+1

                    if FractionSum > 15.75:
                        regData.registers['FLAGS'][-4] = '1'
                        regData.writeData(opcodes.regs[destination], '0000000000000000')
                        return False, temp_pc

                    BinarySum = findIEEE_FI(FractionSum)
                    BinarySum = BinarySum.zfill(16)
                    regData.writeData(opcodes.regs[destination], BinarySum)
                    return False, temp_pc
                
                # for fraction subtraction
                if instruction[0:5]=='10001':
                    FractionDifference = bin_to_dec_IF(regData.registers[regA][8:]) - bin_to_dec_IF(regData.registers[regB][8:])
                    temp_pc = progCount.pc+1

                    if FractionDifference < 0.25 and FractionDifference!=0:
                        regData.registers['FLAGS'][-4] = '1'
                        regData.writeData(opcodes.regs[destination], '0000000000000000')
                        return False, temp_pc

                    BinaryDifference = findIEEE_FI(FractionDifference)
                    BinaryDifference = BinaryDifference.zfill(16)
                    regData.writeData(opcodes.regs[destination], BinaryDifference)
                    return False, temp_pc
                

             #-----------------------type B--------------------------------
            if instruction[0:5] in opcodes.op_codes_B:
                regA = instruction[6:9]
                Imm=instruction[9:16]

                # for move immediate // working, has been tested
                if instruction[0:5]=='00010':

                    Imm=(Imm).zfill(16)#this zfills thingy actually works?
                    regData.writeData(opcodes.regs[regA],Imm)
                    temp_pc = progCount.pc+1
                    return False, temp_pc
                
                #movf
                if instruction[0:5]=='10010':
                    Imm=instruction[8:16]
                    Imm=Imm.zfill(16)
                    regData.writeData(opcodes.regs[regA],Imm)
                    temp_pc = progCount.pc+1
                    return False, temp_pc

                # for right shift // tested, working
                if instruction[0:5]=='01000':

                    Imm=bin_to_int(Imm) 
                    temp=regData.registers[regA]
                    temp='0'*Imm+temp[:-Imm]
                    temp=temp.zfill(16)# not really required, but still- no harm in being careful
                    regData.writeData(opcodes.regs[regA],temp)
                    temp_pc = progCount.pc+1
                    return False, temp_pc
                
                # for left shift // tested, working
                if instruction[0:5]=='01001':

                    Imm=bin_to_int(Imm) 
                    temp=regData.registers[regA]
                    temp=temp[Imm:]+'0'*Imm
                    temp=temp.zfill(16)#this zfills thingy actually works?
                    regData.writeData(opcodes.regs[regA],temp)
                    temp_pc = progCount.pc+1
                    return False, temp_pc
                
                # for right rotate | tested, working
                if instruction[0:5]=='10110':

                    Imm=bin_to_int(Imm)
                    temp=regData.registers[regA]
                    bits=regData.registers[regA][-Imm:]
                    temp=bits+temp[:-Imm]
                    temp=temp.zfill(16)#this zfills thingy actually works?
                    regData.writeData(opcodes.regs[regA],temp)
                    temp_pc = progCount.pc+1
                    return False, temp_pc

                # for left rotate| tested, working
                if instruction[0:5]=='10111':

                    Imm=bin_to_int(Imm)
                    temp=regData.registers[regA]
                    bits=regData.registers[regA][:Imm]
                    temp=temp[Imm:]+bits
                    temp=temp.zfill(16)#this zfills thingy actually works?
                    regData.writeData(opcodes.regs[regA],temp)
                    temp_pc = progCount.pc+1
                    return False, temp_pc


            #------------------------type C-------------------------------
            if instruction[0:5] in opcodes.op_codes_C:
                opreg1 = opcodes.regs[instruction[10:13]]
                opreg2 = opcodes.regs[instruction[13:16]]

                if instruction[0:5] == '00011':
                    value = regData.fetchData(opreg2)
                    regData.writeData(opreg1, value)
                    temp_pc = progCount.pc + 1
                    return False, temp_pc

                elif instruction[0:5] == '00111':
                    reg1Value = bin_to_int(regData.fetchData[opreg1])
                    reg2Value = bin_to_int(regData.fetchData[opreg2])
                    if reg2Value == 0:
                        regData.registers['FLAGS'][12] = '1'
                        regData.writeData('R0', '0000000000000000')
                        regData.writeData('R1', '0000000000000000')
                    
                    else:
                        regData.registers['FLAGS'][12] = '0'
                        quotient = int(reg1Value / reg2Value)
                        quotient = int_to_bin(quotient)
                        quotient = quotient.zfill(16)
                        remainder = int(reg1Value % reg2Value)
                        remainder = int_to_bin(remainder)
                        remainder = remainder.zfill(16)
                        regData.writeData('R0', quotient)
                        regData.writeData('R1', remainder)
                    temp_pc = progCount.pc + 1
                    return False, temp_pc


                elif instruction[0:5] == '01101':
                    value = regData.fetchData(opreg2)
                    for i in range(16):
                        if value[i] == '0':
                            value[i] = '1'
                        else:
                            value[i] = '0'
                    regData.writeData(opreg1, value)
                    temp_pc = progCount.pc + 1
                    return False, temp_pc
                
                elif instruction[0:5] == '01110':
                    reg1Value = bin_to_int(regData.fetchData(opreg1))
                    reg2Value = bin_to_int(regData.fetchData(opreg2))
                    if reg1Value > reg2Value:
                        regData.registers['FLAGS'][14] = '1'
                    elif reg1Value < reg2Value:
                        regData.registers['FLAGS'][13] = '1'
                    elif reg1Value == reg2Value:
                        regData.registers['FLAGS'][15] = '1'
                    temp_pc = progCount.pc + 1
                    return False, temp_pc

                elif instruction[0:5] == '10101':
                    reg1Value = regData.fetchData(opreg1)
                    reg2Value = regData.fetchData(opreg2)
                    regData.writeData(opreg1, reg2Value)
                    regData.writeData(opreg2, reg1Value)
                    temp_pc = progCount.pc + 1
                    return False, temp_pc


            #------------------------type D-------------------------------
            if instruction[0:5] in opcodes.op_codes_D:
                workingReg = opcodes.regs[instruction[6:9]]
                workingMemAddr = bin_to_int(instruction[9:16])

                if instruction[0:5] == '00100':
                    value = memData.fetchData(workingMemAddr)
                    regData.writeData(workingReg, value)
                    temp_pc = progCount.pc + 1
                    return False, temp_pc 
                
                elif instruction[0:5] == '00101':
                    value = regData.fetchData(workingReg)
                    memData.writeData(workingMemAddr, value)
                    temp_pc = progCount.pc + 1
                    return False, temp_pc


            #------------------------type E-------------------------------
            if instruction[0:5] in opcodes.op_codes_E:
                destInt = instruction[9:16]

                #jmp
                if instruction[0:5] == '01111':
                    temp_pc = bin_to_int(destInt)
                    return False, temp_pc
                
                #jlt
                elif instruction[0:5] == '11100':
                    if regData.registers['FLAGS'][13] == '1':
                        temp_pc = bin_to_int(destInt)
                        return False, temp_pc
                    
                    else:
                        temp_pc = progCount.pc+1
                        return False, temp_pc

                #jgt
                elif instruction[0:5] == '11101':
                    if regData.registers['FLAGS'][12] == '1':
                        temp_pc = bin_to_int(destInt)
                        return False, temp_pc
                    
                    else:
                        temp_pc = progCount.pc+1
                        return False, temp_pc
                
                #je
                elif instruction[0:5] == '11111':
                    if regData.registers['FLAGS'][14] == '1':
                        temp_pc = bin_to_int(destInt)
                        return False, temp_pc
                    
                    else:
                        temp_pc = progCount.pc+1
                        return False, temp_pc