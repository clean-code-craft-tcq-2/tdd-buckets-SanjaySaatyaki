import unittest
import current_range_calc
import random

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

    def test_remove_invalid_data_with_valid_data(self):
      input_lst = random.sample(range(0, 4094), 7)
      self.assertTrue(current_range_calc.remove_invalid_data(input_lst,4094) ==  input_lst)

    def test_remove_invalid_data_with_invalid_data(self):
      input_lst = random.sample(range(0, 4094), 7)
      input_lst.append(random.randint(4094,10000))
      self.assertTrue(current_range_calc.remove_invalid_data(input_lst,4094) ==  input_lst[0:-1])

    def test_A2D_12BtoAmps_convertor(self):
      input_lst = [2223, 2214, 1190, 658, 2103, 9, 2588]
      self.assertTrue(current_range_calc.A2D_12BtoAmps_convertor(input_lst)==[5, 5, 3, 2, 5, 0, 6])
    
    def test_A2D_10BtoAmps_convertor(self):
      input_lst = [48, 21, 327, 839, 184, 51, 642]
      self.assertTrue(current_range_calc.A2D_10BtoAmps_convertor(input_lst)==[14, 14, 5, 10, 10, 14, 4])
    
    def test_calc_ranges_from_sensor_12b(self):
      input_lst = [2223, 2214, 1190, 658, 2103, 9, 2588]
      sensor = "A2D_12B"
      self.assertTrue(current_range_calc.calc_ranges_from_sensor(input_lst,sensor)=={(2, 3): 2, (5, 6): 4})
    
    def test_calc_ranges_from_sensor_10b(self):
      input_lst = [48, 21, 327, 839, 184, 51, 642]
      sensor = "A2D_10B"
      self.assertTrue(current_range_calc.calc_ranges_from_sensor(input_lst,sensor)=={(4, 5): 2})



if __name__ == '__main__':
  unittest.main()