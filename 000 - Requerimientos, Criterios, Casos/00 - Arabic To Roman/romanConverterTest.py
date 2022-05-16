import unittest
from romanConverter import isNatural

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
        self.assertEqual(isNatural("0.0"), True)
        self.assertEqual(isNatural("9999.585"), True)
        self.assertEqual(isNatural("1.0000000001"), True)

    def test_WhenTrash(self):
        self.assertEqual(isNatural("abracadabra"), True)
        self.assertEqual(isNatural("Teen Wolf"), True)
        self.assertEqual(isNatural("79797-8"), True)
        self.assertEqual(isNatural("7+8"), True)


if __name__ == "__main__":
    unittest.main()
