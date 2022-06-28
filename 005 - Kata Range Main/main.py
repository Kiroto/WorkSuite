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
        print("Select the first range")
        firstIndex = getValidIndex(ranges)
        r1 = ranges[firstIndex]
        print(r1)
        print("Select the second range")
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

def allFromListFunct(**kwargs):
    ranges = kwargs["ranges"]
    if (len(ranges) == 0):
        print("There are no ranges to check for contents.")
        return

    print("Write a list of numbers (separated by commas)")
    print("Ex. \"5, 7, 8\"")
    inputText = input()
    numberTextList = inputText.split(",")
    numberList = []
    for numberText in numberTextList:
        numberText = numberText.strip(" ")
        if (not numberText.isnumeric()):
            print(f"{numberText} is not an integer")
            return
        numberList.append(int(numberText))
    listFunct(ranges = ranges)
    try:
        print("Select the range to compare")
        rangeIndex = getValidIndex(ranges)
        range = ranges[rangeIndex]
        print(f"The range {range}", end=" ")
        if (range.containsAll(numberList)):
            print("does contain all of", end=" ")
        else:
            print("doesn't contain all of", end = " ")
        print(numberList)
    except(ArgumentError):
        print("The index that you're searching was not a number. Please write a valid index")
        return
    except(IndexError):
        print("The index you are searching is out of range. Please cry about it :( 😿")
        return

def allPointsFunct(**kwargs):
        ranges = kwargs["ranges"]
        if (len(ranges) == 0):
            print("There are no ranges to check.")
            return
        listFunct(ranges = ranges)
        print(f"What range do you whant check all points? (0-{len(ranges)})")
  
        try:
            delIndex = getValidIndex(ranges)
            r1 = ranges[delIndex]
            print(r1.allPoints())
        except(ArgumentError):
            print("the index that you're searching was not a number. please write a valid index")
            return
        except(IndexError):
            print("the index you are searching is out of range, please cry about it :)")
            return

def getExtremeFunct(**kwargs):
        ranges = kwargs["ranges"]
        if (len(ranges) == 0):
            print("There are no ranges to check.")
            return
        listFunct(ranges = ranges)
        print(f"What range do you whant check? (0-{len(ranges)})")
  
        try:
            delIndex = getValidIndex(ranges)
            r1 = ranges[delIndex]
            print(r1.endPoints())
        except(ArgumentError):
            print("the index that you're searching was not a number. please write a valid index")
            return
        except(IndexError):
            print("the index you are searching is out of range, please cry about it :)")
            return

functions = {
    "exit": exitFunct,
    "enter": enterFunct,
    "list": listFunct,
    "delete": delFunct,
    "overlapcheck": overlapFunct,
    "allfromlist": allFromListFunct,
    "allpoints": allPointsFunct,
    "getextremes": getExtremeFunct
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


