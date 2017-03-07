import unittest
from prime_solution import prime_num

class prime_test(unnitest.TestCase):
	 def test_if_input_is_less_than_zero(self):
	 	with self.assertRaises(ValueError, msg='Error negative number entered'):
	 		prime_num(-1)


if __name__=="__main__":
    unittest.main()
   
    
