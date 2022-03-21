import unittest
import current_range_calc

class current_range_calc_test(unittest.TestCase):

    input_lst =[3,3,5,4]
    def test_calc_ranges(self):
       self.assertTrue(current_range_calc.calc_ranges(self.input_lst) ==  {(3,5):4})
      
    def test_get_range(self):
      lst = self.input_lst
      lst.sort()
      res = current_range_calc.get_range(lst)
      self.assertTrue([3,4,5] in res)
    
    def test_get_reading_count(self):
      self.assertTrue(current_range_calc.get_reading_count([3,4,5],self.input_lst)==4)

    def test_calc_ranges_invalid(self):
      self.assertTrue(current_range_calc.calc_ranges([3,5,7,9]) ==  {})
    
    def test_export_dict_to_csv(self):
      self.assertTrue(current_range_calc.export_dict_to_csv({(3,5):4})=="Ranges_and_Readings.csv")


if __name__ == '__main__':
  unittest.main()