import unittest
from ssnValidator import validateSsn

class IsNaturalTest(unittest.TestCase):
    def test_PositiveCases(self):
        testCases = [
            "111-11-1111"
            "123-45-6789"
            "899-99-9999"
            "555-47-7789"
        ]
        for testCase in testCases:
            self.assertEqual(validateSsn(testCase), True)

    def test_NegativeCases(self):
        testCases = [
            "999-99-9999"
            "000-55-5555"
            "555-55-0000"
            "555-00-5555"
            "666-66-6666"
            "987-65-4321"
            "Teen Wolf"
            "123456789"
            "111-111-111"
            "1-1-1"
            "1111-1111-1111"
            "555/47/7789"
        ]
        for testCase in testCases:
            self.assertEqual(validateSsn(testCase), False)


if __name__ == "__main__":
    unittest.main()
