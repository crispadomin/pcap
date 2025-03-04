#############################################################

# # # https://www.geeksforgeeks.org/python-get-function-signature/

# import math

# from inspect import signature

# # declare a function gfg with some 
# # parameter 
# def gfg(x:str, y:int):      # str e int son una sugerencia para el lector, no son una limitación
#     pass


# # with the help of signature function 
# # store signature of the function in 
# # variable t 
# t = signature(gfg) 
  
# # print the signature of the function 
# print(t) 
  
# # print the annonation of the parameter 
# # of the function 
# print(t.parameters['x']) 
  
# # print the annonation of the parameter 
# # of the function 
# print(t.parameters['y'].annotation)

#############################################################

# import math
# import inspect              #No funcoina para funciones built-in

# def foo(arg1,arg2):         
#     #do something with args 
#     a = arg1 + arg2         
#     return a  


# lines = inspect.getsource(foo)
# print(lines)