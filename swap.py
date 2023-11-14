#answer 1:
a = 24
b = 32
 
a = a + b   
b = a - b
a = a - b
 
print("Value of x:", a)
print("Value of y:", b)

#answer 2:
a = 24
b = 32
 
# Swapping using xor
a = a ^ b
b = a ^ b
a = a ^ b
 
print("Value of x:", a)
print("Value of y:", b)