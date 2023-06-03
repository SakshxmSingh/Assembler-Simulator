import opcodes
from CONVERTME import int_to_bin, bin_to_int
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
                opreg1 = instruction[10:13]
                opreg2 = instruction[13:16]
                destreg = instruction[7:10]

                
                # for addition
                if instruction[0:5] == '00000':
                    temp = bin_to_int(regData.registers[opreg1]) + bin_to_int(regData.registers[opreg2]) #need to set for overflow flags and errors, but basic structure gonna be like this
                    temp = int_to_bin(temp)

                    if len(temp) > 16:
                        # set of flags regarding overflow

                        pass

                    elif len(temp) < 16:
                        temp = temp.zfill(16)
                    
                    regData.registers[destreg] = temp
                    temp_pc = progCount.pc+1
                    return False, temp_pc

            #------------------------type C-------------------------------
            if instruction[0:5] in opcodes.op_codes_C:
                opreg1 = opcodes.regs[instruction[10:13]]
                opreg2 = opcodes.regs[instruction[13:16]]

                if instruction[0:5] == '00011':
                    value = regData.fetchData[opreg2]
                    regData.writeData[opreg1, value]
                    temp_pc = progCount + 1
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
                    temp_pc = progCount + 1
                    return False, temp_pc


                elif instruction[0:5] == '01101':
                    value = regData.fetchData(opreg2)
                    for i in range(16):
                        if value[i] == '0':
                            value[i] = '1'
                        else:
                            value[i] = '0'
                    regData.writeData(opreg2, value)
                    temp_pc = progCount + 1
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
                    temp_pc = progCount + 1
                    return False, temp_pc

                elif instruction[0:5] == '10010':
                    reg1Value = regData.fetchData(opreg1)
                    reg2Value = regData.fetchData(opreg2)
                    regData.writeData(opreg1, reg2Value)
                    regData.writeData(opreg2, reg1Value)
                    temp_pc = progCount + 1
                    return False, temp_pc

            #------------------------type D-------------------------------
            if instruction[0:5] in opcodes.op_codes_D:
                workingReg = opcodes.regs[instruction[6:9]]
                workingMemAddr = bin_to_int(instruction[9:16])

                if instruction[0:5] == '00100':
                    value = memData.fetchData(workingMemAddr)
                    regData.writeData(workingReg, value)
                    temp_pc = progCount + 1
                    return False, temp_pc 
                
                elif instruction[0:5] == '00101':
                    value = regData.fetchData(workingReg)
                    memData.writeData(workingMemAddr, value)
                    temp_pc = progCount + 1
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
