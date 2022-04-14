import unittest

from math import log
import calculator



class test(unittest.TestCase):
    def test_root(self):
        self.assertEqual(calculator.square_root(4), 2.0)
        self.assertEqual(calculator.square_root(9), 3.0)
        self.assertEqual(calculator.square_root(0), 0.0)
        self.assertEqual(calculator.square_root(1), 1.0)
        self.assertEqual(calculator.square_root(25), 5.0)
    
    def test_fact(self):
        self.assertEqual(calculator.fact(1), 1)
        self.assertEqual(calculator.fact(0), 1)
        self.assertEqual(calculator.fact(2), 2)
        self.assertEqual(calculator.fact(3), 6)
        self.assertEqual(calculator.fact(5), 120)
        
    def test_log(self):
        self.assertEqual(calculator.nat_log(10), log(10))
        self.assertEqual(calculator.nat_log(1),0)
        self.assertEqual(calculator.nat_log(100), log(100))
        self.assertEqual(calculator.nat_log(893), log(893))
        
    def test_power(self):
        self.assertEqual(calculator.power(1,2),1)
        self.assertEqual(calculator.power(2,2),4)
        self.assertEqual(calculator.power(0,2),0)
        self.assertEqual(calculator.power(6,0),1)
        self.assertEqual(calculator.power(-1,1),-1)
        self.assertEqual(calculator.power(-2,2),4)
        self.assertEqual(calculator.power(-2,3),-8)
        



if(__name__ == "__main__"):
    unittest.main()
