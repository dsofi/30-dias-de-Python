# 01 - Get the current day, month, year, hour, minute and timestamp from datetime module
print('''
--- Exercise 01 ---''')
from datetime import datetime
hoy = datetime.now()
dia = hoy.day
mes = hoy.month
anio = hoy.year
hora = hoy.hour
minuto= hoy.minute
segundo = hoy.second
timestamp = hoy.timestamp()
print(f'{dia}/{mes}/{anio} - {hora}.{minuto}.{segundo}')
print('Timestamp : ', timestamp)

print('--- Alternativa ---')
ahora = datetime.now()
fecha = ahora.strftime('%d/%m/%Y')
hora = ahora.strftime('%H:%M:%S')
print('Fecha actual : ', fecha)
print('Hora actual : ', hora)

# 02 - Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print('''
--- Exercise 02 ---''')
now = datetime.now()
current_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(current_date)

# 03 - Today is 5 December, 2019. Change this time string to time.
print('''
--- Exercise 03 ---''')
date_str = "5 December, 2019"
date_obj = datetime.strptime(date_str, "%d %B, %Y")
print('Time string to Time object : ', date_obj)

# 04 - Calculate the time difference between now and new year.
print('''
--- Exercise 04 ---''')
ahora = datetime.now()
anio_nuevo = datetime(ahora.year+1, 1, 1)
diff = anio_nuevo - ahora
print('Falta para año nuevo : ', diff)

# 05 - Calculate the time difference between 1 January 1970 and now.
print('''
--- Exercise 05 ---''')
fecha_05 = datetime(1970, 1, 1)
diff_05 = ahora - fecha_05
print('Diferencia entre 01/01/1970 hasta hoy : ', diff_05)

# 06 - Think, what can you use the datetime module for? Examples:
# a- Time series analysis
# b- To get a timestamp of any activities in an application
# c- Adding posts on a blog
'''
-Para darle formato a las fechas.
-Alertas (cuando pasa x tiempo de x actividad)
-Conversiones de horario según la zona.
-Logging
-Programar envíos de mail, o ejecutar algún script.
-Hacer trackings de la cantidad de tiempo que toma un proceso hasta ser completado.
-Hacer reportes de alguna actividad o proceso.
-En juegos, para habilitar/deshabilitar funciones
'''