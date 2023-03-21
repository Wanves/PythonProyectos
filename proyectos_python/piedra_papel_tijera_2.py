import random

# 🪨   ✂   📄 

def run():
    
    try:
        
        def jugar():
            usuario = input("Escoge una opción: 'pi' para piedr 🪨, 'pa' para papel 📄, 'ti' para tijera ✂ :\n").lower()
            computadora = random.choice(["pi","pa","ti"])
                
            if usuario == computadora:
                return "Empate!🤪"
                
            if gano_el_jugador(usuario,computadora):
                return "Ganaste!🤩💫💫💫"
                
            return "Perdiste!🙄"
            
        def gano_el_jugador(usuario,oponente):
            if usuario == "pi" and oponente == "ti" or usuario == "ti" and oponente == "pa" or usuario == "pa" and oponente == "pi":
                 return True
            else:
                return False
            
            
        print(jugar())
            
    except:
        print("👾👾👾Error---verifica los valores ingresados")

if __name__ == "__main__":
    run()
