# Variables en Python se escriben con snake_case
first_name = 'Sofi'
country = 'Argentina'
año = 2023
esta_estudiando = True
skills = ['HTML','CSS','JS','Python']
person_info = {
    'firstname':'Sofi',
    'country':'Argentina',
    'learning':'Python'
}

print('First name:', first_name)
print('First name length:', len(first_name))
print('Skills:', skills)
print('Person information:', person_info)

# Se pueden declarar múltiples variables en una sola linea
name2, country2, skills2 = 'Juancito', 'Chile', ['Angular','React']
print('First name 2:', name2)
print('Country 2:', country2)

# Asignar datos desde los inputs del usuario
nombre_usuario = input('Cómo te llamas? ')
edad_usuario = input('Cuántos años tenes? ')
print('Tu nombre es', nombre_usuario)
print('Tu edad es',edad_usuario)

# Casting - convertir tipos de datos ---

# int to float
num_int = 10
num_float = float(num_int)

# float to int
gravity_float = 9.81
gravity_int = int(gravity_float)

# int to str
num_str = str(num_int)

# str to int or float
int(num_str)
float(num_str)

# str to list
nombre = 'Sofi'
nombre_to_list = list(nombre) #['S', 'o', 'f', 'i']

# Some of the most commonly used Python built-in functions are the following: 
# print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir().

num_one = 5
num_two = 4
total = (num_one + num_two)
diff = (num_two - num_one)
product = (num_one * num_two)
division = (num_one / num_two)
remainder = (num_two % num_one)
exp = (num_one ** num_two)
floor_division = (num_one // num_two)

print('----------')

# Círculo con un radio de 30 metros
radius = 30
# Calcular área
import math
pi = math.pi
area_of_circle = pi * radius * radius
# Calcular perímetro
circum_of_circle = 2 * pi * radius
# Tomar el radio desde un input y calcular el área
radius_input = input('Ingrese el radio del círculo: ')
int_rad_input = int(radius_input)
area_input = pi * int_rad_input * int_rad_input
print('El área del círculo es:', area_input)

# Devuelve la lista de palabras reservadas
help('keywords')
'''
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
'''

