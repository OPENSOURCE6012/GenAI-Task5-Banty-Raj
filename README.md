Assignment 5: Importing, Creating Modules & Packages
Problem Statement

You are working as a Python Developer for a small utility tools team. The company wants to organize code into modules and packages to make the project reusable and scalable. Your task is to create simple modules, import them, and organize them into a package.

This assignment focuses ONLY on:

    Creating Python modules (.py files)
    Importing modules
    Creating packages using __init__.py
    Using from module import function and import module
    Keeping the assignment simple and beginner-friendly

Restrictions

    Do NOT use OOP, exceptions, or file I/O beyond creating .py files.
    Keep function logic simple.
    Focus is on understanding modules & packages ONLY.

Folder Structure

Your final folder structure should look exactly like this:

package_folder/
├── main.py
├── math_utils.py
├── string_utils.py
└── shop_package/
    ├── __init__.py
    ├── discount.py
    └── billing.py

Tasks Overview
Task 1: Create a Simple Module (math_utils.py)

Create a module math_utils.py with the following functions:

    add(a, b) → returns a + b

    subtract(a, b) → returns a - b

    square(n) → returns n²

Requirement: In main.py, import this module in two different ways (import math_utils and from math_utils import square) and test all functions.
Task 2: Create Another Module (string_utils.py)

Create a module string_utils.py with the following functions:

    capitalize_words(text) → returns text with each word capitalized

    reverse_string(text) → returns reversed string

    word_count(text) → returns number of words in the text

Requirement: Import this module in main.py and test all functions.
Task 3: Create a Simple Package (shop_package)

Inside the shop_package/ folder, create the following files:

discount.py

    apply_discount(price, percent) → returns discounted price

    flat_discount(price) → always subtracts 50 from price

billing.py

    calculate_total(prices) → returns total bill (sum of all prices)

    apply_tax(amount) → adds 5% tax

__init__.py

    Leave it empty OR add imports to allow calling functions directly from the package:
    Python

    from .discount import apply_discount, flat_discount
    from .billing import calculate_total, apply_tax

Task 4: Importing the Package in main.py

In main.py, do the following:

    import shop_package.discount as disc

    from shop_package.billing import calculate_total

    Call every function inside the package.

Example Usage:
Python

print(disc.apply_discount(1000, 10))
print(calculate_total([100, 200, 300]))    

