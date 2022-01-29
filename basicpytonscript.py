import requests
import json
from decimal import Decimal
from re import sub
import numpy as np



def make_request():
	request =requests.get('http://www.beautylish.com/rest/interview-product/list')
	json_object = json.loads(request.text)
	result = json_object["products"]
	return result

def clean_data():
	result = make_request()
	result = remove_hidden_deleted_products(result)
	result = convert_price_string_to_float(result)
	result = sort_lowest_to_highest(result)
	result = remove_duplicate_from_list(result)
	return result


def remove_hidden_deleted_products(result):
	for product in result:

		if product["deleted"] == True:
			result.remove(product)

		if product["hidden"] == True:
			result.remove(product)

	return result


def convert_price_string_to_float(result):
	for product in result:
		price_as_string = product["price"].replace("$", "")
		price_as_float = float(price_as_string)
		product["price"] = price_as_float

	return result

def sort_lowest_to_highest(result):
	sorted_json = sorted(result, key=lambda k: k['price'], reverse=False)
	return sorted_json


def remove_duplicate_from_list(result):
	for product1 in result:
		for product2 in result:
			if product1 == product2:
				result.remove(product1)

	return result

def generate_final_output():
	result = clean_data()
	number_of_unique_products = len(result)
	number_of_unique_brands = get_count_of_unique_brands(result)
	avg_price = get_average_price(result)
	output_data = {"number_of_unique_products": number_of_unique_products,
	"number_of_unique_brands": number_of_unique_brands,
	"avg_price": avg_price}
	return output_data


def get_count_of_unique_brands(result):
	for product1 in result:
		for product2 in result:
			if product1["brand_name"] == product2["brand_name"]:
				result.remove(product1)

	unique_brands = len(result)
	return unique_brands


def get_average_price(result):
	total_price = 0
	number_of_products = len(result)
	for product1 in result:
		total_price += product1["price"]

	avg_price = total_price/number_of_products
	return avg_price
