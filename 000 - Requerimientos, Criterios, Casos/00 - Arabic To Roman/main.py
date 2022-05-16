from enum import Enum
from typing import overload


class Ruleset(Enum):
    BaseFive = 0    # V L D
    BaseOne = 1     # I X C M
    MaxValue = 2    # /M


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

class RomanNumeral:
    def __init__(self, value: int, symbol: str, ruleset: Ruleset, isMultiplied: bool = False):
        self.value = value
        self.symbol = symbol
        self.isMultiplied = isMultiplied
        self.ruleset = ruleset


romanNumerals = [
    RomanNumeral(1, "I", Ruleset.BaseOne),
    RomanNumeral(5, "V", Ruleset.BaseFive),
    RomanNumeral(10, "X", Ruleset.BaseOne),
    RomanNumeral(50, "L", Ruleset.BaseFive),
    RomanNumeral(100, "C", Ruleset.BaseOne),
    RomanNumeral(500, "D", Ruleset.BaseFive),
    RomanNumeral(1000, "M", Ruleset.BaseOne),
]


