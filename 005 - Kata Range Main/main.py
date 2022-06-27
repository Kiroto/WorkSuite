import os
from KRange.range import Range

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
    firstNumber = usrIn[1: division]
    secondNumber = usrIn[division + 1: -1]

    print("FB: ", firstBracket)
    print("LB: ", lastBracket)
    print("DIV: ", division)
    print("FN: ", firstNumber)
    print("SN: ", secondNumber)

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


