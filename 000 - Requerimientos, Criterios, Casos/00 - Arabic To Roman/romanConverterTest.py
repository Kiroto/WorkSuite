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
        self.assertEqual(isNatural("0.0"), False)
        self.assertEqual(isNatural("9999.585"), False)
        self.assertEqual(isNatural("1.0000000001"), False)

    def test_WhenTrash(self):
        self.assertEqual(isNatural("abracadabra"), False)
        self.assertEqual(isNatural("Teen Wolf"), False)
        self.assertEqual(isNatural("79797-8"), False)
        self.assertEqual(isNatural("7+8"), False)


if __name__ == "__main__":
    unittest.main()
