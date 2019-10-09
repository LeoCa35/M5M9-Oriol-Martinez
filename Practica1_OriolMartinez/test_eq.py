import unittest

from solucionadorEquacions import EqPrimG

class TestEquacio(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(EqPrimG('2x + 3 = 7').calcula(),2)


if __name__ == "_main_":
    unittest.main()