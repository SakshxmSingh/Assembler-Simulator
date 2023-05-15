import os
import shutil

test_files = os.listdir('Assembler/TestCases/SimpleGen')
main_file = 'Assembler/ass.py'
input_file = "Assembler/read.txt"
output_dir = 'Assembler/Bin/simpleBin'

for test_file in test_files:
    test_file_path = os.path.join('Assembler/TestCases/SimpleGen', test_file)
    shutil.copyfile(test_file_path, input_file)
    os.system(f'python3 {main_file}')
    output_file = os.path.basename(test_file).replace('test', 'output')
    shutil.move('write.txt', os.path.join(output_dir, f'{output_file}.txt'))