from enum import Enum


class TemperatureScale(Enum):
    Kelvin = 0
    Celsius = 1
    Farenheit = 2

class Temperature:
    def __init__(self: 'Temperature', value: float, scale: TemperatureScale):
        self._value : float = value
        self._scale : TemperatureScale = scale

    def toKelvin(self: 'Temperature') -> 'Temperature':
        nv : float = self._value
        ns : TemperatureScale = self._scale
        if ns == TemperatureScale.Farenheit:
            nv = (self._value - 32) * 5 / 9
            ns = TemperatureScale.Celsius
        if ns == TemperatureScale.Celsius:
            nv += 273.15
        return Temperature (nv, TemperatureScale.Kelvin)

    def toFarenheit(self: 'Temperature') -> 'Temperature':
        ak = self.toKelvin()
        fvalue = ((ak._value - 273.15) * 9 / 5) + 32
        return Temperature(fvalue, TemperatureScale.Farenheit)

    def toCelsius(self: 'Temperature') -> 'Temperature':
        ak = self.toKelvin()
        fvalue = (ak._value - 273.15)
        return Temperature(fvalue, TemperatureScale.Celsius)

    def toScale(self: 'Temperature', scale: TemperatureScale) -> 'Temperature':
        if self._scale == scale:
            return Temperature(self._value, scale)
        return {
            TemperatureScale.Kelvin : self.toKelvin,
            TemperatureScale.Celsius : self.toCelsius,
            TemperatureScale.Farenheit : self.toFarenheit
        }[scale]()

    def __add__(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        ot = other.toScale(self._scale)
        nv = self._value + ot._value
        return Temperature(nv, self._scale)

    def __sub__(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        ot = other.toScale(self._scale)
        nv = self._value - ot._value
        return Temperature(nv, self._scale)

    def __mul__(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        ot = other.toScale(self._scale)
        nv = self._value * ot._value
        return Temperature(nv, self._scale)

    def __truediv__(self: 'Temperature', other: 'Temperature') -> 'Temperature':
        ot = other.toScale(self._scale)
        nv = self._value / ot._value
        return Temperature(nv, self._scale)

    def getScale(self: 'Temperature') -> TemperatureScale:
        return self._scale

    def __str__(self: 'Temperature') -> str:
        return str(max(self._value, int(self._value))) + " " + {
            TemperatureScale.Kelvin : "K",
            TemperatureScale.Celsius : "°C",
            TemperatureScale.Farenheit : "°F"
        }[self._scale]
