from argparse import ArgumentError
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
    print("Available Ranges:")
    ranges = kwargs["ranges"]
    en = enumerate(ranges)
    for idx, range in en:
        print(f"{idx} - {range}")

def getValidIndex(ranges):
    rangeIndexText = input()
    if (not rangeIndexText.isnumeric()):
        raise ArgumentError("Argument is not numeric")
    rangeIndex = int(rangeIndexText)
    if(not (rangeIndex >= 0 and rangeIndex < len(ranges))):
        raise IndexError("Index out of range")
    return rangeIndex


def delFunct(**kwargs):
    ranges = kwargs["ranges"]
    if (len(ranges) == 0):
        print("There are no ranges to remove.")
        return
    listFunct(ranges = ranges)
    print(f"What range do you whant to remove? (0-{len(ranges)})")

    try:
        delIndex = getValidIndex(ranges)
        ranges.pop(delIndex)
    except(ArgumentError):
        print("the index that you're searching was not a number. please write a valid index")
        return
    except(IndexError):
        print("the index you are searching is out of range, please cry about it :)")
        return


def overlapFunct(**kwargs):
    ranges = kwargs["ranges"]
    if (len(ranges) == 0):
        print("There are no ranges to check for overlap.")
        return
    listFunct(ranges = ranges)

    try:
        print("Insert the first range")
        firstIndex = getValidIndex(ranges)
        r1 = ranges[firstIndex]
        print(r1)
        print("Insert the second range")
        secondIndex = getValidIndex(ranges)
        r2 = ranges[secondIndex]
        print(r2)
        print(f"The ranges  {r1} and {r2}", end=" ")
        if (r1.overlaps(r2)):
            print("do overlap")
        else:
            print("do not overlap.")
    except(ArgumentError):
        print("The index that you're searching was not a number. Please write a valid index")
        return
    except(IndexError):
        print("The index you are searching is out of range. Please cry about it :( 😿")
        return

functions = {
    "exit": exitFunct,
    "enter": enterFunct,
    "list": listFunct,
    "delete": delFunct,
    "overlapcheck": overlapFunct
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
        print("Issue your next command (or help)")
        usrIn = input().lower()
        os.system("cls")

        if (usrIn in functions.keys()):
            toExecute = functions[usrIn]
            if (toExecute(ranges= rangeList) == -1):
                break
            # program
        else:
            print(f"I did not understand \"{usrIn}\"")


