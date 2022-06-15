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
        otherEnd = other.end.value
        selfInitial = self.start.value
        selfEnd = self.end.value

        if (other.start.isOpen) :
            otherInitial += 1
        if (other.end.isOpen) :
            otherEnd -= 1
        if (self.start.isOpen) :
            selfInitial += 1
        if (self.end.isOpen) :
            selfEnd -= 1

        return selfInitial <= otherInitial and selfEnd >= otherEnd