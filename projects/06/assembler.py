# Nand2Tetris program to convert assembly language to Hack binary code.
# File opening code courtesy of jameshope87 
# at https://github.com/jameshope87/nand2tetris/blob/master/projects/06/assemblerns.py

import sys

def openfile(filename):
    with open(filename, "r", newline=None) as hackfile:
        nstripped = list(filter(('\n').__ne__, hackfile.readlines())) # Cleans the '\n' symbols from the list
        newlinestripped = []
        for line in nstripped:
            newlinestripped.append(line.translate(None, '\t\r\n\v'))
        return newlinestripped



def commandType(string):
    pass





if __name__ == "__main__":
    filename = sys.argv[1]
    commands = openfile(filename)
    print(commands)