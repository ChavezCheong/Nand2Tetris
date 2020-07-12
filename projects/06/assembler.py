# Encapsulates access to the input code. Reads an assembly language command,
# parses it, and provides convenient access to the command’s components
# (fields and symbols). In addition, removes all white space and comments.

import sys
import code

def cleancommandline(command_line):
    '''
    Remove comments and whitespace
    '''
    command_line = "".join(command_line.split())
    head, sep, tail = command_line.partition("//")
    return head

def commandtype(command_line):
    '''
    Returns the type of the current
    command:
    - A_COMMAND for @Xxx where
    Xxx is either a symbol or a
    decimal number
    - C_COMMAND for
    dest=comp;jump
    - L_COMMAND (actually, pseudocommand)
    for (Xxx) where Xxx
    is a symbol.
    '''
    if command_line[0] == "@":
        return "A_Command"
    elif command_line.find("(") != -1:
        return "L_Command"
    else:
        return "C_Command"

def convert_binary(mnemonic):
    '''
    Converts decimal numbers in strings to their 15-bit binary equivalents.
    '''
    ob, sep, binary_string = str(bin(int(mnemonic))).partition("0b")
    numlen = 15 - len(binary_string)
    return "0" * numlen + binary_string

symbol_table = {
    "SP":"000000000000000",
    "LCL":"000000000000001",
    "ARG":"000000000000010",
    "THIS":"000000000000011",
    "THAT":"000000000000100",
    "R0":"000000000000000",
    "R1":"000000000000001",
    "R2":"000000000000010",
    "R3":"000000000000011",
    "R4":"000000000000100",
    "R5":"000000000000101",
    "R6":"000000000000110",
    "R7":"000000000000111",
    "R8":"000000000001000",
    "R9":"000000000001001",
    "R10":"000000000001010",
    "R11":"000000000001011",
    "R12":"000000000001100",
    "R13":"000000000001101",
    "R14":"000000000001110",
    "R15":"000000000001111",
    "SCREEN":"100000000000000",
    "KBD":"110000000000000"
}

if __name__ == "__main__":   
    #Opens file and removes all empty lines and returns the assembly file into a list
    try:
        with open(sys.argv[1], 'r') as assembly_file:
            assembly_script = assembly_file.read()
        command_list = assembly_script.split('\n')
        command_list = list(filter(None, command_list))
    except IndexError:
        print("Missing argument. Please indicate a .asm file to be assembled into hack.")

    ROM_address = 0

    # First Sweep
    for command_line in command_list:
        command_line = cleancommandline(command_line)
        if len(command_line) > 0:
            if commandtype(command_line) == "L_Command": #Generating labels
                symbol_table.setdefault(command_line[command_line.find("(")+1:command_line.find(")")],convert_binary(str(ROM_address)))
            else:
                ROM_address += 1

    # Second Sweep
    outputlist = []
    variable_memory_count = 16

    for command_line in command_list:
        outputline = ""
        command_line = cleancommandline(command_line) # Clean comments and whitespace
        if len(command_line) > 0:
            if commandtype(command_line) == "A_Command":
                if not command_line[1:].isnumeric():
                    if not command_line[1:] in symbol_table:
                        symbol_table[command_line[1:]] = convert_binary(str(variable_memory_count))
                        variable_memory_count += 1
                    address = symbol_table[command_line[1:]]
                else:
                    address = convert_binary(command_line[1:])
                outputline = outputline + "0" + address
                outputlist.append(outputline)
            elif commandtype(command_line) == "C_Command":
                dest = ""
                jump = ""
                comp = ""
                if command_line.find(";") > 0:
                    comp, sep, jump = command_line.partition(";")
                else:
                    dest, sep, comp = command_line.partition("=")
                outputline = outputline + "111" + code.comp(comp) + code.dest(dest) + code.jump(jump)
                outputlist.append(outputline)
    #Write to a file
    filename, sep, extension = assembly_file.name.partition(".")
    filename = filename + ".hack"
    with open(filename, "w+") as outputfile:
        for outputline in outputlist:
            outputfile.write(outputline + "\n")


    
    

        



