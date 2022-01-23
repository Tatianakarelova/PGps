a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
print(a is b)
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print(a is None)