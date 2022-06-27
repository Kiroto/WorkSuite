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
    firstNumberText = usrIn[1: division].strip(" ")
    lastNumberText = usrIn[division + 1: -1].strip(" ")

    if(not firstBracket in ["(", "["] or not lastBracket in [")", "]"]):
        print("An edge was invalid (please use \"()\" or \"[]\" in your range declaration!")
        return

    if (not firstNumberText.isnumeric() or not lastNumberText.isnumeric()):
        print("One of the entered numbers was invalid. Please write a valid number!")
        return


    startEdge = firstBracket == "("
    endEdge = lastBracket == ")"
    firstNumber = int(firstNumberText)
    lastNumber = int(lastNumberText)

    ex1 = Extreme(firstNumber, startEdge)
    ex2 = Extreme(lastNumber, endEdge)

    r1 = Range(ex1, ex2)
    ranges.append(r1)
    print(f"Successfully added the range {firstBracket}{firstNumber}, {lastNumber}{lastBracket}!")

def listFunct(**kwargs):
    ranges = kwargs["ranges"]
    en = enumerate(ranges)
    for idx, range in en:
        print(f"{idx} - {range}")


functions = {
    "exit": exitFunct,
    "enter": enterFunct,
    "list": listFunct
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
        os.system("cls")

        if (usrIn in functions.keys()):
            toExecute = functions[usrIn]
            if (toExecute(ranges= rangeList) == -1):
                break
            # program


