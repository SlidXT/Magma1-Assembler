# MAGMA1 ASSEMBLER #

## TABLE OF CONTENTS ##
[**CODING**](#CODING) 
- [INSTRUCTION](#instruction)
- [BRANCHING](#branching)
- [MEMORY](#memory)

[**ASSEMBLING**](#CODING) 
- [WRITING](#writing)
- [RUNNING](#executing)

[**MINECRAFT**](#MINECRAFT) 
- [COMPUTER](#computer)
- [CODE](#code)

[**RUNNING**](#RUNNING) 
- [CHECKS](#checks)
- [CLOCK](#clock)

[**DISCLAIMER**](#DISCLAIMER) 

<a name="CODING"></a>
## CODING ##

<a name="instruction"></a>
###### INSTRUCTION ######
Use the **STRUCTURE** in the `Assembly Sheet`\
Ex. ADD, C, A, B *(ADD, Dest, Src1, Src2)*\
Which makes, C = A + B\
Remember there are only 32 lines, starting at 0

<a name="branching"></a>
###### BRANCHING ######
Branching relies on the **PREVIOUS ARITHMETIC** instruction for flags\
Yellow instructions in the `Assembly Sheet` update the flags\
**PNT**, is a pointer, **BRH**, is an immediate\
Use the Abbreviation for the **CONDITION** part\
Ex. BRH, GRTR, 10 *(BRH, CONDITION, NUMBER)*\
Which makes, Jump to 10 if Greater

<a name="memory"></a>
###### MEMORY ######
**RAM & I/O** is Memory Mapped, meaning\
**RAM** ranges from 0 - 223, and\
**I/O** ranges from 224 - 255\
Ps. M means Memory, R means Register

<a name="ASSEMBLING"></a>
## ASSEMBLING ##

<a name="writing"></a>
###### WRITING ######
To write your code, paste it into the `input.txt`\
Which is under `files`\
With **ONLY 1** instruction per line\
Ensure there are at **MAX** 32 lines

<a name="executing"></a>
###### EXECUTING ######
Run the `main.py` file to begin\
The machine code will be in `machine.txt`\
However that is non-relevant\
The output will be an `output.schem` file

<a name="MINECRAFT"></a>
## MINECRAFT ##

<a name="computer"></a>
###### COMPUTER ######
Before you can paste in the **CODE**,\
you must paste in the **COMPUTER** itself\
Paste in `Magma1.schem` into your world using [**World Edit**](https://www.curseforge.com/minecraft/mc-mods/worldedit)\
Ensure **ALL** redstone has updated properly

<a name="code"></a>
###### CODE ######
Paste the `output.schem` into your world using [**World Edit**](https://www.curseforge.com/minecraft/mc-mods/worldedit)\
Align the blocks with the redstone torches, which are on lamps\
Move the blocks down so the blocks are inline with the lamps

<a name="RUNNING"></a>
## RUNNING ##

<a name="checks"></a>
###### CHECKS ######
Ensure **ALL** blocks are aligned properly\
**ALL** redstone is updated properly
**PROGRAM COUNTER** is on line 0

<a name="clock"></a>
###### CLOCK ######
The **CLOCK** is found behind the **PC**\
On the underside of the **COMPUTER**\
Turn it on to begin running the program

<a name="DISCLAIMER"></a>
## DISCLAIMER ##
The **COMPUTER** has,\
32 bytes of **RAM** on hand,\
Expandable to 224 bytes\
8 **I/O** ports on hand,\
Expandable to 32 ports
32 lines of **PROM**,
which is non-expandable

###### MAGMA1 ASSEMBLER ######
