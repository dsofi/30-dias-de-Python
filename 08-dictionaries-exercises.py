# 01 - Create an empty dictionary called dog
dog = {}

# 02 - Add name, color, breed, legs, age to the dog dictionary
dog['nombre']='Firulais'
dog['color']='blanco'
dog['raza']='callejero'
dog['piernas']=4
dog['edad']=2
print('dog:', dog)

# 03 - Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Juan',
    'last_name':'Gonzalez',
    'gender':'masc',
    'age':20,
    'marital_status':'single',
    'skills':['HTML','CSS','JS'],
    'contry':'Kenia',
    'city':'Nairobi',
    'address':{
        'street':'Moi Ave',
        'zipcode':'xxx123'
    }
}

# 04 - Get the length of the student dictionary
print('length student dct:', len(student))  #9

# 05 - Get the value of skills and check the data type, it should be a list
print('get skills:', student.get('skills'))
print('data type skills:', type(student.get('skills')))

# 06 - Modify the skills values by adding one or two skills
student['skills'].append('Angular')
student['skills'].append('React')
print('add skills:', student)

# 07 - Get the dictionary keys as a list
st_keys = student.keys()
print('student keys:', st_keys)

# 08 - Get the dictionary values as a list
st_values = student.values()
print('student values:', st_values)

# 09 - Change the dictionary to a list of tuples using items() method
st_list = student.items()
print('student list of tuples:', st_list)

# 10 - Delete one of the items in the dictionary
student.pop('address')
print('pop address:', student)

# 11 - Delete one of the dictionaries
del student