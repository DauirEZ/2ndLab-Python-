fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome