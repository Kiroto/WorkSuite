from enum import Enum
import re


class Ruleset(Enum):
    BaseFive = 0    # V L D
    BaseOne = 1     # I X C M
    MaxValue = 2    # /M

class RomanNumeral:
    def __init__(self, value: int, symbol: str, ruleset: Ruleset, isMultiplied: bool = False):
        self.value = value
        self.symbol = symbol
        self.isMultiplied = isMultiplied
        self.ruleset = ruleset

    def toStringTuple(self):
        top = " "
        if (self.isMultiplied):
            top = "_"
        return (top, self.symbol)


romanNumeralList = [
    RomanNumeral(1, "I", Ruleset.BaseOne),
    RomanNumeral(5, "V", Ruleset.BaseFive),
    RomanNumeral(10, "X", Ruleset.BaseOne),
    RomanNumeral(50, "L", Ruleset.BaseFive),
    RomanNumeral(100, "C", Ruleset.BaseOne),
    RomanNumeral(500, "D", Ruleset.BaseFive),
    RomanNumeral(1000, "I", Ruleset.BaseOne, True),
    RomanNumeral(5000, "V", Ruleset.BaseFive, True),
    RomanNumeral(10000, "X", Ruleset.BaseOne, True),
    RomanNumeral(50000, "L", Ruleset.BaseFive, True),
    RomanNumeral(100000, "C", Ruleset.BaseOne, True),
    RomanNumeral(500000, "D", Ruleset.BaseFive, True),
    RomanNumeral(1000000, "M", Ruleset.MaxValue, True),
]

romanNumeralList.reverse()

# Returns true if:
# is not negative
# is not rationed
def isNatural(numberString: str):
    matchObj = re.search("[^0-9]", numberString)
    trueValue = not bool(matchObj)
    return trueValue

def transformToRomanNumeral(number: int):
    romanNumeralTop = ""
    romanNumerals = ""
    while(number > 0):
        for idx, numeral in enumerate(romanNumeralList):
            while (number >= numeral.value):
                numeralTuple = numeral.toStringTuple()
                romanNumeralTop += numeralTuple[0]
                romanNumerals += numeralTuple[1]
                number -= numeral.value
    return romanNumeralTop + "\n" + romanNumerals

