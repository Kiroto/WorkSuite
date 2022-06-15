import unittest
from extreme import Extreme


class ExtremeConstructorTest(unittest.TestCase):
    def test_correct_construction(self):
        testExtreme = Extreme(1, True)
        self.assertEqual(testExtreme.value, 1)
        self.assertEqual(testExtreme.open, True)

    def test_incorrect_construction(self):
        didFail = False
        try:
            Extreme(5.1, "fd")
        except TypeError:
            didFail = True
        self.assertTrue(didFail)
    
class RangeConstructorTest(unittest.TestCase):
    def test_correct_construction(self):
        testRange = Range(1, True)

if __name__ == "__main__":
    unittest.main()