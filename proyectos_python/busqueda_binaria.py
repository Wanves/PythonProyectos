import random
import time


def run():
    
    try:
        
        def busqueda_ingenua(lista, objetivo): 
            for i in range(len(lista)):
                if lista[i] == objetivo:
                    return i
            return -1
        
        def busqueda_binaria(lista, objetivo, limite_inferior=None,limite_superior=None):
            if limite_inferior is None:
                limite_inferior = 0
            if limite_superior is None:
                limite_superior = len(lista)-1
            
            if limite_superior < limite_inferior:
                return -1

            punto_medio = (limite_inferior + limite_superior) // 2
            
            if lista[punto_medio] == objetivo:
                return punto_medio
            elif objetivo < lista[punto_medio]:
                return busqueda_binaria(lista,objetivo,limite_inferior,punto_medio-1)
            else:
                return busqueda_binaria(lista,objetivo,punto_medio+1,limite_superior)
        
        tamaño = 100000
        conjunto_inicial = set()
        
        while len(conjunto_inicial) < tamaño:
            conjunto_inicial.add(random.randint(-3*tamaño,3*tamaño))
            
        mlista = sorted(list(conjunto_inicial))
        
        inicio = time.time()
        for objetivo in mlista:
            busqueda_ingenua(mlista,objetivo)
            
        fin = time.time()
        print(f"Tiempo de búsqueda ingenua: {fin - inicio} segundos.")
        
        inicio = time.time()
        for objetivo in mlista:
            busqueda_binaria(mlista,objetivo)
        fin = time.time()
        print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos.")  
        
        
        # print(busqueda_ingenua(mlista,10000))
        print(busqueda_binaria(mlista,15000))
        
        
    except:
        print(" ")
        print("🤖Error---Verifica los datos ingresados.")
        print(" ")
        
if __name__ == "__main__":
    run()
    
    
    