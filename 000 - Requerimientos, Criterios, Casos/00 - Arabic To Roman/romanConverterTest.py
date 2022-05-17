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

    def test_WhenTrash(self):
        self.assertEqual(isNatural("abracadabra"), False)
        self.assertEqual(isNatural("Teen Wolf"), False)
        self.assertEqual(isNatural("79797-8"), False)
        self.assertEqual(isNatural("7+8"), False)


class ConversionTest(unittest.TestCase):
    def test_BaseNumbers(self):
        self.assertEqual(transformToRomanNumeral(1), " \nI")
        self.assertEqual(transformToRomanNumeral(5), " \nV")
        self.assertEqual(transformToRomanNumeral(10), " \nX")
        self.assertEqual(transformToRomanNumeral(50), " \nL")
        self.assertEqual(transformToRomanNumeral(100), " \nC")
        self.assertEqual(transformToRomanNumeral(500), " \nD")
        self.assertEqual(transformToRomanNumeral(1000), "_\nI")
        self.assertEqual(transformToRomanNumeral(5000), "_\nV")
        self.assertEqual(transformToRomanNumeral(10000), "_\nX")
        self.assertEqual(transformToRomanNumeral(50000), "_\nL")
        self.assertEqual(transformToRomanNumeral(100000), "_\nC")
        self.assertEqual(transformToRomanNumeral(500000), "_\nD")
        self.assertEqual(transformToRomanNumeral(1000000), "_\nM")
        self.assertEqual(transformToRomanNumeral(2000000), "__\nMM")

    def test_NumberCombination(self):
        self.assertEqual(transformToRomanNumeral(12), "   \nXII")
        self.assertEqual(transformToRomanNumeral(58), "     \nLVIII")

    def test_NumberSpecial(self):
        self.assertEqual(transformToRomanNumeral(39), "     \nXXXIX")
        self.assertEqual(transformToRomanNumeral(49), "    \nXLIX")


if __name__ == "__main__":
    unittest.main()
