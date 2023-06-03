import opcodes
from CONVERTME import int_to_bin, bin_to_int
from main import progCount
from main import regData
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


            #------------------------type D-------------------------------
            if instruction[0:5] in opcodes.op_codes_D:
                workingReg = bin_to_int(instruction[6:9])
                workingMemAddr = int(instruction[9:16])

                if instruction[0:5] == '00100':
                    value = mem.fetchData(workingMemAddr)
                    rf.writeData(workingReg, value)
                    temp_pc = progCount + 1
                    return False, temp_pc
                
                elif instruction[0:5] == '00101':
                    value = rf.fetchData(workingReg)
                    mem.writeData(workingMemAddr, value)
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
