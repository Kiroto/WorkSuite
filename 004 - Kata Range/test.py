import unittest
from extreme import Extreme
from range import Range

class ExtremeConstructorTest(unittest.TestCase):
    def test_correct_construction(self):
        testExtreme = Extreme(1, True)
        self.assertEqual(testExtreme.value, 1)
        self.assertEqual(testExtreme.isOpen, True)

    def test_incorrect_construction(self):
        didFail = False
        try:
            Extreme(5.1, "fd")
        except TypeError:
            didFail = True
        self.assertTrue(didFail)

class RangeConstructorTest(unittest.TestCase):
    def test_correct_construction(self):
        testRange = Range(Extreme(1, True), Extreme(3, False)) # (1, 3]
        self.assertEqual(testRange.start.value, 1)
        self.assertEqual(testRange.start.isOpen, True)
        self.assertEqual(testRange.end.value, 3)
        self.assertEqual(testRange.end.isOpen, False)

    def test_incorrect_construction(self):
        didFail = False
        try:
            Range(5.1, "fd")
        except TypeError:
            didFail = True
        self.assertTrue(didFail)

class RangeContainsTest(unittest.TestCase):
    def test_do_contain(self):
        fromRange = Range(Extreme(1, True), Extreme(3, False)) # (1, 3]
        comparingRange = Range(Extreme(2, True), Extreme(3, False)) # (1, 3]
        self.assertTrue(fromRange.contains(comparingRange))

    def test_doesnt_contain(self):
        fromRange = Range(Extreme(1, True), Extreme(4, False)) # (1, 4]
        comparingRange = Range(Extreme(4, True), Extreme(6, False)) # (4, 6]
        self.assertFalse(fromRange.contains(comparingRange))

class RangePointsTest(unittest.TestCase):
    def test_empty(self):
        testingRange = Range(Extreme(1, True), Extreme(2, True)) # (1, 2)
        itemList = testingRange.allPoints()
        self.assertListEqual(itemList, [])

if __name__ == "__main__":
    unittest.main()