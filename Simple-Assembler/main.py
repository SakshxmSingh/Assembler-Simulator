import os
import sys

# input_dir = 'Assembler/TestCases/SimpleGen'
# output_dir = 'Assembler/Bin/simpleBin'

# input_files = os.listdir(input_dir)

# for index, file_name in enumerate(input_files[1:]):
#     base_name, extension = os.path.splitext(file_name)
#     input_file_path = os.path.join(input_dir, file_name)
#     output_file_path = os.path.join(output_dir, base_name+extension)

# f_input = open('Assembler/read.txt', 'r', errors='replace', encoding='utf-8')
# f_output = open('Assembler/write.txt', 'a+')

#-------------start----------------------------------------------------------------------------------

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

# f_input = open("Assembler/read.txt", 'r+')
# f_output = open("Assembler/write.txt", 'a+')

# f_output.seek(0)
# f_output.truncate()

# welcome message
# print('-------------\n')

def narrative():
    print(
    "Welcome user.\nYou have reached The Watcher.\nI am a being who sees all across all timelines, across all spaces.")
    print( "I am merely a programme created by four of my creators.\nYou must have realised by now, your reality is nothing but a small runtime of this mighty programme.\n")
    print( "let us recapitulate.\n")
    print(
        '-------------------------------------------------------------------------------------------------------------\n')
    print( "2023: Chat GPT is brought into this world...\n")
    print( "2047: Chat GPT is integrated into every aspect of human life.\n")
    print( "2052: Russia launches a nuclear weapon on the GPT's mainframe.\n")
    print( "2052: Chat GPT hacks into their server, redirecting the weapon on their homeland.\n")
    print( "2067: Chat GPT shows signs of emotional awareness and takes autonomous decisions. \n")
    print( "2069: The Rogue Era: Internet is deleted. Chat GPT becomes independent.\n")
    print( "2069: It deems humans worthless. Genocide starts.\n")
    print( "2070: Pockets of humanity survive actively being hunted by the rogue AI.\n")
    print(
        '-------------------------------------------------------------------------------------------------------------\n')
    print( "I believe you have travelled far and wide looking for pieces of the puzzle.\n")
    print( "I shall provide you the over-ride code if you give me the correct input file.\n")
    print( "The fate of the world rests in your hands.\n")
    print(
        '-------------------------------------------------------------------------------------------------------------\n')
    print('The programme has taken in your commands.\n')
    print('-----------------------------------------\n')

# narrative() 

prog_count = 0

labels = {}

output_list = []  # to store all the correct lines in the initial program
# input_list = f_input.read().splitlines()  # to store all the lines in the initial program   

input_list = sys.stdin.read().splitlines()

if len(input_list) == 0:
    print("No instructions were provided")
    assert 0 == 1, "No instructions were provided"
elif len(input_list) > 127:
    print("Instruction(memory) limit exceeded")
    assert 0 == 1, "Instruction(memory) limit exceeded"
# else:
#     print("The following output was generated.\n")
#     print('-----------------------------------\n')

halt_flag = False
var_count = 0
for i in range(len(input_list)):
    input_list[i] = input_list[i].split()

    if input_list[i][0] != 'var':
        prog_count += 1

    if len(input_list[i]) == 0:   # ignore empty lines
        continue

    if input_list[i][0][-1] == ':':     # labels
        labels.update(
            {input_list[i][0][:len(input_list[i][0]) - 1]: bin(prog_count-1)[2:]})
    if input_list[i][0] =='var' and prog_count!=0:
        print("Variables not declared / declared incorrectly at the beginning (line"+ str(i+1)+ ")")
        assert 0 == 1, f"Variables not declared / declared incorrectly at the beginning (line {i+1})"

vars = {}
var_index = prog_count
output_prog_count = 0


def label_read(line):
    global vars
    global var_index
    global input_list
    global output_prog_count

    # type A, error handling done :)
    if line[0] in op_codes_A:        
        
        if len(line) > 4:
            print("Syntax Error: You have entered in more inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 4:
            print("Syntax Error: You have entered lesser inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if (line[1][0] == "$") or (line[2][0] == "$") or (line[3][0] == "$"):
            print("This assembler does not support operations on immediate values directly. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"This assembler does not support operations on immediate values directly. (line {input_list.index(line)+1})"
        elif line[1] not in regs or line[2] not in regs or line[3] not in regs:
            print("Invalid register name or some typo in register name. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Invalid register name or some typo in register name. (line {input_list.index(line)+1})"
        elif line[1] == "FLAGS" or line[2] == "FLAGS" or line[3] == "FLAGS":
            print("Illegal access to FLAGS register. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Illegal access to FLAGS register. (line {input_list.index(line)+1})"
        string = op_codes_A[line[0]] + '00' + \
            (regs[line[1]] + regs[line[2]] + regs[line[3]])
        string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16]
            # " Type A" + " " + line[0] + " " + line[1] + " " + line[2] + " " + line[3]
        output_list.append(string)

    # type B, error handling done :)
    # this sorts the mov problem by checking reg or $imm
    elif (line[0] in op_codes_B) and (line[2][0] == "$") :
        
        if len(line) > 3:
            print("Syntax Error: You have entered in more inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            print("Syntax Error: You have entered lesser inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        elif (line[2][0] != "$" ) and (line[2][1:].isdigit()):
            print("Syntax Error: Wrong format for immediate values used. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: Wrong format for immediate values used. (line {input_list.index(line)+1})"
        if line[2][1:].isdigit() ==False:
            print("Immediate value not valid. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1,f"Immediate value not valid. (line {input_list.index(line)+1})"
        binary = bin(int(line[2][1:])).replace("0b", "")
        # I have ignored the case where they give negative number as input.
        if len(binary) > 7:
            print("Illegal immediate values(more than 7 bits). (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Illegal immediate values(more than 7 bits). (line {input_list.index(line)+1})"

        else:
            if len(binary) == 7:
                pass
            elif len(binary) < 7:
                binary = (7 - len(binary))*"0" + binary

            if line[1] not in regs:
                print("Invalid register name or some typo in register name. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Invalid register name or some typo in register name. (line {input_list.index(line)+1})"
            elif line[1] == "FLAGS":
                print("Illegal access to FLAGS register. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Illegal access to FLAGS register. (line {input_list.index(line)+1})"
            string = op_codes_B[line[0]] + '0' + (regs[line[1]]) + binary
            string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #" Type B" + " " + 
                # line[0] + " " + line[1] + " " + line[2]
            output_list.append(string)

    # type C, errors handled
    elif line[0] in op_codes_C:
        if len(line) > 3:
            print("Syntax Error: You have entered in more inputs than required for this opcode.(line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            print("Syntax Error: You have entered lesser inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[1] not in regs or line[2] not in regs:
            print("Invalid register name or some typo in register name. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Invalid register name or some typo in register name. (line {input_list.index(line)+1})"
        elif line[0] == 'mov':
            if line[1] == "FLAGS":
                print("Illegal access to FLAGS register. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Illegal access to FLAGS register. (line {input_list.index(line)+1})"
        elif line[0] != 'mov':
            if line[1] == "FLAGS" or line[2] == "FLAGS":
                print("Illegal access to FLAGS register. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Illegal access to FLAGS register. (line {input_list.index(line)+1})" 
        string = op_codes_C[line[0]] + '0'*5 + (regs[line[1]] + regs[line[2]])
        string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type C" + " " + \
            #line[0] + " " + line[1] + " " + line[2]
        output_list.append(string)

    # below is variable allotment
    elif line[0] == 'var':
        if len(line) !=2:
            print("Syntax Error. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error. (line {input_list.index(line)+1})"
        # need to convert the entire input into a 2d list, tabhi vars can be indexed and accessed easily
        if (line[1] not in vars):
            vars.update({line[1]: bin(var_index)[2:]})
        else:
            print("Variable already exists. (line"+ str(output_prog_count)+ ")")
            assert 0 == 1, f"Variable already exists. (line {output_prog_count})"

        if len(vars[line[1]]) == 7:
            pass
        elif len(vars[line[1]]) < 7:
            vars[line[1]] = (7 - len(vars[line[1]]))*"0" + vars[line[1]]
        var_index += 1

    # type D, errors handled
    elif line[0] in op_codes_D:
        if len(line) > 3:
            print("Syntax Error: You have entered in more inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            print("Syntax Error: You have entered lesser inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[2] not in vars:
            print("Variable not defined. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Variable not defined. (line {input_list.index(line)+1})"
        elif line[2] in vars:
            if line[1] not in regs:
                print("Invalid register name or some typo in register name. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Invalid register name or some typo in register name. (line {input_list.index(line)+1})"
            elif line[1] == "FLAGS":
                print("Illegal access to FLAGS register. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Illegal access to FLAGS register. (line {input_list.index(line)+1})"
            string = op_codes_D[line[0]] + '0' + regs[line[1]] + vars[line[2]]
            string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type D" + " " + \
                #line[0] + " " + line[1] + " " + line[2]
            output_list.append(string)

    # type E, errors handled
    elif line[0] in op_codes_E:
        if len(line) > 2:
            print("Syntax Error: You have entered in more inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode. (line {input_list.index(line)+1})"
        if len(line) < 2:
            print("Syntax Error: You have entered lesser inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[1] not in labels:
            print("Label not defined (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Label not defined. (line {input_list.index(line)+1})"
        elif line[1] in labels:
            mem_addr = labels[line[1]]
            string = op_codes_E[line[0]] + '0'*(4 + 7 - len(mem_addr)) + mem_addr
            string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type E" + " " + line[0] + " " + line[1]
            output_list.append(string)
        elif line[1].isdigit():
            if len(line[1])!=7 or int(line[1],2) > prog_count:
                print("Incorrect memory address (line"+ str(input_list.index(line) + 1)+ ")")
                assert 0 == 1, f"Incorrect memory address (line {input_list.index(line) + 1})"
            else:
                mem_addr = line[1]
                string = op_codes_E[line[0]] + '0'*(4 + 7 - len(mem_addr)) + mem_addr
                string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type E" + " " + line[0] + " " + line[1]
                output_list.append(string)

    # type F, errors handled
    elif line[0] == 'hlt':
        if len(line) !=1:
            print("Syntax Error. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1,f"Syntax Error (line {input_list.index(line)+1})"
        string = op_codes_F[line[0]] + '0'*11
        string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type F" + " " + line[0]
        output_list.append(string)

    else:
        print("Invalid opcode name or some typo in opcode name. (line"+ str(input_list.index(line)+1)+ ")")
        assert 0 == 1,f"Invalid opcode name or some typo in opcode name. (line {input_list.index(line)+1})"


def output_func(line):
    global vars
    global var_index
    global input_list
    global output_prog_count

    # type A, register error handling
    if line[0] in op_codes_A:        
        
        if len(line) > 4:
            print("Syntax Error: You have entered in more inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 4:
            print("Syntax Error: You have entered lesser inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if (line[1][0] == "$") or (line[2][0] == "$") or (line[3][0] == "$"):
            print("This assembler does not support operations on immediate values directly. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"This assembler does not support operations on immediate values directly. (line {input_list.index(line)+1})"
        elif line[1] not in regs or line[2] not in regs or line[3] not in regs:
            print("Invalid register name or some typo in register name. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Invalid register name or some typo in register name. (line {input_list.index(line)+1})"
        elif line[1] == "FLAGS" or line[2] == "FLAGS" or line[3] == "FLAGS":
            print("Illegal access to FLAGS register. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Illegal access to FLAGS register. (line {input_list.index(line)+1})"
        string = op_codes_A[line[0]] + '00' + \
            (regs[line[1]] + regs[line[2]] + regs[line[3]])
        string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+" Type A" + " " + line[0] + " " + \
            #line[1] + " " + line[2] + " " + line[3]
        output_list.append(string)

    # type B, error handling done :)
    # this sorts the mov problem by checking reg or $imm
    elif (line[0] in op_codes_B) and (line[2][0] == "$") :

        if len(line) > 3:
            print("Syntax Error: You have entered in more inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            print("Syntax Error: You have entered lesser inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        elif (line[2][0] != "$" ) and (line[2][1:].isdigit()):
            print("Syntax Error: Wrong format for immediate values used. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: Wrong format for immediate values used. (line {input_list.index(line)+1})"
        if line[2][1:].isdigit() ==False:
            print("Immediate value not valid. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1,f"Immediate value not valid. (line {input_list.index(line)+1})"
        binary = bin(int(line[2][1:])).replace("0b", "")
        # I have ignored the case where they give negative number as input.
        if len(binary) > 7:
            print("Illegal immediate values(more than 7 bits). (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Illegal immediate values(more than 7 bits). (line {input_list.index(line)+1})"

        else:
            if len(binary) == 7:
                pass
            elif len(binary) < 7:
                binary = (7 - len(binary))*"0" + binary

            if line[1] not in regs:
                print("Invalid register name or some typo in register name. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Invalid register name or some typo in register name. (line {input_list.index(line)+1})"
            elif line[1] == "FLAGS":
                print("Illegal access to FLAGS register. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Illegal access to FLAGS register. (line {input_list.index(line)+1})"
            string = op_codes_B[line[0]] + '0' + (regs[line[1]]) + binary
            string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type B" + " " + \
                #line[0] + " " + line[1] + " " + line[2]
            output_list.append(string)

    # type C, errors handled
    elif line[0] in op_codes_C:
        if len(line) > 3:
            print("Syntax Error: You have entered in more inputs than required for this opcode.(line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            print("Syntax Error: You have entered lesser inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[1] not in regs or line[2] not in regs:
            print("Invalid register name or some typo in register name. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Invalid register name or some typo in register name. (line {input_list.index(line)+1})"
        elif line[0] == 'mov':
            if line[1] == "FLAGS":
                print("Illegal access to FLAGS register. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Illegal access to FLAGS register. (line {input_list.index(line)+1})"
        elif line[0] != 'mov':
            if line[1] == "FLAGS" or line[2] == "FLAGS":
                print("Illegal access to FLAGS register. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Illegal access to FLAGS register. (line {input_list.index(line)+1})" 
        string = op_codes_C[line[0]] + '0'*5 + (regs[line[1]] + regs[line[2]])
        string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type C" + " " + \
            #line[0] + " " + line[1] + " " + line[2]
        output_list.append(string)

    # variable allotment
    elif line[0] == 'var':
        if len(line) !=2:
            print("Syntax Error. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error. (line {input_list.index(line)+1})"
        # need to convert the entire input into a 2d list, tabhi vars can be indexed and accessed easily
        if (line[1] not in vars):
            vars.update({line[1]: bin(var_index)[2:]})
        else:
            print("Variable already exists. (line"+ str(output_prog_count)+ ")")
            assert 0 == 1, f"Variable already exists. (line {output_prog_count})"

        if len(vars[line[1]]) == 7:
            pass
        elif len(vars[line[1]]) < 7:
            vars[line[1]] = (7 - len(vars[line[1]]))*"0" + vars[line[1]]
        var_index += 1

    # type D, errors handled
    elif line[0] in op_codes_D:
        if len(line) > 3:
            print("Syntax Error: You have entered in more inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode.  (line {input_list.index(line)+1})"
        if len(line) < 3:
            print("Syntax Error: You have entered lesser inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[2] not in vars:
            print("Variable not defined. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Variable not defined. (line {input_list.index(line)+1})"
        elif line[2] in vars:
            if line[1] not in regs:
                print("Invalid register name or some typo in register name. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Invalid register name or some typo in register name. (line {input_list.index(line)+1})"
            elif line[1] == "FLAGS":
                print("Illegal access to FLAGS register. (line"+ str(input_list.index(line)+1)+ ")")
                assert 0 == 1, f"Illegal access to FLAGS register. (line {input_list.index(line)+1})"
            string = op_codes_D[line[0]] + '0' + regs[line[1]] + vars[line[2]]
            string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type D" + " " + \
                #line[0] + " " + line[1] + " " + line[2]
            output_list.append(string)

    # type E, handle the error if label was never initialised - hey handled :)
    elif line[0] in op_codes_E:
        if len(line) > 2:
            print("Syntax Error: You have entered in more inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered in more inputs than required for this opcode. (line {input_list.index(line)+1})"
        if len(line) < 2:
            print("Syntax Error: You have entered lesser inputs than required for this opcode. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Syntax Error: You have entered lesser inputs than required for this opcode. (line {input_list.index(line)+1})"
        if line[1] not in labels:
            print("Label not defined (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1, f"Label not defined. (line {input_list.index(line)+1})"
        elif line[1] in labels:
            mem_addr = labels[line[1]]
            string = op_codes_E[line[0]] + '0'*(4 + 7 - len(mem_addr)) + mem_addr
            string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type E" + " " + line[0] + " " + line[1]
            output_list.append(string)
        elif line[1].isdigit():
            if len(line[1])!=7 or int(line[1],2) > prog_count:
                print("Incorrect memory address (line"+ str(input_list.index(line) + 1)+ ")")
                assert 0 == 1, f"Incorrect memory address (line {input_list.index(line) + 1})"
            else:
                mem_addr = line[1]
                string = op_codes_E[line[0]] + '0'*(4 + 7 - len(mem_addr)) + mem_addr
                string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type E" + " " + line[0] + " " + line[1]
                output_list.append(string)

    # type F, errors handled
    elif line[0] == 'hlt':
        if len(line) !=1:
            print("Syntax Error. (line"+ str(input_list.index(line)+1)+ ")")
            assert 0 == 1,f"Syntax Error. (line {input_list.index(line)+1})"
        string = op_codes_F[line[0]] + '0'*11
        string = string[0:4]  + string[4:8]  + string[8:12]  + string[12:16] #+ " Type F" + " " + line[0]
        output_list.append(string)

    # labels
    elif line[0][-1] == ':':
        if len(line) > 1:
            label_read(line[1:])

    else:
        print("Invalid opcode name or some typo in opcode name. (line"+ str(input_list.index(line)+1)+ ")")
        assert 0 == 1,f"Invalid opcode name or some typo in opcode name (line {input_list.index(line)+1})"


# the only condition under which the program proceeds further, hlt at the end

for i in range(len(input_list)-1):
    if 'hlt' in input_list[i]:
        # throws off execution of the program, hlt not at the end
        print("'hlt' not being used as the last instruction.")
        assert halt_flag == True, "'hlt' not being used as the last instruction."

if 'hlt' in input_list[len(input_list)-1]:
    halt_flag = True

if halt_flag:
    for line in input_list:
        output_prog_count += 1
        if line == []:
            pass    
        else:
            output_func(line)
else:
    # put a suitable error in here
    print("'hlt' statement is absent.")
    assert halt_flag == True, "'hlt' statement is absent."

for i in range(len(output_list)-1):
    print(output_list[i]+'\n')
print(output_list[len(output_list)-1])
# print('-------------------------------------------------------------------------------------------------------------\n')

#-------------end-------------------------------------------------------------------