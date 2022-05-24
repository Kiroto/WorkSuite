# Manual
These are the instructions for the Temperature API.

## Creating a new Temperature
```python
from kTemperature import Temperature

tooCold = Temperature(45) # Default scale is Kelvin, so this is 45 K
lukewarm = Temperature(37, TemperatureScale.Celsius)
ironMelting = Temperature(2200, TemperatureScale.Farenheit)
mercuryFreezing = Temperature(234.3, TemperatureScale.Kelvin)
```
## Converting temperatures
Temperature conversion creates a new instance with the new type.
```python
from kTemperature import Temperature

kelvinTemperature = Temperature(200, TemperatureScale.Kelvin)                   # 200 K
celsiusTemperature = kelvinTemperature.ToCelsius()                              # -73.15 °C
farenheitTemperature = kelvinTemperature.ToScale(TemperatureScale.Farenheit)    # -99.67
```

## Temperature Arithmetic
Temperature arithmetic through operators creates a new object instance.
```python
from kTemperature import Temperature

a = Temperature(200, TemperatureScale.Kelvin) # 200 K
b = Temperature(400, TemperatureScale.Kelvin) # 400 K

c = a + b # 600 K
d = a - b # -200 K
e = a * b # 80000 K     (Hey, you wanted it~)
f = a / b # 0.5 K       (This is for the homework I swear)

a # Still 200 K
```

## Implicit Conversion
Temperature arithmetic through operators will keep the first temperature's scale
```python
from kTemperature import Temperature

a = Temperature(300, TemperatureScale.Kelvin) # 300 K
b = Temperature(78, TemperatureScale.Celsius) # 78 °C -> 351.15 K

c = a + b # 651.15 K
d = a - b # -151.15 K
e = a * b # 70230 K         (This physically doesn't make sense)
f = a / b # 0.56957169 K    (This should be a ratio not a temperature)

a # Still 300 K

```

## Mutating the Temperature Value
You can mutate a temperature's value by using the non-operator functions.
These functions will return the same object.
```python
from kTemperature import Temperature
a = Temperature(150, TemperatureScale.Farenheit)    # 150 °F
b = Temperature(0, TemperatureScale.Celsius)        # 0 °C -> 32 °F

c = a.Add(b)        # 150 °F + 32 °F = 182 °F
d = a.Substract(b)  # 182 °F - 32 °F = 150 °F
e = a.MultiplyBy(b) # 150 °F * 32 °F = 4800 °F  (Oh man)
f = a.DivideBy(b)   # 4800 °F / 32 °F = 150 °F  (Like, really)

# a === c === d === e === f
# c is 150°F
```

## Mutating the Temperature Scale
You can mutate a temperature's scale by using the transformative To Scale functions.
These functions will return the same object.
```python
from kTemperature import Temperature

kelvinTemperature = Temperature(200, TemperatureScale.Kelvin)                   # 200 K
celsiusTemperature = kelvinTemperature.TToCelsius()                             # -73.15 °C
farenheitTemperature = kelvinTemperature.TToScale(TemperatureScale.Farenheit)   # -99.67 °F

# kelvinTemperature === celsiusTemperature === farenheitTemperature
# kelvinTemperature is -99.67 °F
```
## Getting the temperature string
The temperature string will have the value, if it has decimals; the decimals, a space, and the scale (K, °C or °F).
```python
from kTemperature import Temperature

kelvinTemperature = Temperature(200, TemperatureScale.Kelvin)   # 200 K
print(kelvinTemperature)                                        # 200 K
print(Temperature(150, TemperatureScale.Farenheit))             # 150 °F
tempString = str(kelvinTemperature.ToCelsius())                 # -73.15 °C
```