import random
import os
def run():
    IMAGENES = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']
    DB = [
        "c++",
        "python",
        "javascript",
        "rubi",
        "php"
    ]
    
    palabras = random.choice(DB)
    espacios = ["_"] * len(palabras)
    intentos = 6
    
    while True:
        os.system("cls")
        for caracter in espacios:
            print(caracter,end=" ")
        print(IMAGENES[intentos])
        print(" ")
        letra = input("💡 Elige una letra: ").lower()
        print(" ")

        found = False
        for idx, caracter in enumerate(palabras):
            if caracter == letra:
                espacios[idx] = letra
                found  = True
                
        if not found:
            intentos -=1

        if "_" not in espacios:
            os.system("cls")
            print(" ")
            print("Ganaste 🎉🎉🎉😃")
            print(" ")
            break
            input()
            
        if intentos == 0:
            os.system("cls")
            print(" ")
            print("Perdiste 💥💥💥😬")
            print(" ")
            break
            input()
            
        
    
if __name__ == "__main__":
    run()