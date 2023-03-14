# computadora adivina número
import random

def run():
    try:
        
        def adivina_el_numero_computadora(x):
            print(" ")
            print("====================================")
            print("      BienVenido al juego     ")
            print("  computadora adivinando número  ")
            print("====================================")
            print(" ")
            print(f"Seleciona un número entre 1 y {x} para que la computadora intente adivinar el número seleccionado por ti: ")
            
            limite_inferior = 1
            limite_superior = x
            
            
            respuesta = ""
            while respuesta != "c":
                if limite_inferior != limite_superior:
                    prediccion = random.randint(limite_inferior, limite_superior)
                else:
                    prediccion = limite_inferior
                
                respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja , ingresa (B). Si es correcta ingresa (C): ").lower()
            

                if respuesta == "a":
                    limite_superior -= prediccion
                elif respuesta == "b":
                    limite_superior += prediccion
            
            print(f"🎉🎉🎉🎉🎉 La computadora adivinó tu número correctamente: {prediccion}")    
            
            
        adivina_el_numero_computadora(10)
    except:
        print("Error--- verifica los valores ingresados")
        
if __name__ == "__main__":
    run()