###############################################################################################################
#######################################---LAB 3.4.1.12 La clase Timer---#######################################
###############################################################################################################

# class Timer():
#     def __init__(self, h = 0, m = 0, s = 0):
#         self.__hrs = h
#         self.__min = m
#         self.__sec = s
#         self.to_string()
        
#     def next_second(self):
#         if self.__sec < 59:
#             self.__sec += 1
#         else:
#             self.__sec = 0
#             if self.__min < 59:
#                 self.__min += 1
#             else:
#                 self.__min = 0
#                 if self.__hrs < 23:
#                     self_hrs += 1
#                 else:
#                     self.__hrs = 0
#         self.to_string()

#     def prev_second(self):
#         if self.__sec > 0:
#             self.__sec -= 1
#         else:
#             self.__sec = 59
#             if self.__min > 0:
#                 self.__min -= 1
#             else:
#                 self.__min = 59
#                 if self.__hrs > 0:
#                     self_hrs -= 1
#                 else:
#                     self.__hrs = 23
#         self.to_string()
    
#     def to_string(self):
#         str_hrs = str(self.__hrs)
#         str_min = str(self.__min)
#         str_sec = str(self.__sec)

#         if len(str_hrs) == 1:
#             str_hrs = '0' + str_hrs
#         if len(str_min) == 1:
#             str_min = '0' + str_min
#         if len(str_sec) == 1:
#             str_sec = '0' + str_sec

#         print(str_hrs, ':', str_min, ':', str_sec, sep='')

# ##########################################################
# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)

###############################################################################################################
####################################---LAB 3.4.1.13 Días de la semana---#######################################
###############################################################################################################

# class WeekDayError(Exception):
#     pass
	
# class Weeker:
#     __day_lst = ['Lun', 'Mar', 'Mier', 'Jue', 'Vie', 'Sab', 'Dom']
#     def __init__(self, day):
#         if day not in Weeker.__day_lst:
#             raise WeekDayError
#         else:
#             self.__current_day = day

#     def __str__(self):
#         return self.__current_day   #Para convertir a cadena el valor devuelto (de lo contrario, devuelve la direción del objeto)

#     def add_days(self, n):
#         while n > 7:
#             n -= 7
#         if self.__current_day == 'Dom':
#             self.__current_day = 'Lun'
#             n -= 1
#         self.__current_day = Weeker.__day_lst[Weeker.__day_lst.index(self.__current_day) + n]
        
#     def subtract_days(self, n):
#         while n > 7:
#             n -= 7
#         if self.__current_day == 'Lun':
#             self.__current_day = 'Dom'
#             n += 1
#         self.__current_day = Weeker.day_lst[Weeker.day_lst.index(self.__current_day) - n]

# #############################################################################
# try:
#     weekday = Weeker('Lun')
#     print(weekday)
#     weekday.add_days(15)
#     print(weekday)
#     weekday.subtract_days(23)
#     print(weekday)
#     weekday = Weeker('Lunes')
# except WeekDayError:
#     print("Lo siento, no puedo atender tu solicitud.")

###############################################################################################################
####################################---LAB 3.4.1.14 Puntos en un plano---######################################
###############################################################################################################

# import math

# class Point:
#     def __init__(self, x1=0.0, y1=0.0):
#         self.__x = x1
#         self.__y = y1

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__y

#     def distance_from_xy(self, x2, y2):
#         dist_x = math.fabs (self.getx() - x2)
#         dist_y = math.fabs (self.gety() - y2)
#         return math.hypot(dist_x, dist_y)

#     def distance_from_point(self, point):
#         x2 = point.getx()
#         y2 = point.gety()
#         dist_x = math.fabs (self.getx() - x2)
#         dist_y = math.fabs (self.gety() - y2)
#         return math.hypot(dist_x, dist_y)

# ###########################################################################
# point1 = Point(0, 0)
# point2 = Point(1, 1)
# print(point1.distance_from_point(point2))
# print(point2.distance_from_xy(2, 0))

###############################################################################################################
####################################---LAB 3.4.1.15 Triángulo---######################################
###############################################################################################################
import math

class Point:
    def __init__(self, x1=0.0, y1=0.0):
        self.__x = x1
        self.__y = y1

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x2, y2):
        dist_x = math.fabs (self.getx() - x2)
        dist_y = math.fabs (self.gety() - y2)
        return math.hypot(dist_x, dist_y)

    def distance_from_point(self, point):
        x2 = point.getx()
        y2 = point.gety()
        dist_x = math.fabs (self.getx() - x2)
        dist_y = math.fabs (self.gety() - y2)
        return math.hypot(dist_x, dist_y)

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        perimetro = 0
        for i in range (3):
            for j in range (i+1, 3):
                perimetro += Point.distance_from_point(self.__vertices[i], self.__vertices[j])
        return perimetro

###############################################################################################
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())