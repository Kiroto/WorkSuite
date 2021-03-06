from enum import Enum, auto

class TemperatureScale(Enum):
    K = auto(),
    C = auto(),
    F = auto()

class Temperature:
    def __init__(self, value: float, scale : TemperatureScale):
        self.value : float = value
        self._scale : TemperatureScale = scale

    def toKelvin(self):
        if self._scale == TemperatureScale.K:
            return Temperature(self.value, self._scale)
        c = self.toCelsius()
        return Temperature(c.value + 273.15, TemperatureScale.K)

    def toFarenheit(self):
        if self._scale == TemperatureScale.F:
            return Temperature(self.value, self._scale)
        c = self.toCelsius()
        return Temperature((c.value * 9 / 5) + 32, TemperatureScale.F)

    def toCelsius(self):
        if self._scale == TemperatureScale.C:
            return Temperature(self.value, self._scale)
        nv = Temperature(self.value, TemperatureScale.C)
        if (self._scale == TemperatureScale.F):
            nv.value = (self.value - 32) * 5 / 9
        elif (self._scale == TemperatureScale.K):
            nv.value = self.value - 273.15
        return nv


    def toScale(self, scale: TemperatureScale):
        if self._scale == scale:
            return Temperature(self.value, self._scale)
        return {
            TemperatureScale.K: self.toKelvin,
            TemperatureScale.C: self.toCelsius,
            TemperatureScale.F: self.toFarenheit
        }[scale]()

    def __add__(self, other : 'Temperature'):
        nv = other.toScale(self._scale)
        return Temperature(self.value + nv.value, self._scale)

    def __sub__(self, other : 'Temperature'):
        nv = other.toScale(self._scale)
        return Temperature(self.value - nv.value, self._scale)

    def __mul__(self, other : 'Temperature'):
        nv = other.toScale(self._scale)
        return Temperature(self.value * nv.value, self._scale)

    def __truediv__(self, other : 'Temperature'):
        nv = other.toScale(self._scale)
        return Temperature(self.value / nv.value, self._scale)

    def getScale(self):
        return self._scale

    def __str__(self):
        scaleStr = {
            TemperatureScale.K: "K",
            TemperatureScale.C: "C",
            TemperatureScale.F: "F"
        }[self._scale]
        return f"{self.value} {scaleStr}"
