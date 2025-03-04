# w: ancho de la columna de fecha (por defecto 2)
# l: número de líneas por semana (por defecto 1)
# c: número de espacios entre las columnas del mes (por defecto 6)
# m: número de columnas (por defecto 3)

import calendar

# print(calendar.calendar(2020))
# calendar.prcal(2020)

# print(calendar.month(2020, 11))

# calendar.setfirstweekday(calendar.SUNDAY)
# calendar.prmonth(2020, 12)

# print(calendar.weekday(2020, 12, 24))

# print(calendar.weekheader(2))
# print(calendar.weekheader(3))


# print(calendar.isleap(2020))
# print(calendar.leapdays(2010, 2021))  # Hasta 2021, pero sin incluirlo.

######################--Iterar en los días de la semana--######################

# c = calendar.Calendar(calendar.SUNDAY)

# for weekday in c.iterweekdays():
#     print(weekday, end=" ")

######################--Iterar en los días del mes--######################

# c = calendar.Calendar()
# for date in c.itermonthdays(2019, 11):
#     print(date, end=" ")

# c = calendar.Calendar()
# for date in c.itermonthdates(2019, 11):
#     print(date, end=" ")

# Hay otros cuatro métodos similares en la clase Calendar que difieren en los datos devueltos:

# itermonthdates2: devuelve días en forma de tuplas que consisten en un número de día del mes y un número de día de la semana.
# itermonthdates3: devuelve días en forma de tuplas que constan de un año, un mes y un día de los números del mes. Este método ha estado disponible desde la versión 3.7 de Python.
# itermonthdates4: devuelve días en forma de tuplas que constan de números de año, mes, día del mes y día de la semana. Este método ha estado disponible desde la versión 3.7 de Python.


######################--monthdays2calendar()--######################

# c = calendar.Calendar()

# for data in c.monthdays2calendar(2020, 12):
#     print(data)

#################################################################################################
 #############################--LAB 4.6.1.13: El módulo calendar--##############################
#################################################################################################
from calendar import Calendar

class MyCalendar(Calendar):
    def count_week_day_in_year(self, year, weekday):
        count = 0
        for month in range(1,13):
            c = self.monthdays2calendar(year, month)
            for week in c:
                for day in week:
                    if day[0] != 0 and day[1] == weekday:
                        count += 1
        return count

cal = MyCalendar()
print(cal.count_week_day_in_year(2000, 6))