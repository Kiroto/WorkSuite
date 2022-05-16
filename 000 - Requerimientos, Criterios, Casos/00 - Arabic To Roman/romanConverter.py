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
            top = " "
        return (top,self.symbol)


romanNumerals = [
    RomanNumeral(1, "I", Ruleset.BaseOne),
    RomanNumeral(5, "V", Ruleset.BaseFive),
    RomanNumeral(10, "X", Ruleset.BaseOne),
    RomanNumeral(50, "L", Ruleset.BaseFive),
    RomanNumeral(100, "C", Ruleset.BaseOne),
    RomanNumeral(500, "D", Ruleset.BaseFive),
    RomanNumeral(1000, "M", Ruleset.BaseOne),
]

# Returns true if:
# is not negative
# is not rationed
def isNatural(numberString: str):
    return bool(re.search("[^0-9]", numberString))


