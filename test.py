import unittest
import basicpytonscript


class TestSum(unittest.TestCase):


	def returns_with_success(self):
		result = basicpytonscript.generate_final_output()
		
		number_of_unique_products = result["number_of_unique_products"]
		number_of_unique_brands = result["number_of_unique_brands"]
		avg_price = result["avg_price"]

		self.assertEqual(number_of_unique_products, 1)
		#self.assertIsNot(number_of_unique_brands, None)
		#self.assertIsNot(avg_price, None)
