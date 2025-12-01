import random
price_rice=float(45)
price_sugar=float(40)
price_oil=float(130)
quant_rice=float(3)
quant_sugar=2.5
quant_oil=1.8
total_rice=price_rice*quant_rice
total_sugar=price_sugar*quant_sugar
total_oil=price_oil*quant_oil
print("Total price of rice is",total_rice)
print("Total price of sugar is",total_sugar)
print("Total price of oil is",total_oil)
total=total_rice+total_sugar+total_oil
print("Total bill is",total)
print("Total bill as integer",int(total))
print("Total bill as string",str(total))
del_charge= random.randrange(5,10)
final=total+del_charge
print("Bill including delivery charge",final)
