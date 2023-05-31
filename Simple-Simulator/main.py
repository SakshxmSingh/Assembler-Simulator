import sys
from MEM import mem
from RF import rf
from PC import pc
from EE import ee

progMem = mem() # Create memory object
progMem.initialize(sys.stdin.readlines()) # Load memory from stdin

progCount = pc() # Create PC object
regData = rf() # Create RF object

halted = False
while(not halted):
    Instruction = progMem.fetchData(progCount.pc); # Get current instruction
    halted, new_PC = ee.execute(Instruction) # Update RF compute new_PC
    progCount.dump() # Print PC
    rf.dump() # Print RF state
    progCount.update(new_PC) # Update PC


progMem.dump() # Print the complete memory