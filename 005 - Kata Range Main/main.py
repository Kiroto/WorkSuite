import imp
import os
from KRange.range import Range
from KRange.extreme import Extreme

def exitFunct(**kwargs):
    return -1

def enterFunct(**kwargs):
    ranges = kwargs["ranges"]
    print("Enter a new range")
    print("Ranges of the form: <( or [> + <integer> + \",\" + <integer> + <) or ]> ")
    usrIn = input()
    firstBracket = usrIn[0]
    lastBracket = usrIn[-1]
    division = usrIn.find(",")
    firstNumber = int(usrIn[1: division])
    secondNumber = int(usrIn[division + 1: -1])
    isOpen1 = True
    isOpen2 = True
    
    print("FB: ", firstBracket)
    print("LB: ", lastBracket)
    print("DIV: ", division)
    print("FN: ", firstNumber)
    print("SN: ", secondNumber)
    if(firstBracket in ["(", "["]): 
        isOpen1 = firstBracket == "("
    if(lastBracket in [")", "]"]):
        isOpen2 = lastBracket == ")"
    
    ex1 = Extreme(firstNumber, isOpen1)
    ex2 = Extreme(secondNumber, isOpen2)

    r1 = Range(ex1, ex2)
    ranges.append(r1)
    print(r1.allPoints())


functions = {
    "exit": exitFunct,
    "enter": enterFunct
}


def showFunctions(**kwargs):
    keys = functions.keys()
    print("The available commands are:")
    for key in keys:
        print(key)


functions["help"] = showFunctions

if __name__ == "__main__":
    print("Welcome to the Range Testing program!")
    rangeList = []
    showFunctions()
    while(True):
        print("Issue your next command")
        usrIn = input().lower()
        toExecute = functions[usrIn]
        os.system("cls")

        if (usrIn in functions.keys()):
            toExecute = functions[usrIn]
            if (toExecute(ranges= rangeList) == -1):
                break
            # program


