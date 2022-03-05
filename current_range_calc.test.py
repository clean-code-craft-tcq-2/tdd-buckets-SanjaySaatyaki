import unittest
import current_range_calc

class current_range_calc_test(unittest.TestCase):
    
    def test_calc_ranges(self):
       self.assertTrue(current_range_calc.calc_ranges([3,3,5,4]) ==  4)



if __name__ == '__main__':
  unittest.main()