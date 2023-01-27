# Exercises: Level 1
print('''

--------- * LEVEL 1 * ---------
''')

# 01 - Writ a function which generates a six digit/character random_user_id.
print('-- Exercise 1 --')
import random
import string
def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
print('random user : ', random_user_id())

# 02 - Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print('-- Exercise 2 --')
def user_id_gen_by_user():
    cant_char = int(input('Ingrese la cantidad de caracteres que deben tener las IDs : '))
    cant_id = int(input('Ingrese la cantidad de IDs a generar : '))
    ids = []
    for _ in range(cant_id):
        gen_id = ''.join(random.choices(string.ascii_letters + string.digits, k=cant_char))
        ids.append(gen_id)
    return '\n'.join(ids)
print(user_id_gen_by_user())

# 03 - Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print('-- Exercise 3 --')
def rgb_color_gen():
    red, green, blue = (random.randint(0,255) for _ in range(3))
    return f'rgb({red},{green},{blue})'
print(rgb_color_gen())


# Exercises: Level 2
print('''

--------- * LEVEL 2 * ---------
''')

# 01 - Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
print('-- Exercise 1 --')
def list_of_hexa_colors(cant_col):
    symbols = '0123456789abcdef'
    hexa_colors = []
    for _ in range(cant_col):
        gen_col = '#'
        for _ in range(6):
            gen_col += random.choice(symbols)
        hexa_colors.append(gen_col)
    return hexa_colors
print('Lista de colores hexadecimales : ', list_of_hexa_colors(3))

# 02 - Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print('-- Exercise 2 --')
def list_of_rgb_colors(cant_col):
    rgb_colors = []
    for _ in range(cant_col):
        gen_col = rgb_color_gen()
        rgb_colors.append(gen_col)
    return rgb_colors
print('Lista de colores rgb : ', list_of_rgb_colors(3))

print('-- Exercise 2 (alternativa)--')
def list_of_rgb_colors_alt(cant_col):
    return [rgb_color_gen() for _ in range(cant_col)]
print('Lista de colores rgb : ', list_of_rgb_colors_alt(3))

# 03 - Write a function generate_colors which can generate any number of hexa or rgb colors.
print('-- Exercise 3 --')
def generate_colors(type,cant_col):
    if type == 'hexa':
        return list_of_hexa_colors(cant_col)
    elif type == 'rgb':
        return list_of_rgb_colors(cant_col)
    else:
        raise ValueError("Tipo de color inválido. Solo se permite 'hexa' o 'rgb'.")
print('Lista random hexa , 3 colores : ', generate_colors('hexa', 3)) 
print('Lista random hexa , 1 color : ', generate_colors('hexa', 1))
print('Lista random rgb , 3 colores : ', generate_colors('rgb', 3)) 
print('Lista random rgb , 1 color : ', generate_colors('rgb', 1))  


# Exercises: Level 3
print('''

--------- * LEVEL 3 * ---------
''')

# 01 - Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
print('-- Exercise 1 --')
def shuffle_list(lista):
    copy_lst = lista.copy()
    random.shuffle(copy_lst)
    return copy_lst
lst_prueba = ['uno','dos','tres','cuatro','cinco','seis']
print(shuffle_list(lst_prueba))

# 02 - Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print('-- Exercise 2 --')
def uniq_7_num():
    lst_num = []
    while len(lst_num) < 7:
        num = random.randint(0,9)
        if num not in lst_num:
            lst_num.append(num)
    return lst_num
print(uniq_7_num())

