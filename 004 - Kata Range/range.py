from extreme import Extreme

class Range:
    def __init__(self: 'Range', startExtreme: Extreme, endExtreme: Extreme, ) -> None:
        if type(startExtreme) is not Extreme:
            raise TypeError(startExtreme)
        if type(endExtreme) is not Extreme:
            raise TypeError(endExtreme)
        self.start = startExtreme
        self.end = endExtreme

    def contains(self: 'Range', other: 'Range') -> bool:
        otherInitial = other.start.value
        if (other.start.isOpen)
