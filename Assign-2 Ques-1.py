string = "Python is a case sensitive language"

# a.
print("Length of string:", len(string))

# b.
print("Reversed string:", string[::-1])

# c.
new_string = string[10:27]
print("New string:", new_string)

# d.
new_string = string.replace("a case sensitive", "object oriented")
print("New string:", new_string)

# e.
print("Index of 'a':", string.index("a"))

# f.
new_string = string.replace(" ", "")
print("New string:", new_string)
