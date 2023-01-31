fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
# newlist = [expression for item in iterable if condition == True] (its syntax)
# The return value is a new list, leaving the old list unchanged.