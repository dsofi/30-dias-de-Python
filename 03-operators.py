
# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N') # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume 
print(density, 'kg/m3') 


# Comparison Operators
print('----- Comparison Operators -----') 
print('3 > 2 :', 3 > 2)    # True, because 3 is greater than 2
print('3 >= 2 :',3 >= 2)   # True, because 3 is greater than 2
print('3 < 2 :',3 < 2)     # False,  because 3 is greater than 2
print('2 < 3 :',2 < 3)     # True, because 2 is less than 3
print('2 <= 3 :',2 < 3)    # True, because 2 is less than 3
print('3 == 2 :',2 < 3)    # False, because 3 is not equal to 2
print('3 != 2 :',2 < 3)    # True, because 3 is not equal to 2

# In addition to the above comparison operator Python uses:
# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all')       # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')            # True
print('4 is 2 ** 2:', 4 is 2 ** 2)        # True

# Logical Operators
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True) # True
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False) # True
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False


# Exercises - Day 3
print('----- Exercises - Day 3 -----') 
age =  80
height_example = 1.6
comp_num = 2 + 3j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
print('----- Calcular área de un triángulo -----') 
base = float(input('Ingrese la medida de la base: '))
height = float(input('Ingrese la altura del triángulo: '))
area = 0.5 * base * height
print('El área del triángulo es: ', area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
print('----- Calcular perímetro de un triángulo -----') 
side_a = float(input('Ingrese la medida del lado a: '))
side_b = float(input('Ingrese la medida del lado b: '))
side_c = float(input('Ingrese la medida del lado c: '))
perimeter = (side_a + side_b + side_c)
print('El perímetro del triángulo es: ', perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print('----- Calcular área y perímetro de un rectángulo -----') 
lado_a = float(input('Ingrese el lado a del rectángulo: '))
lado_b = float(input('Ingrese el lado b del rectángulo: '))
area_rect = lado_a * lado_b
perim_rect = 2 * (lado_a + lado_b)
print('El área del rectángulo es: ', area_rect)
print('El perímetro del rectángulo es: ', perim_rect)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print('----- Calcular área y perímetro de un círculo -----') 
radio = float(input('Ingrese el radio del círculo: ')) 
area_circ = 3.14 * radio * radio
perim_circ = 2 * 3.14 * radio
print('El área del círculo es: ', area_circ)
print('El perímetro del círculo es: ', perim_circ)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
inter_x = 2 / 2
inter_y = -2
slope_1 = (0 - inter_y) / (inter_x - 0)
print('Slope 1: ',slope_1)
print('x-intercept: ',inter_x)
print('y-intercept: ',inter_y)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1,y1 = 2,2
x2,y2 = 6,10
slope_2 = (y2-y1)/(x2-x1)
euclidean_distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
print('Slope 2: ',slope_2)
print('Euclidean distance: ',euclidean_distance)

# Compare the slopes in tasks 8 and 9.
print('Slopes are equal? :', slope_2 == slope_1)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
print('----- Calcular el valor de y en (y = x^2 + 6x + 9) -----') 
x = float(input("Ingrese el valor de x: "))
y = x**2 + 6*x + 9
a=1
b=6
c=9
print('Valor de y: ', y)
import cmath
x1_to0 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
x2_to0 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
print('Para que y sea 0, x tiene que ser: ', x1_to0, ' ó : ', x2_to0) 

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_python = len('python')
length_dragon = len('dragon')
falsy_comparison = length_python != length_dragon
print('falsy_comparison: ',falsy_comparison)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
is_on = 'on' in 'phyton' and 'on' in 'dragon'
print('is_on: ',is_on)

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
is_jargon = 'jargon' in 'I hope this course is not full of jargon'
print('is_jargon: ',is_jargon)

# There is no 'on' in both dragon and python
### NO ENTENDI

# Find the length of the text python and convert the value to float and convert it to string
text = 'phyton'
length = len(text)
to_float = float(length)
to_string = str(to_float)
print('text phyton length - to_float: ',to_float)
print('text phyton length - to_string: ',to_string)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = float(input('Ingrese un número para ver si es par: '))
es_par = num  % 2 == 0
print('El numero es par: ', es_par)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_conv = int(2.7)
is_equal = floor_division == int_conv
print('is floor division equal to the int converted value of 2.7? ', is_equal)

# Check if type of '10' is equal to type of 10
is_10_equal = type('10') == type(10)
print("type of '10' is equal to type of 10: ", is_10_equal)

# Check if int('9.8') is equal to 10
float_9_8 = float('9.8')
is_int_equal = int(float_9_8) == 10
print("int('9.8') is equal to 10: ", is_int_equal)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input('Ingrese la cantidad de horas: '))
rate_ph = float(input('Ingrese el precio por hora: '))
pay = hours * rate_ph
print('Su pago es de: ', pay)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person has live. 
years = int(input('Ingrese su edad: '))
seconds = years * 365.25 * 24 * 60 * 60
print(f"Has vivido durante {seconds} segundos")

# Write a Python script that displays the following table
n = 1
while n <= 5:
    print(n, n ** 0, n ** 1, n ** 2, n ** 3)
    n += 1