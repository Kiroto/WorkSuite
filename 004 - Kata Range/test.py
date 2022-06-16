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
        self.assertTrue(fromRange.containsRange(comparingRange))

    def test_doesnt_contain(self):
        fromRange = Range(Extreme(1, True), Extreme(4, False)) # (1, 4]
        comparingRange = Range(Extreme(4, True), Extreme(6, False)) # (4, 6]
        self.assertFalse(fromRange.containsRange(comparingRange))

class RangePointsTest(unittest.TestCase):
    def test_empty(self):
        testingRange = Range(Extreme(1, True), Extreme(2, True)) # (1, 2)
        itemList = testingRange.allPoints()
        self.assertListEqual(itemList, [])

    def test_contents(self):
        testingRange = Range(Extreme(1, False), Extreme(2, False)) # [1, 2]
        itemList = testingRange.allPoints()
        self.assertListEqual(itemList, [1, 2])

class RangeIntContainsTest(unittest.TestCase):
    def test_does_contain(self):
        testingRange = Range(Extreme(1, True), Extreme(6, True)) # (1, 6)
        self.assertTrue(testingRange.containsAll([2,3,4,5]))

    def test_doesnt_contain(self):
        testingRange = Range(Extreme(1, True), Extreme(6, True)) # (1, 6)
        self.assertFalse(testingRange.containsAll([-1,2,3,4,5]))

class RangeContainsAny(unittest.TestCase):
    def test_does_contain(self):
        testingRange = Range(Extreme(1, True), Extreme(6, True)) # (1, 6)
        self.assertTrue(testingRange.any([2,3,4,5]))

    def test_does_contains_just_one(self):
        testingRange = Range(Extreme(1, True), Extreme(6, True)) # (1, 6)
        self.assertTrue(testingRange.any([2,3,4,5,6,8,7,9,8,45,78]))

    def test_doesnt_contain(self):
        testingRange = Range(Extreme(1, True), Extreme(6, True)) # (1, 6)
        self.assertFalse(testingRange.any([-1]))

class RangeEndpointsTest(unittest.TestCase):
    def test_open_endpoints(self):
        testingRange = Range(Extreme(1, True), Extreme(6, True)) # (1, 6)
        self.assertListEqual(testingRange.endPoints(), [2, 5])

    def test_closed_endpoints(self):
        testingRange = Range(Extreme(4, False), Extreme(6, False)) # [4, 6]
        self.assertListEqual(testingRange.endPoints(), [4, 6])


    def test_semiOpen_endpoints(self):
        testingRange = Range(Extreme(1, True), Extreme(6, False)) # (1, 6]
        self.assertListEqual(testingRange.endPoints(), [2, 6])

class RangeOverlapTest(unittest.TestCase):
    def test_does_overlap_right(self):
        testingRange = Range(Extreme(1, True), Extreme(6, True)) # (1, 6)
        comparingRange = Range(Extreme(2, True), Extreme(9, False)) # (2, 9]

        self.assertTrue(testingRange.overlaps(comparingRange))

    def test_does_overlap_left(self):
        comparingRange = Range(Extreme(1, False), Extreme(6, False)) # [1, 6]
        testingRange = Range(Extreme(2, True), Extreme(9, False)) # (2, 9]

        self.assertTrue(testingRange.overlaps(comparingRange))


    def test_does_overlap_contains(self):
        testingRange = Range(Extreme(1, True), Extreme(6, False)) # (1, 6]
        comparingRange = Range(Extreme(2, True), Extreme(3, False)) # (2, 3]

        self.assertTrue(testingRange.overlaps(comparingRange))

    def test_does_overlap_is_contained(self):
        comparingRange = Range(Extreme(1, True), Extreme(6, False)) # (1, 6]
        testingRange = Range(Extreme(2, True), Extreme(3, False)) # (2, 3]

        self.assertTrue(testingRange.overlaps(comparingRange))

    def test_doesnt_overlap_edge(self):
        testingRange = Range(Extreme(1, True), Extreme(6, False)) # (1, 6]
        comparingRange = Range(Extreme(6, True), Extreme(9, False)) # (6, 9]

        self.assertFalse(testingRange.overlaps(comparingRange))

    def test_doesnt_overlap_plain(self):
        testingRange = Range(Extreme(1, True), Extreme(6, False)) # (1, 6]
        comparingRange = Range(Extreme(7, False), Extreme(9, False)) # [7, 9]

        self.assertFalse(testingRange.overlaps(comparingRange))

class RangeEqualsTest(unittest.TestCase):
    def test_self_equals_self(self):
        testingRange = Range(Extreme(3, False), Extreme(5, True)) # [3, 5)

        self.assertTrue(testingRange == testingRange)

    def test_range_not_equals(self):
        testingRange = Range(Extreme(3, False), Extreme(5, True)) # [3, 5)
        otherRange = Range(Extreme(4, False), Extreme(5, True)) # [4, 5)

        self.assertFalse(testingRange == otherRange)

    def test_range_equivalent(self):
        testingRange = Range(Extreme(4, True), Extreme(8, True)) # (4, 8)
        otherRange = Range(Extreme(5, False), Extreme(7, False)) # [5, 7]

        self.assertTrue(testingRange == otherRange)


if __name__ == "__main__":
    unittest.main()