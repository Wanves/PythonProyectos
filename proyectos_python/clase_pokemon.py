import random

class Pokemon:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = 100
        
    def gano(self):
        print("")
        print(f"El Pokemon {self.nombre} ha ganado!")
        print('Más suerte la próxima vez')
        print("")
        
p1 = Pokemon('Pikachu',60)
p2 = Pokemon('Charmander',55)

p1.vida = 100
p2.vida = 100

turno = random.randint(1,2)
print(" ")
print('Comienza la Batalla')
print(f'{p1.nombre} vs. {p2.nombre}')
print(" ")

print(f'Pikachu 🐱 HP: {p1.vida} Charmander 🐺 HP: {p2.vida} ')
opcion = input('Ingresa una opción: 1. Para continuar 2. Salir: ')

while opcion == '1':
    if opcion == '1':
        while p1.vida > 0 and p2.vida > 0:
            if turno == 1:
                p2.vida = p2.vida - p1.ataque
                turno = 2
                print(" ")
                print(f'{p1.nombre} ataca, {p2.nombre} ahora tiene {p2.vida}')
                print(f'Pikachu 🐱 HP: {p1.vida} Charmander 🐺 HP: {p2.vida} ')
                print('=== PRÓXIMA RONDA ===')
                print(" ")
            else:
                p1.vida = p1.vida - p2.ataque
                turno = 1
                print(" ")
                print(f'{p2.nombre} ataca, {p1.nombre} ahora tiene {p1.vida}')
                print(f'Pikachu 🐱 HP: {p1.vida} Charmander 🐺 HP: {p2.vida} ')
                print('=== PRÓXIMA RONDA ===')
                print(" ")
            if p1.vida <= 0:
                p2.gano()
            else:
                p1.gano() 
            print(f'Pikachu 🐱 HP: {p1.vida} Charmander 🐺 HP: {p2.vida} ')
            if p1.vida <= 0:
                print(f'{p1.nombre} fue eliminado')
                print('Fin de la partida')
                break
            elif p2.vida <= 0:
                print(f'{p2.nombre} fue eliminado')
                print('Fin de la partida')
                break 
            
            opcion = input('Ingresa una opción: 1. Para continuar 2. Salir: ')
            if opcion == '2':
                print('Has elegido salir')
                print('Fin de la partida')
                break
            
    else:
        break
    
    