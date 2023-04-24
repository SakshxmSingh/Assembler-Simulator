import os

op_codes = {
            'add':('00000','A'),
            'sub':('00001','A'),
            'mov':[('00010','B'),('00011','C')],            #this needs to be taken care and thought upon
            'ld':('00100','D'),
            'st':('00101','D'),
            'mul':('00110','A'),
            'div':('00111','C'),
            'rs':('01000','B'),
            'ls':('01001','B'),
            'xor':('01010','A'),
            'or':('01011','A'),
            'and':('01100','A'),
            'not':('01101','C'),
            'cmp':('01110','C'),
            'jmp':('01111','E'),
            'jlt':('11100','E'),
            'jgt':('11101','E'),
            'je':('11111','E'),
            'hlt':('11010','F')
            }

op_codes_A = {
              'add':'00000',
              'sub':'00001',
              'mul':'00110',
              'xor':'01010',
              'or':'01011',
              'and':'01100'
             }

regs = {
        'R0':'000',
        'R1':'001',
        'R2':'010',
        'R3':'011',
        'R4':'100',
        'R5':'101',
        'R6':'110'
        }

f_input =  open("read.txt",'r+')
f_output = open("write.txt",'a+')

f_output.seek(0)
f_output.truncate()

for line in f_input:
    line = line.split()
    
    #type A, error handling left
    if line[0] in op_codes_A:
        string = ''
        string += op_codes_A[line[0]]+'00'+(regs[line[1]]+regs[line[2]]+regs[line[3]])
        string = string[0:4]+'_'+string[4:8]+'_'+string[8:12]+'_'+string[12:16]
        f_output.write(string+"\n")
