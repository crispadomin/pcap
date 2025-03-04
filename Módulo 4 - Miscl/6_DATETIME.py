####################################--date.today--######################################
# from datetime import date

# today = date.today()

# print("Hoy:", today)
# print("Año:", today.year)
# print("Mes:", today.month)
# print("Día:", today.day)

####################################--date--######################################
# from datetime import date

# my_date = date(2019, 11, 4)
# print(my_date)

####################################--tiemstamp--######################################
# from datetime import date
# import time

# timestamp = time.time()
# print("Marca de tiempo:", timestamp)

# d = date.fromtimestamp(timestamp)
# print("Fecha:", d)

####################################--fromisoformat--######################################
# from datetime import date

# d = date.fromisoformat('2019-11-04')
# print(d)

####################################--datetime.replace--######################################
# from datetime import date

# d = date(1991, 2, 5)
# print(d)

# d = d.replace(year=1992, month=1, day=16)
# print(d)

####################################--datetime.weekday--######################################
# from datetime import date

# d = date(2019, 11, 4)
# print(d.weekday())      # Día 0 es lunes

# d = date(2019, 11, 4)
# print(d.isoweekday())   # Día 0 es domingo

####################################--datetime.time--######################################
# from datetime import time

# t = time(14, 53, 20, 1)

# print("Tiempo:", t)
# print("Hora:", t.hour)
# print("Minuto:", t.minute)
# print("Segundo:", t.second)
# print("Microsegundo:", t.microsecond)

###################################################################################3
# import time

# class Student:
#     def take_nap(self, seconds):
#         print("Estoy muy cansado. Tengo que echarme una siesta. Hasta luego.")
#         time.sleep(seconds)
#         print("¡Dormí bien! ¡Me siento genial!")

# student = Student()
# student.take_nap(5)

####################################--time.ctime--######################################
# import time

# timestamp = 1572879180
# print(time.ctime(timestamp))

####################################--time.gmtime/localtime--######################################
# time.struct_time:
#     tm_year   # Especifica el año.
#     tm_mon    # Especifica el mes (valor de 1 a 12)
#     tm_mday   # Especifica el día del mes (valor de 1 a 31)
#     tm_hour   # Especifica la hora (valor de 0 a 23)
#     tm_min    # Especifica el minuto (valor de 0 a 59)
#     tm_sec    # Especifica el segundo (valor de 0 a 61)
#     tm_wday   # Especifica el día de la semana (valor de 0 a 6)
#     tm_yday   # Especifica el día del año (valor de 1 a 366)
#     tm_isdst  # Especifica si se aplica el horario de verano (1: sí, 0: no, -1: no se sabe)
#     tm_zone   # Especifica el nombre de la zona horaria (valor en forma abreviada)
#     tm_gmtoff # Especifica el desplazamiento al este del UTC (valor en segundos)

# import time

# timestamp = 1572879180
# print(time.gmtime(timestamp))
# print(time.localtime(timestamp))
# print(time.localtime(timestamp).tm_year)

####################################--time.asctime/mktime--######################################
# import time

# timestamp = 1572879180
# st = time.gmtime(timestamp)

# print(time.asctime(st))
# print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0))) # Pasamos una tupla con 9 valores y lso convierte a formato EPOC

####################################--datetime.today/now/utcnow--######################################
# from datetime import datetime

# print("hoy:", datetime.today())
# print("ahora:", datetime.now())
# print("utc_ahora:", datetime.utcnow())

####################################--datetime.timestamp--######################################
# A partir del 01-01-1970

# from datetime import datetime

# dt = datetime(2020, 10, 4, 14, 55)
# print("Marca de tiempo:", dt.timestamp())

####################################--datetime.strftime--######################################
# # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# %a - The abbreviated weekday name (“Sun”)
# %A - The full weekday name (“Sunday”)
# %b - The abbreviated month name (“Jan”)
# %B - The full month name (“January”)
# %c - The preferred local date and time representation
# %d - Day of the month (01..31)
# %H - Hour of the day, 24-hour clock (00..23)
# %I - Hour of the day, 12-hour clock (01..12)
# %j - Day of the year (001..366)
# %m - Month of the year (01..12)
# %M - Minute of the hour (00..59)
# %p - Meridian indicator (“AM” or “PM”)
# %S - Second of the minute (00..60)
# %U - Week number of the current year, starting with the first Sunday as the first day of the first week (00..53)
# %W - Week number of the current year, starting with the first Monday as the first day of the first week (00..53)
# %w - Day of the week (Sunday is 0, 0..6)
# %x - Preferred representation for the date alone, no time
# %X - Preferred representation for the time alone, no date
# %y - Year without a century (00..99)
# %Y - Year with century
# %Z - Time zone name %% - Literal “%’’ character t = Time.now t.strftime(“Printed on %m/%d/%Y”) #=> “Printed on 04/09/2003” t.strftime(“at %I:%M%p”) #=> “at 08:56AM”
# from datetime import date

# d = date(2020, 1, 4)
# print(d.strftime('%Y/%m/%d'))

####################################--datetime.strptime--######################################
# Convierte la cadena de texto con la fecha en date_time
# from datetime import datetime
# print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

####################################--datetime.timedelta--######################################

# from datetime import date
# from datetime import datetime

# d1 = date(2020, 11, 4)
# d2 = date(2019, 11, 4)

# print(d1 - d2)

# dt1 = datetime(2020, 11, 4, 0, 0, 0)
# dt2 = datetime(2019, 11, 4, 14, 53, 0)

# print(dt1 - dt2)

########################################################################################
# from datetime import timedelta

# delta = timedelta(weeks=2, days=2, hours=3)
# print(delta)

########################################################################################
# from datetime import timedelta
# from datetime import date
# from datetime import datetime

# delta = timedelta(weeks=2, days=2, hours=2)
# print(delta)

# delta2 = delta * 2
# print(delta2)

# d = date(2019, 10, 4) + delta2
# print(d)

# dt = datetime(2019, 10, 4, 14, 53) + delta2
# print(dt)

########################################################################################
    ##############--LAB 4.5.1.22: Los módulos datetime y time--#####################
########################################################################################
# from datetime import datetime, date

# d = datetime(2020, 11, 4, 14, 53)
# print(d.strftime('%Y/%m/%d %H:%M:%S'))
# print(d.strftime('%y/%B/%d %H:%M:%S %p'))
# print(d.strftime('%a, %Y %b %d'))
# print(d.strftime('%A, %Y %B %d'))
# print('Día de la semana: ', d.isoweekday())

# año = int(d.year)
# dia_inicio = datetime(d.year - 1, 12, 31)
# dia_año = str(d - dia_inicio).split()
# print('Día del año: ', dia_año[0])

# semana_año = int(dia_año[0]) / 7

# print('Semaña del año: ', int(semana_año))

#################################--¿Cuándo es el próximo lunes pasadas 6 semanas?--############################

# from datetime import date, timedelta

# today = date.today()
# periodo = timedelta(weeks=6, days=0, hours=0)
# next_day = today + periodo
# hasta_proximo_lunes = timedelta(weeks=0, days=7 - next_day.weekday(), hours=0)
# print(next_day + hasta_proximo_lunes)

#################################################################
# from datetime import datetime

# my_date = datetime(2020, 11, 4, 14, 53)

# print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
# print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
# print(my_date.strftime("%a, %Y %b %d"))
# print(my_date.strftime("%A, %Y %B %d"))
# print(my_date.strftime("Día de la semana: %w"))
# print(my_date.strftime("Día del año: %j"))
# print(my_date.strftime("Número de semana en el año: %W"))

#################################################################

# from datetime import date, timedelta

# def siguiente_dia(fecha, dia):
#     dias_hasta_nuevo_dia = dia - fecha.weekday()
#     if dias_hasta_nuevo_dia <= 0: # El día ya ha transcurrido en esa semana
#         dias_hasta_nuevo_dia += 7
#     return fecha + timedelta(dias_hasta_nuevo_dia)
# seis_semanas = timedelta(weeks=6)
# fecha_actual = date.today()
# siguiente_lunes = siguiente_dia(fecha_actual + seis_semanas, 0) # 0 = Lunes, 1 = Martes, 2 = Miércoles...
# print('El próximo Lunes 6 semanas después de la fecha actual es el día', siguiente_lunes)

#################################################################
#######################################
# José Antonio
#######################################

# from datetime import datetime, timedelta

# ahora = datetime.now()
# intervalo = timedelta(weeks=6)
# vencimiento = ahora + intervalo

# dia_semana_vencimiento = int(vencimiento.strftime('%w'))
# if dia_semana_vencimiento == 1:
#     print(vencimiento.strftime('%Y/%m/%d día semana: %a'))
# else:
#     vencimiento = vencimiento + timedelta(days= 8 - dia_semana_vencimiento)
#     print(vencimiento.strftime('%Y/%m/%d día semana: %a'))

########################################
# Francisco
########################################

# from datetime import datetime, timedelta

# # Fecha determinada (un lunes)
# fecha_actual = datetime(2024, 2, 26)  

# # Sumar 6 meses a la fecha determinada
# fecha_despues = fecha_actual + timedelta(days=30*6)

# # Encontrar el lunes más cercano después del tiempo
# while fecha_despues.weekday() != 0:  # 0 es el código para el lunes
#     fecha_despues += timedelta(days=1)

# print("Fecha del lunes después del tiempo:", fecha_despues.strftime("%Y-%m-%d"))

########################################
# Miguel Angel
########################################

# from datetime import *

# fecha_actual = date.today()
# seis_meses_despues  = fecha_actual + timedelta(365/2)

# dia_semana = seis_meses_despues.weekday()

# if dia_semana != 0 :
#     seis_meses_despues += timedelta(7-dia_semana)
# print(seis_meses_despues.strftime("Seis meses despues estamos a: %A"))
# print(seis_meses_despues)