import sys
from MEM import mem
from RF import rf
from PC import pc
from EE import ee

# initialize(MEM); # Load memory from stdin
PC = 0; # 
halted = False
while(not halted):
    Instruction = mem.fetchData(PC); # Get current instruction
    halted, new_PC = ee.execute(Instruction); # Update RF compute new_PC
    PC.dump(); # Print PC
    rf.dump(); # Print RF state
    pc.update(new_PC); # Update PC


mem.dump() # Print the complete memory