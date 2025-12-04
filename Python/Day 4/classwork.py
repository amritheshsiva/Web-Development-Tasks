fruits=["apple","banana","orange","pineapple"]
vegetables=["carrot","tomato","cabbage","onion"]
beverages=["tea","coffee","soda"]
fruits.append("kiwi")
vegetables.insert(1,"spinache")
beverages.pop()
inventory=fruits+vegetables+beverages
print(fruits[0:2])
print(vegetables[:-1])
p= [len(x) for x in fruits]
print(p)
print("Water" in beverages)