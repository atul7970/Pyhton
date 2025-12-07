def add_vat(price,vat):
    return price * (100+vat)/100

orders =[100,150,300]

for price in orders:
    final_amount = add_vat(price,10)
    print(f"Original price = {price} and Final amount = {final_amount}")

