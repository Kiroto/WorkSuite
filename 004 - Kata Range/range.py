from extreme import Extreme

class Range:
    def __init__(self: 'Range', startExtreme: Extreme, endExtreme: Extreme, ) -> None:
        if type(startExtreme) is not Extreme:
            raise TypeError(startExtreme)
        if type(endExtreme) is not Extreme:
            raise TypeError(endExtreme)
        self.start = startExtreme
        self.end = endExtreme

    def containsRange(self: 'Range', other: 'Range') -> bool:
        return self.initialValue() <= other.initialValue() and self.finalValue() >= other.finalValue()

    def initialValue(self: 'Range') -> int:
        selfInitial = self.start.value
        if (self.start.isOpen) :
            selfInitial += 1
        return selfInitial

    def finalValue(self: 'Range') -> int:
        selfLast = self.end.value
        if (self.end.isOpen) :
            selfLast -= 1
        return selfLast


    def allPoints(self: 'Range') -> 'list[int]':
        counter = self.initialValue()
        finalValue = self.finalValue()
        points = []
        
        while (counter  <= finalValue) :
            points.append(counter)
            counter += 1  
        return points