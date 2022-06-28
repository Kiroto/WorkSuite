import os
from unicodedata import numeric
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

def delFunct(**kwargs):
    ranges = kwargs["ranges"]
    listFunct(ranges = ranges)
    print("what range do you whant to remove?: ")
    delText = input()
    if (not delText.isnumeric()):
        print("the index that you're searching was not a number. please write a valid index")
        return
    delIndex = int(delText)
    if(not (delIndex >= 0 and delIndex < len(ranges))):
        print("the index you are searching is not available, please cry about it :)")
        return 
    ranges.pop(delIndex)
    
def overlapFunct(**kwargs):
    ranges = kwargs["ranges"]

    idxText = input()
    if (not idxText.isnumeric()):
        print("the index that you're searching was not a number. please write a valid index")
        return
    delIndex = int(idxText)
    if(not (delIndex >= 0 and delIndex < len(ranges))):
        print("the index you are searching is not available, please cry about it :)")
        return
    
    r1 = ranges [idxText]

    idxText = input()
    if (not idxText.isnumeric()):
        print("the index that you're searching was not a number. please write a valid index")
        return
    delIndex = int(idxText)
    if(not (delIndex >= 0 and delIndex < len(ranges))):
        print("the index you are searching is not available, please cry about it :)")
        return

    r2 = ranges [idxText]
    
    print(r1.overlaps(r2))
    



functions = {
    "exit": exitFunct,
    "enter": enterFunct,
    "list": listFunct,
    "delete": delFunct,
    "overlapCheck": overlapFunct
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


