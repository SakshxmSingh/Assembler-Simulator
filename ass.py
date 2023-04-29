op_codes_A = {
              'add':'00000',
              'sub':'00001',
              'mul':'00110',
              'xor':'01010',
              'or':'01011',
              'and':'01100'
             }

op_codes_B = {
              'mov':'00010',
              'rs':'01000',
              'ls':'01101',
              }

op_codes_C = {
              'mov':'00011',
              'div':'00111',
              'not':'01001',
              'cmp':'01110'
              }

op_codes_D = {
              'ld':'00100',
              'st':'00101'
             }

op_codes_E = {
                'jmp' : '01111',
                'jlt' : '11100',
                'jgt' : '11101',
                'je' : '11111'
             }

op_codes_F = {
                'hlt' : '11010'
             }

regs = {
        'R0':'000',
        'R1':'001',
        'R2':'010',
        'R3':'011',
        'R4':'100',
        'R5':'101',
        'R6':'110',
        'FLAGS':'111'
        }

f_input =  open("read.txt",'r+')
f_output = open("write.txt",'a+')

f_output.seek(0)
f_output.truncate()

# welcome message
f_output.write('-------------\n')

f_output.write("Welcome user.\nWelcome to a programme put into existence by the combined forces of users 2022434, 2022451, 2022351, 2022466.\n")
f_output.write('-------------------------------------------------------------------------------------------------------------\n')
f_output.write('The programme has taken in your commands.\n')
f_output.write('-----------------------------------------\n')

prog_count=0

labels={}

output_list=[]  #to store all the correct lines in the initial program
input_list = f_input.readlines()

if len(input_list) == 0:
    f_output.write('Error 256 detected: There were no instructions given. The programme has come to an end. \n')
else:
   f_output.write("The following output was generated.\n")
   f_output.write('-----------------------------------\n')

halt_flag = False

for i in range(len(input_list)):
    
    input_list[i] = input_list[i].split()
    
    if input_list[i][0][-1] == ':':
        labels.update({input_list[i][0][:len(input_list[i][0]) - 1]:bin(prog_count)[2:]})
    
    if input_list[i][0] != 'var':
        prog_count += 1
    # needs to be checked with suitable testcases, both asserts
#     if (input_list[i][0] == 'hlt') and i != len(input_list)-1:
#         assert halt_flag==True, "halt statement not at the end"

#     elif input_list[i][0] == 'hlt' and i == len(input_list)-1:
#         halt_flag = True
    
#     assert halt_flag==True,"Halt statement is not present"

# if (halt_flag == False) and (len(input_list) != 0):
#     f_output.write('halt not in program\n')

vars = {}
var_index = prog_count

def label_read(line):
    global vars
    global var_index

    #type A, error handling done :)
    if line[0] in op_codes_A:
        if line[1] not in regs or line[2] not in regs or line[3] not in regs:
            assert 0==1, "Invalid register name or some typo in register name"
        string = op_codes_A[line[0]] + '00' + (regs[line[1]] + regs[line[2]] + regs[line[3]])
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type A" + " " + line[0] + " " + line[1] + " " + line[2] + " " + line[3]
        f_output.write(string + "\n")


    #type B, error handling done :)
    elif (line[0] in op_codes_B) and (line[2][0] == "$") : # this sorts the mov problem by checking reg or $imm
        binary = bin(int(line[2][1:])).replace("0b", "")        
                                                    #I have ignored the case where they give negative number as input.
        if len(binary) > 7:
            assert 0==1,"Illegal immediate values(more than 7 bits)"
            
        else:
            if len(binary) == 7:
                pass  
            elif len(binary) < 7:
                binary = (7 - len(binary))*"0" + binary        

            if line[1] not in regs:
                assert 0==1, "Invalid register name or some typo in register name"
            string = op_codes_B[line[0]] + '0'+ (regs[line[1]]) + binary
            string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type B" + " " + line[0] + " " + line[1] + " " + line[2]
            f_output.write(string + "\n")


    #type C
    elif line[0] in op_codes_C:
        if line[1] not in regs or line[2] not in regs:
            assert 0==1,"Invalid register name or some typo in register name"
        string = op_codes_C[line[0]] + '0'*5 + (regs[line[1]] + regs[line[2]])
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type C" + " " + line[0] + " " + line[1] + " " + line[2]
        f_output.write(string + "\n")


    #type D, needs to be tested
    elif line[0] == 'var':
        #need to convert the entire input into a 2d list, tabhi vars can be indexed and accessed easily
        vars.update({line[1]:bin(var_index)[2:]})
        if len(vars[line[1]]) == 7:
            pass  
        elif len(vars[line[1]]) < 7:
            vars[line[1]] = (7 - len(vars[line[1]]))*"0" + vars[line[1]]
        var_index += 1
    
    elif line[0] in op_codes_D:
        if line[2] in vars:
            string = op_codes_D[line[0]] + '0' + regs[line[1]] + vars[line[2]]
            string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type D" + " " + line[0] + " " + line[1] + " " + line[2]
            f_output.write(string + "\n")


    #type E, handle the error if label was never initialised
    elif line[0] in op_codes_E:
        mem_addr = labels[line[1]]
        string = op_codes_E[line[0]] + '0'*(4 + 7 - len(mem_addr)) + mem_addr
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type E" + " " + line[0] + " " + line[1]
        f_output.write(string + '\n')


    #type F, no need to test i hope
    elif line[0] == 'hlt':
        string = op_codes_F[line[0]] + '0'*11
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type F" + " " + line[0]
        f_output.write(string + '\n')
   
def output_func(line):
    global vars
    global var_index

    #type A, register error handling
    if line[0] in op_codes_A:

        if line[1] not in regs or line[2] not in regs or line[3] not in regs:
            assert 0==1, "Invalid register name or some typo in register name"
        string = op_codes_A[line[0]] + '00' + (regs[line[1]] + regs[line[2]] + regs[line[3]])
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type A" + " " + line[0] + " " + line[1] + " " + line[2] + " " + line[3]
        f_output.write(string + "\n")


    #type B, error handling done :)
    elif (line[0] in op_codes_B) and (line[2][0] == "$") : # this sorts the mov problem by checking reg or $imm
        binary = bin(int(line[2][1:])).replace("0b", "")        
        #I have ignored the case where they give negative number as input.
        if len(binary) > 7:
            assert 0==1,"Illegal immediate values(more than 7 bits)"
            
        else:
            if len(binary) == 7:
                pass  
            elif len(binary) < 7:
                binary = (7 - len(binary))*"0" + binary        

            if line[1] not in regs:
                assert 0==1, "Invalid register name or some typo in register name"
            string = op_codes_B[line[0]] + '0'+ (regs[line[1]]) + binary
            string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type B" + " " + line[0] + " " + line[1] + " " + line[2]
            f_output.write(string + "\n")

    #type C
    elif line[0] in op_codes_C:
        if line[1] not in regs or line[2] not in regs:
            assert 0==1,"Invalid register name or some typo in register name"
        string = op_codes_C[line[0]] + '0'*5 + (regs[line[1]] + regs[line[2]])
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type C" + " " + line[0] + " " + line[1] + " " + line[2]
        f_output.write(string + "\n")


    #type D, needs to be tested
    elif line[0] == 'var':
        #need to convert the entire input into a 2d list, tabhi vars can be indexed and accessed easily
        vars.update({line[1]:bin(var_index)[2:]})
        if len(vars[line[1]]) == 7:
            pass  
        elif len(vars[line[1]]) < 7:
            vars[line[1]] = (7 - len(vars[line[1]]))*"0" + vars[line[1]]
        var_index += 1
    
    elif line[0] in op_codes_D:
        if line[2] in vars:
            string = op_codes_D[line[0]] + '0' + regs[line[1]] + vars[line[2]]
            string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type D" + " " + line[0] + " " + line[1] + " " + line[2]
            f_output.write(string + "\n")


    #type E, handle the error if label was never initialised
    elif line[0] in op_codes_E:
        mem_addr = labels[line[1]]
        string = op_codes_E[line[0]] + '0'*(4 + 7 - len(mem_addr)) + mem_addr
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type E" + " " + line[0] + " " + line[1]
        f_output.write(string + '\n')


    #type F, no need to test i hope
    elif line[0] == 'hlt':
        string = op_codes_F[line[0]] + '0'*11
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16] + " Type F" + " " + line[0]
        f_output.write(string + '\n')

    #labels
    elif line[0][-1] == ':':
        label_read(line[1:])



if 'hlt' in input_list[len(input_list)-1]: # the only condition under which the program proceeds further, hlt at the end
        halt_flag=True
else:
    for i in range(len(input_list)-1):
        if 'hlt' in input_list[i]:
            assert halt_flag==True,"'hlt' not being used as the last instruction" # throws off execution of the program, hlt not at the end


if halt_flag:
    for line in input_list:
        output_func(line)
else:
    assert halt_flag==True,"'hlt' statement is absent" # put a suitable error in here





f_output.write('-------------------------------------------------------------------------------------------------------------\n')