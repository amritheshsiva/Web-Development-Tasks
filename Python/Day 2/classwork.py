header=""" 
_________________________
\tBOOK RECEIPT
_________________________
"""
title1="Python Basics"
title2="Data Science Intro"
price1=450
price2=600
b1="{}\t\t Rs{}".format(title1,price1)
b2="{}\t Rs{}".format(title2,price2)
total=price1+price2
thanku="thank you for shopping with us!"
receipt=(header+"{}\n{}.\n The total price is {}.\n\n{}".format(b1,b2,total,thanku))
print(receipt.upper())