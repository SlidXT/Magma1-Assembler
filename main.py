import lib
import schem

finalCode = []

def writeFile():
    x = 32 - len(finalCode)
    for i in range(x):
        finalCode.append("0000000000000000")

    codeFile = open("files/machine.txt", "w")
    for i in range(len(finalCode)):
        if i != 0:
            codeFile.write("\n")
        codeFile.write(finalCode[i])
    codeFile.close()

    print("Machine Code Successful!")

def readFile():
    codeFile = open("files/input.txt", "r")
    code = codeFile.readlines()
    codeFile.close()
    return code

def toBin(num, length):
    binNum = "{0:b}".format(int(num))
    for i in range((length) - len(binNum)):
        binNum = "0" + binNum
    return binNum

def aInst(line):
    tempCode = ""
    tempCode += lib.register[line[1]]
    tempCode += lib.operation[line[0]][1]
    tempCode += lib.register[line[2]]
    tempCode += "000"
    return tempCode

def fInst(line):
    tempCode = ""
    tempCode += lib.register[line[1]]
    tempCode += lib.operation[line[0]][1]
    tempCode += lib.register[line[2]]
    tempCode += lib.register[line[3]]
    return tempCode

def main():
    code = readFile()
    for instruction in code:
        line = []
        tempCode = ""
        instruction = instruction.strip()
        line = instruction.split(", ")

        if not instruction:
            continue

        tempCode += lib.operation[line[0]][0]
        if line[0] == "NOP":
            tempCode += lib.operation[line[0]][1]
        elif line[0] == "LDM":
            tempCode += lib.register[line[1]]
            tempCode += lib.operation[line[0]][1]
            tempCode += lib.register[line[2]]
            tempCode += "000"
        elif line[0] == "STM":
            tempCode += "000"
            tempCode += lib.operation[line[0]][1]
            tempCode += lib.register[line[1]]
            tempCode += lib.register[line[2]]

        elif line[0] == "ADD" or line[0] == "SUB":
            tempCode += fInst(line)
        elif line[0] == "IAD" or line[0] == "DES":
            tempCode += fInst(line)
        elif line[0] == "AND" or line[0] == "ORE":
            tempCode += fInst(line)
        elif line[0] == "XOR":
            tempCode += fInst(line)

        elif line[0] == "IMM":
            tempCode += lib.register[line[1]]
            tempCode += toBin(int(line[2]), 8)

        elif line[0] == "BRH":
            tempCode += lib.flag[line[1]]
            tempCode += lib.operation[line[0]][1]
            tempCode += "0"
            tempCode += toBin(int(line[2]), 5)
        elif line[0] == "PNT":
            tempCode += lib.flag[line[1]]
            tempCode += lib.operation[line[0]][1]
            tempCode += "000"
            tempCode += lib.register[line[2]]

        else:
            tempCode += aInst(line)

        finalCode.append(tempCode)
        
    writeFile()

if __name__ == "__main__":
    main()

schem.main()