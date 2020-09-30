# Modulo de teste de abstração do decorator
from main import (func_decorator, class_decorator)

# // função original retorna soma entre 'a' e 'b'
@class_decorator
def adicionar(a, b):
    return a + b

# // função original retorna subtração entre 'a' e 'b'
@func_decorator
def subtrair(a, b):
    return a - b


a = adicionar(20, 20)
b = subtrair(20, 20)

# // apos modificação 'a' deve retornar 400
# // apos modificação 'b' deve retornar 4.0
print('Soma modificada == ', a)
print('Subtração modificada == ', b)
