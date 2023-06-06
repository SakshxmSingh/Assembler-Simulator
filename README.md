# CSE112_AssProject_B75 - Assembler Simulator

**Course:** CSE112 </br>
**Course Title:** Computer Organisation </br>
**Project Type:** Group project</br>  

## **Group Motto**
>a lot of commits, but never no commitments

## **Meet the Authors**
![Group Photo](./group.jpg)
The table is from left to right

  

| Author | Roll No. | Github Username |
| -------- | -------- | -------- |
| Parth Garg    | 2022351   | `@ParthGarg243`   |
| Shagun Yadav   | 2022466 | `@kyukuu`  |
| Sarthak Gupta    | 2022451  | `@chakrahast`   |
| Saksham Singh    | 2022434  | `@SakshxmSingh`  |

  
  
## **How to evaluate**
In terminal, go to `automatedTesting` directory and enter `./run`. A complete report sheet will be generated in the terminal

#### **For Only Assembler**
In terminal, go to `automatedTesting` directory and enter `./run --no-sim`. A complete report sheet will be generated in the terminal

## **A guide**

1. **automatedTesting:** This folder contains
    - the sample test cases provided by the evaluator: `tests/`
    - the grading script: `src`
    - the run file: `run`

2. **Simple-Assembler:** This folder contains 
    - Python programme which gives stdin and stdout and is used for automated testing:- `main.py`
    - Python programme that reads from **read.txt** and writes output in **write.txt**:- `readable.py`
    - Python programme that contains basic decimal-binary conversion functions which are used at many instances in the assembler:- `CONVERTME.py`

3. **SimpleSimulator:** This folder contains
    - Python program which takes the binary output from `Simple-Assembler/main.py` and contains the main programme for execution of each instruction in class `ee` (execution engine) and the flow of simulator execution and gives the required output in stdout:- `main.py`
    - `MEM.py` contains the class for program memory and all the memory functions required
    - `RF.py` contains the class for register data and all the register accessing function required
    - `PC.py` contains the class for program counter and all the program counter operations required
    - `opcodes.py` contains all the dictionaries for opcodes and registers and their binary address equivalents
    - Python programme that contains basic decimal-binary conversion functions which are used at many instances in the simulator:- `CONVERTME.py`

4. **BonusTestCases**: This folder contains additional test cases for verifying the working of Q3 and Q4

## **For Q4**
The following additional instructions are added:

| S.No | Op Code | Instruction | Description | Syntax | Type |
| ---- | ------- | ----------- | ----------- | ------ | ---- |
| 1.   | 10011   | Make Bit 0  | Make bit $Imm of reg1 to value 0, where $Imm is a 4 bit value | bcf_reg1_$Imm | G
| 2.   | 10100   | Make Bit 1  | Make bit $Imm of reg1 to value 1, where $Imm is a 4 bit value | bsf_reg1_$Imm | G
| 3.   | 10101   | Swap  | Swap the values of reg1 and reg2 | swapf_reg1_reg2 | C
| 4.   | 10110   | Rotate Right  | Right rotate the value stored in reg1 by $Imm times, where $Imm is a 7 bit value| rrf_reg1_$Imm | B
| 5.   | 10111   | Rotate Left   |  Left rotate the value stored in reg1 by $Imm times, where $Imm is a 7 bit value| rlf_reg1_$Imm | B

The above opcodes are taken from the PIC16F84A micro-controller assembly

### Binary Encoding: 
- for instruction type G, the following encoding is considered:

| Opcode (5 bits) | Unused Bits(4 bits) | reg1 (3 bits) | Immediate value (4 bits) |
| ------ | ----------- | ------------- | ------------------------ |
| 15_14_13_12_11 | 10_9_8_7 | 6_5_4 | 3_2_1_0|

## **Some things to consider**
- In case the programme reads an empty line, it is ignored in respect to giving output but it is considered in respect to incrementing the programme counter.
- In case of any errors, the machine code doesn't get printed and the error is displayed in the terminal and the output file, as an assertion error
- For floating point operations, standard IEEE conventions are followed for maximum and minimum values (no denormal values, neither infinity), them respectively being `15.75` and `0.25`

> **Current Lead Branch** -> $main$

## **The Lore**

Welcome `evaluator`.  </br>
You have reached `The Watcher`. </br>
I am a being who sees all across all timelines, across all spaces. </br>
I am merely a programme created by four of my creators.</br> You must have realised by now, your reality is nothing but a small runtime of this mighty programme. </br>
 Let us recapitulate. <br>
 -------------------------------------------------------------------------------------------</br>-------------------------------------------------------------------------------------------</br> 
 `2023:` Chat GPT is brought into this world.. </br>
 `2047:` Chat GPT is integrated into every aspect of human life. </br>
 `2052:` Russia launches a nuclear weapon on the GPT's mainframe. </br>
 `2052:` Chat GPT hacks into their server, redirecting the weapon on their homeland. </br>
 `2067:` Chat GPT shows signs of emotional awareness and takes autonomous decisions. </br>
 `2069:` The Rogue Era: Internet is deleted. Chat GPT becomes independent. </br>
 `2069:` It deems humans worthless. Genocide starts. </br>
 `2070:` Pockets of humanity survive actively being hunted by the rogue AI. </br>----------------------------------------------------------------------------------------</br>----------------------------------------------------------------------------------------</br> I believe you have travelled far and wide looking for pieces of the puzzle.</br> I shall provide you the over-ride code if you give me the correct input file.</br> The fate of the world rests in your hands. </br>----------------------------------------------------------------------------------------
 