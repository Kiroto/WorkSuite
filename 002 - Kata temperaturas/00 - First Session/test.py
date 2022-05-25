import unittest
from kTemperature import Temperature, TemperatureScale



class ConstructorTests(unittest.TestCase):
    CONSTRUCTION_DATA = [
            (5, TemperatureScale.CELSIUS),
            (10, TemperatureScale.FARENHEIT),
            (15, TemperatureScale.KELVIN),
        ]
    def test_construction(self):
        for data in ConstructorTests.CONSTRUCTION_DATA:
            temp = Temperature(data[0], data[1])
            self.assertEqual(temp.value, data[0])
            self.assertEqual(temp._scale, data[1])

class GetterTests(unittest.TestCase):
    CONSTRUCTION_DATA = [
            (7, TemperatureScale.CELSIUS),
            (8, TemperatureScale.FARENHEIT),
            (9, TemperatureScale.KELVIN),
        ]
    def test_construction(self):
        for data in GetterTests.CONSTRUCTION_DATA:
            temp = Temperature(data[0], data[1])
            self.assertEqual(temp.getScale(), data[1])


class ArithmeticTests(unittest.TestCase):
    TEST_TEMPS = [
        Temperature(1, TemperatureScale.CELSIUS),
        Temperature(3, TemperatureScale.CELSIUS),
        Temperature(5, TemperatureScale.KELVIN),
        Temperature(7, TemperatureScale.KELVIN),
        Temperature(11, TemperatureScale.FARENHEIT),
        Temperature(13, TemperatureScale.FARENHEIT),
    ]

    def test_addition(self):
        celsius1 = ArithmeticTests.TEST_TEMPS[0]
        celsius2 = ArithmeticTests.TEST_TEMPS[1]
        kelvin1 = ArithmeticTests.TEST_TEMPS[2]
        kelvin2 = ArithmeticTests.TEST_TEMPS[3]
        farenheit1 = ArithmeticTests.TEST_TEMPS[4]
        farenheit2 = ArithmeticTests.TEST_TEMPS[5]
        testCases = [
            (celsius1, celsius2, 4),
            (kelvin1, kelvin2, 12),
            (farenheit1, farenheit2, 24),
            (celsius1, kelvin1, -267.15),
            (celsius1, farenheit1, -10.666),
            (kelvin1, celsius2, 281.15),
            (kelvin1, farenheit1, 266.483),
            (farenheit1, celsius2, 48.4),
            (farenheit1, kelvin2, -436.07)
        ]
        for testCase in testCases:
            tsum = (testCase[0] + testCase[1])
            self.assertAlmostEqual(tsum.value, testCase[2], 2)
            self.assertEqual(tsum.getScale(), testCase[0].getScale())

    def test_subtraction(self):
        celsius1 = ArithmeticTests.TEST_TEMPS[0]
        celsius2 = ArithmeticTests.TEST_TEMPS[1]
        kelvin1 = ArithmeticTests.TEST_TEMPS[2]
        kelvin2 = ArithmeticTests.TEST_TEMPS[3]
        farenheit1 = ArithmeticTests.TEST_TEMPS[4]
        farenheit2 = ArithmeticTests.TEST_TEMPS[5]
        testCases = [
            (celsius1, celsius2, -2),
            (kelvin1, kelvin2, -2),
            (farenheit1, farenheit2, -2),
            (celsius1, kelvin1, 269.15),
            (celsius1, farenheit1, 12.666),
            (kelvin1, celsius2, -271.15),
            (kelvin1, farenheit1, -256.483),
            (farenheit1, celsius2, -26.4),
            (farenheit1, kelvin2, 458.07)
        ]
        for testCase in testCases:
            tsum = (testCase[0] - testCase[1])
            self.assertAlmostEqual(tsum.value, testCase[2], 2)
            self.assertEqual(tsum.getScale(), testCase[0].getScale())

    def test_multiplication(self):
        celsius1 = ArithmeticTests.TEST_TEMPS[0]
        celsius2 = ArithmeticTests.TEST_TEMPS[1]
        kelvin1 = ArithmeticTests.TEST_TEMPS[2]
        kelvin2 = ArithmeticTests.TEST_TEMPS[3]
        farenheit1 = ArithmeticTests.TEST_TEMPS[4]
        farenheit2 = ArithmeticTests.TEST_TEMPS[5]
        testCases = [
            (celsius1, celsius2, 3),
            (kelvin1, kelvin2, 35),
            (farenheit1, farenheit2, 143),
            (celsius1, kelvin1, -268.15),
            (celsius1, farenheit1, -11.666),
            (kelvin1, celsius2, 1380.75),
            (kelvin1, farenheit1, 1307.416),
            (farenheit1, celsius2, 411.4),
            (farenheit1, kelvin2, -4917.769),
        ]
        for testCase in testCases:
            tsum = (testCase[0] * testCase[1])
            self.assertAlmostEqual(tsum.value, testCase[2], 2)
            self.assertEqual(tsum.getScale(), testCase[0].getScale())

    def test_division(self):
        print("div")
        celsius1 = ArithmeticTests.TEST_TEMPS[0]
        celsius2 = ArithmeticTests.TEST_TEMPS[1]
        kelvin1 = ArithmeticTests.TEST_TEMPS[2]
        kelvin2 = ArithmeticTests.TEST_TEMPS[3]
        farenheit1 = ArithmeticTests.TEST_TEMPS[4]
        farenheit2 = ArithmeticTests.TEST_TEMPS[5]
        testCases = [
            (celsius1, celsius2, 0.333),
            (kelvin1, kelvin2, 0.714),
            (farenheit1, farenheit2, 0.846),
            (celsius1, kelvin1, -0.003),
            (celsius1, farenheit1, -0.085),
            (kelvin1, celsius2,  0.018),
            (kelvin1, farenheit1,  0.019),
            (farenheit1, celsius2,  0.294),
            (farenheit1, kelvin2, -0.024),
        ]
        for testCase in testCases:
            tsum = (testCase[0] / testCase[1])
            self.assertAlmostEqual(tsum.value, testCase[2], 2)
            self.assertEqual(tsum.getScale(), testCase[0].getScale())

class StringTests(unittest.TestCase):
    TEST_TEMPS = [
        (Temperature(1, TemperatureScale.CELSIUS), "1 °C"),
        (Temperature(3, TemperatureScale.CELSIUS), "3 °C"),
        (Temperature(5, TemperatureScale.KELVIN), "5 K"),
        (Temperature(7, TemperatureScale.KELVIN), "7 K"),
        (Temperature(11, TemperatureScale.FARENHEIT), "11 °F"),
        (Temperature(13, TemperatureScale.FARENHEIT), "13 °F"),
    ]
    def test_Strings(self):
        for test in StringTests.TEST_TEMPS:
            self.assertEqual(str(test[0]), test[1])

if __name__ == "__main__":
    unittest.main()