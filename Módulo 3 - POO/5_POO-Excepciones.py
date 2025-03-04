###########################---else---############################
# Se ejecuta cuando no se genera excepción

# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("División fallida")
#         return None
#     else:
#         print("Todo salió bien")
#         return n


# print(reciprocal(2))
# print(reciprocal(0))

###########################---finaly---###########################
# Se ejecuta siempre, al final

# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("División fallida")
#         n = None
#     else:
#         print("Todo salió bien")
#     finally:
#         print("Es momento de decir adiós")
#         return n


# print(reciprocal(2))
# print(reciprocal(0))

###########################---alias---###########################
# try:
#     i = int("¡Hola!")
# except Exception as e:
#     print(e)
#     print(e.__str__())
#     print(type(e).__name__)
#     print(e.__cause__)
#     print(e.args)

###########################---jerarquía---###########################

# def print_exception_tree(thisclass, nest = 0):
#     if nest > 1:
#         print("   |" * (nest - 1), end="")
#     if nest > 0:
#         print("   +---", end="")

#     print(thisclass.__name__)

#     for subclass in thisclass.__subclasses__():
#         print_exception_tree(subclass, nest + 1)

# print_exception_tree(BaseException)

###########################---ejemplos---###########################

# def print_args(args):
#     lng = len(args)
#     if lng == 0:
#         print("")
#     elif lng == 1:
#         print(args[0])
#     else:
#         print(str(args))


# try:
#     raise Exception
# except Exception as e:
#     print(e, e.__str__(), sep=' : ' ,end=' : ')
#     print_args(e.args)

# try:
#     raise Exception("mi excepción")
# except Exception as e:
#     print(e, e.__str__(), sep=' : ', end=' : ')
#     print_args(e.args)

# try:
#     raise Exception("mi", "excepción")
# except Exception as e:
#     print(e, e.__str__(), sep=' : ', end=' : ')
#     print_args(e.args)

###########################---ejemplos---###########################

# def print_args(args):
#     lng = len(args)
#     if lng == 0:
#         print("")
#     elif lng == 1:
#         print(args[0])
#     else:
#         print(str(args))


# try:
#     raise Exception
# except Exception as e:
#     print(e, e.__str__(), sep=' : ' ,end=' : ')
#     print_args(e.args)

# try:
#     raise Exception("mi excepción")
# except Exception as e:
#     print(e, e.__str__(), sep=' : ', end=' : ')
#     print_args(e.args)

# try:
#     raise Exception("mi", "excepción")
# except Exception as e:
#     print(e, e.__str__(), sep=' : ', end=' : ')
#     print_args(e.args)

###########################---EXCEPCIONES PERSONALIZADAS---###########################

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no hay tal pizza en el menú")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "demasiado queso")
    print("¡Pizza lista!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)