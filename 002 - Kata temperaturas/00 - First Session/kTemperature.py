from enum import Enum, auto


class TemperatureScale(Enum):
    CELSIUS = auto()
    KELVIN = auto()
    FARENHEIT = auto()

class Temperature:
    def __init__(self: 'Temperature', value: float, scale: TemperatureScale = TemperatureScale.KELVIN):
        self.value = value
        self._scale = scale

    def toFarenheit(self: 'Temperature') -> 'Temperature':
        value = self.value
        scale = self._scale
        if (scale == TemperatureScale.KELVIN):
            nv = self.toCelsius()
            value = nv.value
            scale = nv._scale
        if (scale == TemperatureScale.CELSIUS):
            value = (value * 9/5) + 32
        return Temperature(value, TemperatureScale.FARENHEIT)

    def toCelsius(self: 'Temperature') -> 'Temperature':
        value = self.value
        scale = self._scale
        if (scale == TemperatureScale.FARENHEIT):
            nv = self.toKelvin()
            value = nv.value
            scale = nv._scale
        if (scale == TemperatureScale.KELVIN):
            value -= 273.15
        return Temperature(value, TemperatureScale.CELSIUS)

    def toKelvin(self: 'Temperature') -> 'Temperature':
        value = self.value
        scale = self._scale
        if (scale == TemperatureScale.CELSIUS):
            nv = self.toFarenheit()
            value = nv.value
            scale = nv._scale
        if (scale == TemperatureScale.FARENHEIT):
            value = ((value-32) * 5/9) + 273.15
        return Temperature(value, TemperatureScale.KELVIN)

    # Returns a new temperature instance of the new scale
    def toScale(self: 'Temperature', newScale : TemperatureScale) -> 'Temperature':
        return {
            TemperatureScale.KELVIN : self.toKelvin,
            TemperatureScale.CELSIUS : self.toCelsius,
            TemperatureScale.FARENHEIT: self.toFarenheit
        }[newScale]()

    # Operation Override
    def __add__(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        newTemp = other.toScale(self._scale)
        return Temperature(self.value + newTemp.value, self._scale)

    def __sub__(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        newTemp = other.toScale(self._scale)
        return Temperature(self.value - newTemp.value, self._scale)

    def __mul__(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        newTemp = other.toScale(self._scale)
        return Temperature(self.value * newTemp.value, self._scale)

    def __truediv__(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        newTemp = other.toScale(self._scale)
        return Temperature(self.value / newTemp.value, self._scale)

    # Mutation Operations
    def add(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        newTemp = other.toScale(self._scale)
        self.value += newTemp.value
        return self

    def subtract(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        newTemp = other.toScale(self._scale)
        self.value -= newTemp.value
        return self

    def multiplyBy(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        newTemp = other.toScale(self._scale)
        self.value *= newTemp.value
        return self

    def divideBy(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        newTemp = other.toScale(self._scale)
        self.value /= newTemp.value
        return self

    def __str__(self: 'Temperature') -> str:
        scaleString = {
            TemperatureScale.KELVIN : "K",
            TemperatureScale.CELSIUS : "°C",
            TemperatureScale.FARENHEIT: "°F"
        }[self._scale]
        if (int(self.value) == self.value):
            self.value = int(self.value)
        return f"{self.value} {scaleString}"

    def toString(self) -> str:
        return str(self)

    def getScale(self) -> TemperatureScale:
        return self._scale
