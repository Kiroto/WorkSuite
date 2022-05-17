import unittest
from romanConverter import (isNatural, transformToRomanNumeral)


class IsNaturalTest(unittest.TestCase):
    def test_WhenNegative(self):
        self.assertEqual(isNatural("-89"), False)
        self.assertEqual(isNatural("-1"), False)
        self.assertEqual(isNatural("-0"), False)

    def test_WhenPositive(self):
        self.assertEqual(isNatural("89"), True)
        self.assertEqual(isNatural("1"), True)
        self.assertEqual(isNatural("1000000"), True)

    def test_WhenDecimal(self):
        self.assertEqual(isNatural("0.0"), False)
        self.assertEqual(isNatural("9999.585"), False)
        self.assertEqual(isNatural("1.0000000001"), False)

    def text_WhenZero(self):
        self.assertEqual(isNatural("0"), False)

    def test_WhenTrash(self):
        self.assertEqual(isNatural("abracadabra"), False)
        self.assertEqual(isNatural("Teen Wolf"), False)
        self.assertEqual(isNatural("79797-8"), False)
        self.assertEqual(isNatural("7+8"), False)


class ConversionTest(unittest.TestCase):
    def test_BaseNumbers(self):
        self.assertEqual(transformToRomanNumeral(1), (" ", "I"))
        self.assertEqual(transformToRomanNumeral(5), (" ", "V"))
        self.assertEqual(transformToRomanNumeral(10), (" ", "X"))
        self.assertEqual(transformToRomanNumeral(50), (" ", "L"))
        self.assertEqual(transformToRomanNumeral(100), (" ", "C"))
        self.assertEqual(transformToRomanNumeral(500), (" ", "D"))
        self.assertEqual(transformToRomanNumeral(1000), ("_", "I"))
        self.assertEqual(transformToRomanNumeral(5000), ("_", "V"))
        self.assertEqual(transformToRomanNumeral(10000), ("_", "X"))
        self.assertEqual(transformToRomanNumeral(50000), ("_", "L"))
        self.assertEqual(transformToRomanNumeral(100000), ("_", "C"))
        self.assertEqual(transformToRomanNumeral(500000), ("_", "D"))
        self.assertEqual(transformToRomanNumeral(1000000), ("_", "M"))
        self.assertEqual(transformToRomanNumeral(2000000), ("__", "MM"))

    def test_NumberCombination(self):
        self.assertEqual(transformToRomanNumeral(12), ("   ", "XII"))
        self.assertEqual(transformToRomanNumeral(58), ("     ", "LVIII"))

    def test_NumberSpecial(self):
        self.assertEqual(transformToRomanNumeral(39), ("     ", "XXXIX"))
        self.assertEqual(transformToRomanNumeral(49), ("    ", "XLIX"))


if __name__ == "__main__":
    unittest.main()
