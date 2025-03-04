######################################################################
#####################--ENFOQUE PROCEDURAL--###########################
######################################################################

######################--Ejemplo si tenemos una pila--########################

# stack = []
# def push(val):
#     stack.append(val)
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
# ################################################
# push(3)
# push(2)
# push(1)
# print(pop())
# print(pop())
# print(pop())

######################--Ejemplo si tenemos dos pilas--########################
# def push(val, pila):
#     pila.append(val)
# def pop(pila):
#     val = pila[-1]
#     del pila[-1]
#     return val
# ################################################
# stack1 = []
# stack2 = []
# push(3, stack1)
# push(2, stack1)
# push(1, stack1)
# print(pop(stack1))
# print(pop(stack1))
# print(pop(stack1))
# print()
# push('a', stack2)
# push('b', stack2)
# push('c', stack2)
# print(pop(stack2))
# print(pop(stack2))
# print(pop(stack2))

############################################################################################
#####################--ENFOQUE PROGRAMACIÓN ORIENTADA A OBJETOS--###########################
################################--NO ENCAPSULADO--##########################################

# class Stack:  # Definiendo la clase de la pila.
#     def __init__(self):  # Definiendo el constructor (MÉTODO ESPECIAL: se ejecuta cada vez y únicamente cuando se crea un objeto nuevo.)
#         print("¡Inicializando el objeto!")
#         self.stack_list = []                # Atributo NO encapsulado

# ################################################

# stack_object = Stack()  # Instanciando el objeto.
# print(len(stack_object.stack_list))
# print(stack_object.stack_list)          # Para atributo no encapsulado

# stack_object2 = Stack()  # Instanciando el objeto.
# stack_object2.stack_list.append(123)      # Para atributo no encapsulado
# stack_object2.stack_list.append(455)      # Para atributo no encapsulado

# print(len(stack_object2.stack_list))
# print(stack_object2.stack_list)

############################################################################################
#####################--ENFOQUE PROGRAMACIÓN ORIENTADA A OBJETOS--###########################
################################--SÍ ENCAPSULADO--##########################################

######################--Ejemplo no funciona--########################

# class Stack:
#     def __init__(self):
#         self.__stack_list = []


# stack_object = Stack()
# print(len(stack_object.__stack_list))   # No se puede acceder directamente desde el código
#                                         # Necesitaresmo crear un método para acceder al atributo

######################--Ejemplo correcto--########################

# class Stack:
#     def __init__(self):             # Constructor
#         self.__stack_list = []      # Lista encapsulada


#     def push(self, val):            # Método 1
#         self.__stack_list.append(val)


#     def pop(self):                  # Método 2
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

# #################################################################
    
# stack_object = Stack()
# stack_object2 = Stack()

# stack_object.push(3)
# stack_object.push(2)
# stack_object.push(1)
# stack_object2.push('a')
# stack_object2.push('b')
# stack_object2.push('c')

# print(stack_object.pop())
# print(stack_object.pop())
# print(stack_object.pop())
# print()
# print(stack_object2.pop())
# print(stack_object2.pop())
# print(stack_object2.pop())

############################################################################################
#####################---------Añadiendo una subclase-------------###########################
############################################################################################

# class Stack:
#     def __init__(self):         # Construtor de la clase Stack
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val


# class AddingStack(Stack):       # Entre paréntesis pasamos el nombre de la clase inmediatamente superior
#     def __init__(self):         # Constructor de la clase AddingStack
#         Stack.__init__(self)    # Llamada al contructor de la clase inmediatamente superior
#         self.__sum = 0          # Inicializando atributo de la clase AddingStack

#     def get_sum(self):
#         return self.__sum

#     def push(self, val):        # Sobreescritura del método 'push' de la clase 'Stack'
#         Stack.push(self, val)
#         self.__sum += val       

#     def pop(self):              # Sobreescritura del método 'pop' de la clase 'Stack'
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val

# #################################################################
    
# stack_object = AddingStack()

# for i in range(5):
#     stack_object.push(i)

# print(stack_object.get_sum())
# print()

# for i in range(5):
#     print(stack_object.pop())

# print()
# print(stack_object.get_sum())

############################################################################################
#####################---------LAB 3.2.1.14 Pila Contadora--------###########################
############################################################################################

# class Stack:
#     def __init__(self):
#         self.__stk = []

#     def push(self, val):
#         self.__stk.append(val)

#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val

# class CountingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__count_pop = 0

#     def get_counter(self):
#         return self.__count_pop

#     def pop(self):
#         val = Stack.pop(self)
#         self.__count_pop += 1
#         return val

# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())

############################################################################################
#####################------LAB 3.2.1.15 Colas de alias FIFO------###########################
############################################################################################
# class QueueError (IndexError):
#     pass

# class Queue:
#     def __init__(self):
#         self.__cola = []

#     def put(self, elem):
#         self.__cola.append (elem)

#     def get(self):
#         primer_elemento = self.__cola[-1]
#         del self.__cola [-1]
#         return primer_elemento

# que = Queue()
# que.put(1)
# que.put("perro")
# que.put(False)
# try:
#     for i in range(4):
#         print(que.get())
# except QueueError:
#     print("Error de Cola")
# except:
#     print("Ha ocurrido un error desconocido")

############################################################################################
#####################------LAB 3.2.1.16 Colas de alias FIFO------###########################
####################################--Forma 1--#############################################
    
# class SuperQueue():
#     def __init__(self):
#         self.__cola = []

#     def put(self, elem):
#         self.__cola.append(elem)
    
#     def get(self):
#         primer_elemento = self.__cola[-1]
#         del self.__cola [-1]
#         return primer_elemento
        
#     def isempty(self):
#         if len(self.__cola):
#             return False
#         else:
#             return True

# #################################################
# que = SuperQueue()
# que.put(1)
# que.put("perro")
# que.put(False)
# for i in range(4):
#     if not que.isempty():
#         print(que.get())
#     else:
#         print("Cola vacía")

############################################################################################
#####################------LAB 3.2.1.16 Colas de alias FIFO------###########################
####################################--Forma 2--#############################################

# class QueueError(IndexError):
#     pass

# class Queue:
#     def __init__(self):
#         self.cola = []      # No puede estar enccapsulado para que pueda ser accedido desde una subclase

#     def put(self, elem):
#         self.cola.append (elem)

#     def get(self):
#         primer_elemento = self.cola[0]
#         del self.cola [0]
#         return primer_elemento

# class SuperQueue(Queue):        # Esta clase no requiere un nuevo atributo, por lo que no necesita un constructor
#     def isempty(self):          # Al no necesitar un constructor, el constructor de la superclase se ejecuta implícitamente
#         return len(self.cola) == 0 # Cuando la subclase necesite un constructor, sí hay que llamar al constructor de la superclase (que debe NO tener argumentos)

# ################################################
# que = SuperQueue()
# que.put(1)
# que.put("perro")
# que.put(False)
# for i in range(4):
#     if not que.isempty():
#         print(que.get())
#     else:
#         print("Cola vacía")

############################################################################################
#####################------LAB 3.2.1.16 Colas de alias FIFO------###########################
#####################--Forma 3: ENCAPSULACIÓN/NAME MANGLING--###############################
        
class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.__lista_pila = []
    def put(self, elem):
        self.__lista_pila.insert(0,elem)
        
    def get(self):
        if len(self.__lista_pila) > 0:
            ultimo_elemento = self.__lista_pila[-1]
            del self.__lista_pila[-1]
            return ultimo_elemento
        else:
            raise QueueError

class SuperQueue(Queue):
    def isempty(self):
        return len(self._Queue__lista_pila) == 0    # NAME MANGLIG para accedes a atributos encapsulados!!!!!


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
