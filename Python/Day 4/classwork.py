fruits=["apple","banana","orange","pineapple"]
vegetables=["carrot","tomato","cabbage","onion"]
beverages=["tea","coffee","soda"]
fruits.append("kiwi")
vegetables.insert(1,"spinach")
beverages.pop()
inventory=[fruits,vegetables,beverages]
print(fruits[0:2])
print(vegetables[-1])
p= [len(x) for x in fruits]
print(p)
print("Water" in beverages)
first_item=(fruits[0],vegetables[0],beverages[0])
