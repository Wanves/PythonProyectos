# El ahorcado
import string
import random
from palabras_ahorcado import palabras 
from visual_ahorcado import vidas_diccionario_visual
def run():
    
    try:
        
        def obtener_palabra_valida(palabras):
            palabra = random.choice(palabras)
            
            while "-" in palabra or " " in palabra:
                palabra = random.choice(palabras)
            return palabra.upper()
        
        def ahorcado():
            print(" ")
            print("======================================")
            print("   Bienvenido al juego del Ahorcado  ")
            print("======================================")
            print(" ")
            
            palabra = obtener_palabra_valida(palabras)
            
            letras_por_adivinar = set(palabra)
            letras_adivinadas = set()
            abecedario = set(string.ascii_uppercase)
            
            vidas = 7
            
            while len(letras_por_adivinar) > 0 and vidas > 0:
                print(" ")
                print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
                print(" ")
                palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
                print("")
                print(vidas_diccionario_visual[vidas])
                print(" ")
                print("")
                print(f"Palabra:{' '.join(palabra_lista)}")
                print(" ")

                letra_usuario = input("Escoge un aletra: ").upper()
                
                if letra_usuario in abecedario - letras_adivinadas:
                    letras_adivinadas.add(letra_usuario)

                    if letra_usuario in letras_por_adivinar:
                        letras_por_adivinar.remove(letra_usuario)
                        print(" ")
                    else:
                        vidas -= 1
                        print("")
                        print(f"\nTu letra, {letra_usuario} no esta en la palabra.")
                        print(" ")

                elif letra_usuario in letras_adivinadas:
                    print("")
                    print(f"\nYa escogiste esa letra por favor elige una letra nueva.")
                    print(" ")
                else:
                    print("")
                    print(f"\nEsta letra no es válida")
                    print(" ")
                    
            if vidas == 0:
                print("")
                print(vidas_diccionario_visual[vidas])
                print(" ")
                print("")
                print(f"Ahorcado!👻 Perdiste. La palabra era: {palabra}")
                print(" ")
            else:
                print("")
                print(f"Excelente!🤩 Adivinaste la palabra {palabra}!")
                print(" ")       
                        
        
        ahorcado()
    except:
        print("🤖Error---Verifica los datos ingresados.")
        
if __name__ == "__main__":
    run()