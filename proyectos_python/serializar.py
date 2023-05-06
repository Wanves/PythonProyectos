import pickle

lista = [
    'Juan - Python',
    'Juan - JavaScript',
    'Pedro - C#',
    'Juan - Go',
    'Zoe - Ruby',
    'Sam - Python',
    'Zoe - Vue',
    'Xavi - React'
]

serializado = open('lista','wb')

pickle.dump(lista, serializado)

serializado.close()

ar_serializado = open('lista','rb')

lista_recuperada = pickle.load(ar_serializado)
print(" ")
print(lista_recuperada)
print(" ")

for i in lista_recuperada:
    print(i)