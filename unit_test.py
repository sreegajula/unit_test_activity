import unittest
import calc

class testAdd(unittest.TestCase):
        def test_add(self):
            result = calc.add(4,3)
            self.assertEqual(result,7)

        def test_add_fail(self):
            result = calc.add(4,3)
            self.assertEqual(result,10)

class testSub(unittest.TestCase):
        def test_sub(self):
            result = calc.sub(4,3)
            self.assertEqual(result,1)

        def test_sub_fail(self):
            result = calc.sub(4,3)
            self.assertEqual(result,2)

class testMult(unittest.TestCase):
        def test_mult(self):
            result = calc.mult(4,3)
            self.assertEqual(result,12)

        def test_mult_fail(self):
            result = calc.mult(4,3)
            self.assertEqual(result,7)

class testDiv(unittest.TestCase):
        def test_div(self):
            result = calc.div(9,3)
            self.assertEqual(result,3)

        def test_div_fail(self):
            result = calc.div(9,3)
            self.assertEqual(result,10)



