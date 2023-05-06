import pickle

class Estudiante:
    def __init__(self, nombre, edad, curso, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.curso_inicial = curso_inicial
        self.esta_activo = True
        self.cursos = [curso_inicial]
        
    def desactivar(self):
        self.esta_activo = False
        
    def info(self):
        print(f'Estudiante: {self.nombre} Edad: {self.edad} {self.esta_activo}')
    
est1 = Estudiante('Juan',35,'Python',1)
est2 = Estudiante('Sam',25,'React',2)
est3 = Estudiante('Pam',45,'Go',3)

lista_est_obj = [
    est1,
    est2,
    est3
]

archivo_est_obj = open('estudiantes_obj','wb')

pickle.dump(lista_est_obj, archivo_est_obj)

archivo_est_obj.close()
del archivo_est_obj

archivo_est_obj = open('estudiantes_obj','rb')

lista_recuperada = pickle.load(archivo_est_obj)


for i in lista_recuperada:
    print(' ')
    print(i.nombre)
    print(i.edad)
    print(i.curso)
    print(' ')