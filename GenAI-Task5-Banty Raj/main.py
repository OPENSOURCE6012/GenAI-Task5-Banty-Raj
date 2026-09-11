# main.py

# TASK1



# pyrefly: ignore [missing-import]
from package_folder.math_utils import add,sub,sqrt



print("--- Testing functions ---")

sum_result = add(10, 5)
print(f"10 + 5 = {sum_result}")

diff_result = (20, 8)
print(f"20 - 8 = {diff_result}")


square_result = sqrt(4)
print(f"4 squared = {square_result}")

#TASK2

# pyrefly: ignore [missing-import]
from package_folder.string_utils import capitalize_words,reverse_string,word_count
print("----Testing string_utils----")
sample_txt = "python programing is fun"
print(f" capitalize words:{capitalize_words(sample_txt)}")
print(f" reverse words:{reverse_string(sample_txt)}")
print(f"word count:{word_count(sample_txt)}")


##TASK4

# pyrefly: ignore [missing-import]
from package_folder.shop_package.discount import apply_discount , flat_discount
# pyrefly: ignore [missing-import]
from package_folder.shop_package.billing import calculate_total , apply_tax


print("____discount function____")
print(f"Apply 10% discount to 1000: {apply_discount(1000, 10)}")
print(f"Apply flat discount to 500: {flat_discount(500)}")


print("____Billing Function____")
prices_list = [100, 200, 300]
total_bill = calculate_total(prices_list)
print(f"Calculate total for {prices_list}: {total_bill}")

taxed_amount = apply_tax(total_bill)
print(f"Apply 5% tax to the total bill ({total_bill}): {taxed_amount}")