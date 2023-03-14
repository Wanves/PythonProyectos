# organización = "FreeCodeCamp"

# print(" ")
# print(f"Aprende a programar con {organización}")
# print(" ")


# Mad libs (Historias locas)
def run():
    try:
        adj = input("Ingresa el adjetivo seleccionado: ")
        verbo1 = input("Ingresa el verbo seleccionado: ")
        sustantivo_plural = input("Ingresa el sustantivo plural: ")
        
        madlib = f"Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1}. Aprende a programar con freeCodeCamp y alcanza tus {sustantivo_plural}"
        
        def mostrar_texto(frase):
            print(" ")
            print(frase)
            print(" ")
            
        mostrar_texto(madlib)
        
        
    except:
        print(" ")
        print("Error--- verifica los datos ingresados")
        print(" ")    
        
if __name__ == "__main__":
    run()