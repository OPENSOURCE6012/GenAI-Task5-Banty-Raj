# pyrefly: ignore [missing-import]
def apply_discount(price , percentage):
    """____return the discountprice____"""
    discount_amount = price*(percentage/100)
    return price - discount_amount

def flat_discount(price):
    return price-50    