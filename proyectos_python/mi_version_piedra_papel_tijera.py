import random

def run():
    
    try:
        opcion = ['piedra', 'papel', 'tijera']

        jugada = 0
        usuario = 0
        pcContrincante = 0
        empate = 0
        ganador = usuario - pcContrincante

        while True:
            jugada += 1
            print('Jugada N°', jugada)
            print(f'Empates {empate}')
            print(f'Jugadas ganadas usuario {usuario}')
            print(f'Jugadas ganadas pc {pcContrincante}')
            opcion2 = ['salir']
            opcion3 = ['seguir']
            jugador = input('Elige una opción-> piedra, papel o tijera: ').lower()
            if jugador not in opcion:
                print('Elección no valida')
                continue
            pc = random.choice(opcion)

            print(' ')
            print(f'PC elige:   {pc}')
            print(f'Tu eliges:  {jugador}')

            if jugador == pc:
                print(' ')
                print('Empate 🤙🤙')
                print(' ')
                empate += 1
                print(empate)
                print(' ')
            elif jugador == 'tijera' and pc == 'papel':
                print(' ')
                print('Ganaste 😃 tijera ✂️  gana a papel 📰')
                print(' ')
                usuario += 1
                print(f'Jugada ganada usuario {usuario}')
                print(' ')
            elif jugador == 'papel' and pc == 'piedra':
                print(' ')
                print('Ganaste 😃 papel 📰  gana a piedra 🪨 ')
                print(' ')
                usuario += 1
                print(f'Jugada ganada usuario {usuario}')
                print(' ')
            elif jugador == 'piedra' and pc == 'tijera':
                print(' ')
                print('Ganaste 😃 piedra 🪨  gana a tijera ✂️')
                print(' ')
                usuario += 1
                print(f'Jugada ganada usuario {usuario}')
                print(' ')
            elif pc == 'tijera' and jugador == 'papel':
                print(' ')
                print('Perdiste 😮 tijera ✂️  gana a papel 📰')
                print(' ')
                print(' ')
                pcContrincante += 1
                print(pcContrincante)
                print(' ')
            elif pc == 'papel' and jugador == 'piedra':
                print(' ')
                print('Perdiste 😮 papel 📰  gana a piedra 🪨 ')
                print(' ')
                print(' ')
                pcContrincante += 1
                print(pcContrincante)
                print(' ')
            elif pc == 'piedra' and jugador == 'tijera':
                print(' ')
                print('Perdiste 😮 piedra 🪨  gana a tijera ✂️')
                print(' ')
                print(' ')
                pcContrincante += 1
                print(pcContrincante)
                print(' ')
            else:
                print(' ')
                print('Perdiste')
                print(' ')
            jugador = input(
                'Escribe salir para terminar el juego o seguir para continuar jugando: ').lower()
            if jugador == 'salir':
                print(' ')
                print('🔷 🔶 Fin del juego 🔶 🔷')
                print(' ')
                print('🚨 Resultado Final 🚨')
                print(' ')
                jugada += 1 - 1
                print(f'🟠 Número de jugadas: {jugada}')
                print(' ')
                print(f'🔵 Empates: {empate}')
                print(' ')
                print(f'🟡 Jugadas ganadas usuario {usuario}')
                print(' ')
                print(f'🟢 Jugadas ganadas pc {pcContrincante}')
                break
            elif jugador == 'seguir':
                continue
                print('Continua el juego')
            else:
                print(' ')
                print('Elección no valida, tienes una oportunidad más para salir o seguir jugando, si la opción no es corrécta el juego terminará automáticamente.')
                print(' ')
                jugador = input(
                    'Escribe salir para terminar el juego o seguir para continuar jugando: ').lower()
                print(' ')
                if jugador == 'salir':
                    print(' ')
                    print('Fin del juego')
                    print(' ')
                    break
                elif jugador == 'seguir':
                    print(' ')
                    print('Continua el juego')
                    print(' ')
                    continue
                else:
                    print('Elección no valida')
                    print('Fin del juego')
                    print(' ')
                    print('🔷 🔶 Fin del juego 🔶 🔷')
                    print(' ')
                    print('🚨 Resultado Final 🚨')
                    print(' ')
                    jugada += 1 - 1
                    print(f'🟠 Número de jugadas: {jugada}')
                    print(' ')
                    print(f'🔵 Empates: {empate}')
                    print(' ')
                    print(f'🟡 Jugadas ganadas usuario {usuario}')
                    print(' ')
                    print(f'🟢 Jugadas ganadas pc {pcContrincante}')    
                    break
        if usuario > pcContrincante:
            print(' ')
            print('Ganador 😃 Usuario')
        elif usuario < pcContrincante:
            print(' ')
            print('Ganador 🤖 Pc')
        else:
            print(' ')
            print('Empate entre usuario 😃 y 🤖 Pc')
            
                    

    except:
        print('Error de carga -- recarga nuevamente y continua')


if __name__ == '__main__':
        run()
    