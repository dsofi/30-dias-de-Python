# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Sofi'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Sofi'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


# Euclidean distance
# d(p,q)^2=(qx-px)^2 + (qy-py)^2

# Para calcular la raiz cuadrada : 
from math import sqrt
print(sqrt(16))

# o también se puede hacer así :
print(16**0.5)

# Datos : p(2,3); q(10,8)
px = 2
py = 3
qx = 10
qy = 8

print(((qx - px)**2 + (qy - py)**2)**0.5) # Resultado : 9.43398