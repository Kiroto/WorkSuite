from romanConverter import *
import platform    # For obtaining the operating system information
import os          # Import the os module to clear screen

def clr_scr():
    #Python program to clear screen
    #Get command to execute
    if(platform.system().lower() == "windows"):
        cmd = 'cls'
    else:
        cmd = 'clear'
    # Run command
    os.system(cmd)

# Input Example
# 4 000 000
# Output Example
# ____
# MMMM

# Input Exxample
# 3 000 035
# Output Example
# ___
# MMMXXXV

def printNumerals(tops: str, bottoms: str):
    size = os.get_terminal_size()
    cols = size.columns
    while(len(tops) > 0):
        topSegment = tops[:cols]
        bottomSegment = bottoms[:cols]
        tops = tops[cols:]
        bottoms = bottoms[cols:]
        print(topSegment)
        print(bottomSegment)

def getUserString(prompt:str):
    print(prompt)
    userInput = input()
    return userInput

def main():
    clr_scr()
    while (True):
        userIn = getUserString("Write the number to be transformed to a roman numeral.\n(Values > 0, non decimal)\n(or \"exit\" to exit)").lower()
        if (userIn == "exit"):
            break
        clr_scr()
        if (not isNatural(userIn)):
            print("The value entered \"" + userIn + "\" is not a natural number...")
            continue
        print("The number \"" + userIn + "\" in roman numerals is:")
        romanNumeralTuple = transformToRomanNumeral(int(userIn))
        printNumerals(romanNumeralTuple[0], romanNumeralTuple[1])

if __name__ == "__main__":
    main()
