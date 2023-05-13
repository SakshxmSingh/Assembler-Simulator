op_codes_A = {
    'add': '00000',
    'sub': '00001',
    'mul': '00110',
    'xor': '01010',
    'or': '01011',
    'and': '01100'
}

op_codes_B = {
    'mov': '00010',
    'rs': '01000',
    'ls': '01101',
}

op_codes_C = {
    'mov': '00011',
    'div': '00111',
    'not': '01001',
    'cmp': '01110'
}

op_codes_D = {
    'ld': '00100',
    'st': '00101'
}

op_codes_E = {
    'jmp': '01111',
    'jlt': '11100',
    'jgt': '11101',
    'je': '11111'
}

op_codes_F = {
    'hlt': '11010'
}

regs = {
    'R0': '000',
    'R1': '001',
    'R2': '010',
    'R3': '011',
    'R4': '100',
    'R5': '101',
    'R6': '110',
    'FLAGS': '111'
}

f_input = open("Assembler/read.txt", 'r+')
f_output = open("Assembler/write.txt", 'a+')

f_output.seek(0)
f_output.truncate()

# welcome message
f_output.write('-------------\n')

f_output.write(
    "Welcome user.\nWelcome to a programme put into existence by the combined forces of users 2022434, 2022451, 2022351, 2022466.\n")
f_output.write(
    '-------------------------------------------------------------------------------------------------------------\n')
f_output.write('The programme has taken in your commands.\n')
f_output.write('-----------------------------------------\n')

prog_count = 0

labels = {}

output_list = []  # to store all the correct lines in the initial program
input_list = f_input.readlines()

if len(input_list) == 0:
    assert 0 == 1, "No instructions were provided"
elif len(input_list) > 127:
    assert 0 == 1, "Instruction(memory) limit exceeded"
else:
    f_output.write("The following output was generated.\n")
    f_output.write('-----------------------------------\n')

halt_flag = False
var_count = 0
for i in range(len(input_list)):
    input_list[i] = input_list[i].split()

    if len(input_list[i]) == 0:   #ignore empty lines
        continue

    if input_list[i][0][-1] == ':':
        labels.update(
            {input_list[i][0][:len(input_list[i][0]) - 1]: bin(prog_count)[2:]})
    if input_list[i][0] =='var' and prog_count!=0:
        assert 0 == 1, f"Variables not declared / declared incorrectly at the beginning (line {i+1})"
    if input_list[i][0] != 'var':
        prog_count += 1


vars = {}
var_index = prog_count


def label_read(line):
    global vars
    global var_index

    # type A, error handling done :)
    if line[0] in op_codes_A:
        if (line[1][0] == "$") or (line[2][0] == "$") or (line[3][0] == "$"):
            assert 0 == 1, f"This assembler does not support operations on immediate values directly. (line {input_list.index(line)+1})"
        elif line[1] not in regs or line[2] not in regs or line[3] not in regs:
            assert 0 == 1, f"Invalid register name or some typo in register name (line {input_list.index(line)+1})"
        if len(line) > 4:
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 4:
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        string = op_codes_A[line[0]] + '00' + \
            (regs[line[1]] + regs[line[2]] + regs[line[3]])
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + \
            " Type A" + " " + line[0] + " " + \
            line[1] + " " + line[2] + " " + line[3]
        output_list.append(string)

    # type B, error handling done :)
    # this sorts the mov problem by checking reg or $imm
    elif (line[0] in op_codes_B):
        
        if len(line) > 3:
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if (line[2][0] != "$" ) and (line[2][1:].isdigit()):
            assert 0 == 1, f"Syntax Error: Wrong format for immediate values used. (line {input_list.index(line)+1})"
        if line[2][1:].isdigit() == False:
            assert 0 == 1, f"Immediate value not valid (line {input_list.index(line)+1})"
        binary = bin(int(line[2][1:])).replace("0b", "")
        # I have ignored the case where they give negative number as input.
        if len(binary) > 7:
            assert 0 == 1, f"Illegal immediate values(more than 7 bits) (line {input_list.index(line)+1})"

        else:
            if len(binary) == 7:
                pass
            elif len(binary) < 7:
                binary = (7 - len(binary))*"0" + binary

            if line[1] not in regs:
                assert 0 == 1, f"Invalid register name or some typo in register name (line {input_list.index(line)+1})"
            string = op_codes_B[line[0]] + '0' + (regs[line[1]]) + binary
            string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + \
                string[12:16] + " Type B" + " " + \
                line[0] + " " + line[1] + " " + line[2]
            output_list.append(string)

    # type C
    elif line[0] in op_codes_C:
        if len(line) > 3:
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[1] not in regs or line[2] not in regs:
            assert 0 == 1, f"Invalid register name or some typo in register name (line {input_list.index(line)+1})"
        string = op_codes_C[line[0]] + '0'*5 + (regs[line[1]] + regs[line[2]])
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + \
            string[12:16] + " Type C" + " " + \
            line[0] + " " + line[1] + " " + line[2]
        output_list.append(string)

    # type D, needs to be tested
    elif line[0] == 'var':
        if len(line) !=2:
            assert 0 == 1, f"Syntax Error (line {input_list.index(line)+1})"
        # need to convert the entire input into a 2d list, tabhi vars can be indexed and accessed easily
        if (line[1] not in vars):
            vars.update({line[1]: bin(var_index)[2:]})
        else:
            assert 0 == 1, f"Variable already exists (line {input_list.index(line)+1})"

        if len(vars[line[1]]) == 7:
            pass
        elif len(vars[line[1]]) < 7:
            vars[line[1]] = (7 - len(vars[line[1]]))*"0" + vars[line[1]]
        var_index += 1

    elif line[0] in op_codes_D:
        if len(line) > 3:
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[2] not in vars:
            assert 0 == 1, f"Variable not defined (line {input_list.index(line)+1})"
        elif line[2] in vars:
            if line[1] not in regs:
                assert 0 == 1, f"Invalid register name or some typo in register name (line {input_list.index(line)+1})"
            string = op_codes_D[line[0]] + '0' + regs[line[1]] + vars[line[2]]
            string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + \
                string[12:16] + " Type D" + " " + \
                line[0] + " " + line[1] + " " + line[2]
            output_list.append(string)

    # type E, handle the error if label was never initialised
    elif line[0] in op_codes_E:
        if len(line) > 2:
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 2:
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[1] not in labels:
            assert 0 == 1, f"Label not defined (line {input_list.index(line)+1})"
        mem_addr = labels[line[1]]
        string = op_codes_E[line[0]] + '0'*(4 + 7 - len(mem_addr)) + mem_addr
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + \
            '_' + string[12:16] + " Type E" + " " + line[0] + " " + line[1]
        output_list.append(string)

    # type F, no need to test i hope
    elif line[0] == 'hlt':
        if len(line) !=1:
            assert 0 == 1,f"Syntax Error (line {input_list.index(line)+1})"
        string = op_codes_F[line[0]] + '0'*11
        string = string[0:4] + '_' + string[4:8] + '_' + \
            string[8:12] + '_' + string[12:16] + " Type F" + " " + line[0]
        output_list.append(string)

    else:
        assert 0 == 1,f"Invalid opcode name or some typo in opcode name (line {input_list.index(line)+1})"


def output_func(line):
    global vars
    global var_index

    # type A, register error handling
    if line[0] in op_codes_A:

        if (line[1][0] == "$") or (line[2][0] == "$") or (line[3][0] == "$"):
            assert 0 == 1, f"This assembler does not support operations on immediate values directly. (line {input_list.index(line)+1})"
        if line[1] not in regs or line[2] not in regs or line[3] not in regs:
            assert 0 == 1, f"Invalid register name or some typo in register name (line {input_list.index(line)+1})"
        if len(line) > 4:
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 4:
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        string = op_codes_A[line[0]] + '00' + \
            (regs[line[1]] + regs[line[2]] + regs[line[3]])
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + \
            " Type A" + " " + line[0] + " " + \
            line[1] + " " + line[2] + " " + line[3]
        output_list.append(string)

    # type B, error handling done :)
    # this sorts the mov problem by checking reg or $imm
    elif (line[0] in op_codes_B):

        if len(line) > 3:
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if (line[2][0] != "$" ) and (line[2][1:].isdigit()):
            assert 0 == 1, f"Syntax Error: Wrong format for immediate values used. (line {input_list.index(line)+1})"
        if line[2][1:].isdigit() ==False:
            assert 0 == 1,f"Immediate value not valid (line {input_list.index(line)+1})"
        binary = bin(int(line[2][1:])).replace("0b", "")
        # I have ignored the case where they give negative number as input.
        if len(binary) > 7:
            assert 0 == 1, f"Illegal immediate values(more than 7 bits) (line {input_list.index(line)+1})"

        else:
            if len(binary) == 7:
                pass
            elif len(binary) < 7:
                binary = (7 - len(binary))*"0" + binary

            if line[1] not in regs:
                assert 0 == 1, f"Invalid register name or some typo in register name (line {input_list.index(line)+1})"
            string = op_codes_B[line[0]] + '0' + (regs[line[1]]) + binary
            string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + \
                string[12:16] + " Type B" + " " + \
                line[0] + " " + line[1] + " " + line[2]
            output_list.append(string)

    # type C
    elif line[0] in op_codes_C:
        if len(line) > 3:
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[1] not in regs or line[2] not in regs:
            assert 0 == 1, f"Invalid register name or some typo in register name (line {input_list.index(line)+1})"
        string = op_codes_C[line[0]] + '0'*5 + (regs[line[1]] + regs[line[2]])
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + \
            string[12:16] + " Type C" + " " + \
            line[0] + " " + line[1] + " " + line[2]
        output_list.append(string)

    # type D, needs to be tested
    elif line[0] == 'var':
        if len(line) !=2:
            assert 0 == 1,f"Syntax Error (line {input_list.index(line)+1})"
        # need to convert the entire input into a 2d list, tabhi vars can be indexed and accessed easily
        if (line[1] not in vars):
            vars.update({line[1]: bin(var_index)[2:]})
        else:
            assert 0 == 1, f"Variable already exists (line {input_list.index(line)+1})"

        if len(vars[line[1]]) == 7:
            pass
        elif len(vars[line[1]]) < 7:
            vars[line[1]] = (7 - len(vars[line[1]]))*"0" + vars[line[1]]
        var_index += 1

    elif line[0] in op_codes_D:
        if len(line) > 3:
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[2] not in vars:
            assert 0 == 1, f"Variable not defined (line {input_list.index(line)+1})"
        elif line[2] in vars:
            if line[1] not in regs:
                assert 0 == 1, f"Invalid register name or some typo in register name (line {input_list.index(line)+1})"
            string = op_codes_D[line[0]] + '0' + regs[line[1]] + vars[line[2]]
            string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + \
                string[12:16] + " Type D" + " " + \
                line[0] + " " + line[1] + " " + line[2]
            output_list.append(string)

    # type E, handle the error if label was never initialised- hey handled :)
    elif line[0] in op_codes_E:
        if len(line) > 2:
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 2:
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[1] not in labels:
            assert 0 == 1, f"Label not defined (line {input_list.index(line)+1})"
        mem_addr = labels[line[1]]
        string = op_codes_E[line[0]] + '0'*(4 + 7 - len(mem_addr)) + mem_addr
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + \
            '_' + string[12:16] + " Type E" + " " + line[0] + " " + line[1]
        output_list.append(string)

    # type F, no need to test i hope
    elif line[0] == 'hlt':
        if len(line) !=1:
            assert 0 == 1,f"Syntax Error (line {input_list.index(line)+1})"
        string = op_codes_F[line[0]] + '0'*11
        string = string[0:4] + '_' + string[4:8] + '_' + \
            string[8:12] + '_' + string[12:16] + " Type F" + " " + line[0]
        output_list.append(string)

    # labels
    elif line[0][-1] == ':':
        label_read(line[1:])

    else:
        assert 0 == 1,f"Invalid opcode name or some typo in opcode name (line {input_list.index(line)+1})"


# the only condition under which the program proceeds further, hlt at the end

for i in range(len(input_list)-1):
    if 'hlt' in input_list[i]:
        # throws off execution of the program, hlt not at the end
        assert halt_flag == True, "'hlt' not being used as the last instruction"

if 'hlt' in input_list[len(input_list)-1]:
    halt_flag = True

if halt_flag:
    for line in input_list:
        if line == []:  #handling empty line
            pass    
        else:
            output_func(line)
else:
    # put a suitable error in here
    assert halt_flag == True, "'hlt' statement is absent"

for i in output_list:
    f_output.write(i+'\n')
f_output.write('-------------------------------------------------------------------------------------------------------------\n')
