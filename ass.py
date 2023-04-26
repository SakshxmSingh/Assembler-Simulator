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
f_output.write('------------\n')

f_output.write("Welcome user.\nWelcome to a programme put into existence by the combined forces of users 2022434, 2022451, 2022351, 2022466.\n")
f_output.write('------------------------------------------------------------------------------------------------------------\n')
f_output.write('The programme has taken in your commands.\n')
f_output.write('----------------------------------------\n')

prog_count=0

input_list = f_input.readlines()
if len(input_list) == 0:
    f_output.write('Error 256 detected: There were no instructions given. The programme has come to an end. \n')
else:
   f_output.write("The following output was generated.\n")
   f_output.write('-----------------------------------\n')
halt_flag = False
for i in range(len(input_list)):
    input_list[i] = input_list[i].split()
    if input_list[i][0]!='var':
        prog_count+=1
    if (input_list[i][0]=='hlt') and i!=len(input_list)-1:
        halt_flag = True
        f_output.write('halt not in end\n')
    elif input_list[i][0]=='hlt' and i==len(input_list)-1:
        halt_flag=True
if (halt_flag==False)and (len(input_list) != 0):
    f_output.write('halt not in program\n')

vars = {}
var_index = prog_count

for line in input_list:
    # line = line.split()
    
    #type A, error handling left
    if line[0] in op_codes_A:
        string = op_codes_A[line[0]]+'00'+(regs[line[1]]+regs[line[2]]+regs[line[3]])
        string = string[0:4]+'_'+string[4:8]+'_'+string[8:12]+'_'+string[12:16] + " Type A" + " " + line[0] + " "+ line[1] +" "+ line[2]+ " "+line[3]
        f_output.write(string+"\n")


    
    #typeB
    elif (line[0] in op_codes_B) and (line[2][0] == "$") : # this sorts the mov problem by checking reg or $imm
        binary = bin(int(line[2][1:])).replace("0b", "")        
                                                    #I have ignored the case where they give negative number as input.
        if len(binary) > 7:
            string = "overflow error" + " Type B" + " " + line[0] + " "+ line[1] +" "+ line[2]
            f_output.write(string+"\n")
        else:
            if len(binary) == 7:
                pass  
            elif len(binary) < 7:
                binary = (7-len(binary))*"0"+binary        
        
            string = op_codes_B[line[0]] + '0'+ (regs[line[1]]) + binary
            string = string[0:4]+'_'+string[4:8]+'_'+string[8:12]+'_'+string[12:16] + " Type B" + " " + line[0] + " "+ line[1] +" "+ line[2]
            f_output.write(string+"\n")


    #type C
    elif line[0] in op_codes_C:
        string = op_codes_C[line[0]]+'00000'+(regs[line[1]]+regs[line[2]])
        string = string[0:4]+'_'+string[4:8]+'_'+string[8:12]+'_'+string[12:16] + " Type C"+ " "  + line[0] + " "+ line[1] +" "+ line[2]
        f_output.write(string+"\n")


    #type D, needs to be tested
    if line[0]=='var':
        #need to convert the entire input into a 2d list, tabhi vars can be indexed and accessed easily
        vars.update({line[1]:bin(var_index)[2:]})
        if len(vars[line[1]]) == 7:
            pass  
        elif len(vars[line[1]]) < 7:
            vars[line[1]] = (7-len(vars[line[1]]))*"0"+vars[line[1]]
        var_index+=1
    
    if line[0] in op_codes_D:
        if line[2] in vars:
            string = op_codes_D[line[0]]+'0'+regs[line[1]]+vars[line[2]]
            string = string[0:4]+'_'+string[4:8]+'_'+string[8:12]+'_'+string[12:16] + " Type D"+ " "  + line[0] + " "+ line[1] +" "+ line[2]
            f_output.write(string+"\n")


    #type F
    if line[0] == 'hlt':
        #no need to test i hope
        string = op_codes_F[line[0]] + '0'*11
        string = string[0:4] + '_' + string[4:8] + '_' + string[8:12] + '_' + string[12:16]
        f_output.write(string + '\n')







f_output.write('-----------------------------------------------------------------------------------------------------------------------\n')