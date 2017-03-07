import unittest
from prime_solution import prime_num

class prime_test(unnitest.TestCase):
	 def test_if_input_is_less_than_zero(self):
	 	with self.assertRaises(ValueError, msg='Error negative number entered'):
	 		prime_num(-1)

	 def test_if_output_is_list(self):
            result = prime_numbers(20)
            self.assertIsInstance(prime_numbers(20), list, msg='Output must be of type list'):
		

if __name__=="__main__":
    unittest.main()
   
    
