
import basicpytonscript

result = basicpytonscript.generate_final_output()

print("number of unique products: " + str(result["number_of_unique_products"]))
print("number of unique brands: " + str(result["number_of_unique_brands"]))
print("avg price: "+ str(result["avg_price"]))
