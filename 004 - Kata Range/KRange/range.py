from .extreme import Extreme

class Range:
    def __init__(self: 'Range', startExtreme: Extreme, endExtreme: Extreme, ) -> None:
        if type(startExtreme) is not Extreme:
            raise TypeError(startExtreme)
        if type(endExtreme) is not Extreme:
            raise TypeError(endExtreme)
        if (startExtreme.value > endExtreme.value):
            temp = endExtreme
            endExtreme = startExtreme
            startExtreme = temp
        self.start = startExtreme
        self.end = endExtreme

    def containsAll(self: 'Range', intList: 'list[int]') -> bool :
        initialValue = self.initialValue()
        endValue = self.finalValue()

        for item in intList:
            if item < initialValue or item > endValue :
                return False
        return True

    def any(self: 'Range', intList: 'list[int]') -> bool :
        initialValue = self.initialValue()
        endValue = self.finalValue()

        for item in intList:
            if item >= initialValue and item <= endValue :
                return True
        return False

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

    def endPoints(self: 'Range') -> 'list[int]':
        endpoints = [self.initialValue(), self.finalValue()]
        return endpoints

    def overlaps(self: 'Range', other: 'Range') -> bool:
        otherContains = other.any([self.initialValue(), self.finalValue()])
        Icontain = self.any([other.initialValue(), other.finalValue()])
        return otherContains or Icontain

    def __eq__(self: 'Range', other: 'Range') -> bool:
        return self.initialValue() == other.initialValue() and self.finalValue() == other.finalValue()

    def __str__(self: 'Range'):
        startChar = "["
        if (self.start.isOpen):
            startChar = "("

        endChar = "]"
        if (self.end.isOpen):
            endChar = ")"
        return f"{startChar}{self.start.value}, {self.end.value}{endChar}"