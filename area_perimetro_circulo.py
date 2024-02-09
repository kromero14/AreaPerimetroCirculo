import math

# input
r = input("ingrese el radio")
r = int(r)

# processing
a = math.pi * r**2
p = 2 * math.pi * r

# output
print("El área es: " + str(a))
print("El perímetro es: " + str(p))