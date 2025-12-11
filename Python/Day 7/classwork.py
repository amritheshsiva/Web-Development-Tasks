items = ["milk", "bread", "eggs"]
def add_item(item):
    items.append(item)
def remove_last_item():
    items.pop()
display_item = lambda item: print(f"Item: {item}")
def count_characters(items, index=0):
    if index == len(items):
        return 0
    else:
        return len(items[index]) + count_characters(items, index + 1)
print(count_characters(items))
