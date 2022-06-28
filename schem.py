from nbt.nbt import *
def GenNBTfile(Code:list):
    #create NBT file
    NBTfile = NBTFile()
    NBTfile.name = "Schematic"
    
    #create metadata (WE offsets)
    NBTfile.tags.append(TAG_Compound(name = "Metadata"))
    NBTfile["Metadata"].tags.extend([
    TAG_Int(name = "WEOffsetX", value = 1), 
    TAG_Int(name = "WEOffsetY", value = -13),
    TAG_Int(name = "WEOffsetZ", value = -30)])

    #create palette
    NBTfile.tags.append(TAG_Compound(name = "Palette"))
    NBTfile["Palette"].tags.extend([
    TAG_Int(name = "minecraft:air", value = 0),
    TAG_Int(name = "minecraft:redstone_block", value = 1),
    TAG_Int(name = "minecraft:glass", value = 2)])

    #Create other and BlockDataArray
    NBTfile.tags.extend([TAG_Int(name = "DataVersion", value = 2730),
    TAG_Short(name = "Height", value = 15),
    TAG_Short(name = "Length", value = 31),
    TAG_Short(name = "Width", value = 28),
    TAG_Int(name = "PaletteMax", value = 3),
    TAG_Int(name = "Version", value = 2),
    TAG_Byte_Array(name = "BlockData")])

    #create actual Blockdata
    Blockdata = [0 for i in range(15*31*28)]
    for InstrID in range(32):   #go through each instr
        Instr = Code[InstrID]
        z = 30 - (InstrID % 16) * 2

        for BitID in range(16):      #go trough each bit of the instr
            Bit = Instr & (1<<BitID)
            x = (InstrID // 16) * 10 + 17 * (1 - (BitID // 8))
            y = (BitID % 8) * 2
            if Bit == 0:
                Blockdata[(y*31 + z)*28 + x] = 1    #redstone block
            else:
                Blockdata[(y*31 + z)*28 + x] = 2    #glass
    #write Blockdata
    NBTfile["BlockData"].value = Blockdata

    return NBTfile

def main():
    codeFile = open("files/machine.txt", "r")
    code = codeFile.readlines()
    for i in range(len(code)):
        code[i] = int(code[i].strip(), base=2)
    codeFile.close()

    files = GenNBTfile(code) 
    files.write_file("output.schem")

    print("Schematic Successful!")
    print("DONE!")