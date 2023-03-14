# adivina el número
import random

def run():
    try:
        
        def adivina_el_numero(x):
            print(" ")
            print("==============================")
            print("      BienVenido al juego     ")
            print("==============================")
            print(" ")
            print("Tu meta es adivinar el número generado por la computadora.")
            
            numero_aleatorio = random.randint(1,x)
            print(numero_aleatorio)
            
            prediccion = 0
            
            while prediccion != numero_aleatorio:
                prediccion = int(input(f"Adivina un número entre 1 y {x}: "))
                if prediccion < numero_aleatorio:
                    print("Intenta nuevamente. Este número es muy pequeño.")
                elif prediccion > numero_aleatorio:
                    print("Intentalo nuevamente. Este número es muy grande.")
                elif prediccion == numero_aleatorio:
                    print(f"Felicidades! Adivinaste el número aleatorio.")
                    print(f"Número aleatorio: {numero_aleatorio}\nNúmero seleccionado: {prediccion}")
                else:
                    print("Estas intentando ingresar un valor no valido.")
            
            
        adivina_el_numero(10)
    except:
        print("Error--- verifica los valores ingresados")
        
if __name__ == "__main__":
    run()