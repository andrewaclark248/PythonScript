import unittest
import basicpytonscript


class TestScript(unittest.TestCase):


	def test_returns_with_success_1(self):
		result = basicpytonscript.generate_final_output()
		
		number_of_unique_products = result["number_of_unique_products"]
		number_of_unique_brands = result["number_of_unique_brands"]
		avg_price = result["avg_price"]

		self.assertIsNot(number_of_unique_products, None)
		self.assertIsNot(number_of_unique_brands, None)
		self.assertIsNot(avg_price, None)


	def test_correct_number_of_unique_products(self):
		result = basicpytonscript.generate_final_output()
		
		number_of_unique_products = result["number_of_unique_products"]
		products = basicpytonscript.clean_data()
		actual_number_of_unique_products = len(products)

		self.assertEqual(number_of_unique_products, actual_number_of_unique_products)
