import opcodes
from CONVERTME import int_to_bin, bin_to_int
from main import progCount
from main import regData
from RF import rf
from PC import pc

class ee:

    def execute(instruction):
        if instruction[0:5] in opcodes.op_codes_F:
            progCount.pc+=1
            return True, progCount.pc                 # needs to be taken care of, what index to return when halt is encountered
        else:
            # need to implement the rest of the opcodes individually w.r.t. their respective instruction and how to execute them
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