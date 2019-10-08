from solucionadorEquacions import EqPrimG

import unittest


class TestEquacio(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(EqPrimG('2x + 3 = 7').calcula().2)