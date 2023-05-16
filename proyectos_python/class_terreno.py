

class Terreno:
    def __init__(self,ancho,largo,precio_metro):
        self.ancho = float(input('Ingresa el ancho del terreno: '))
        self.largo = float(input('Ingresa el largo del terreno: ')) 
        self.precio_metro = float(input('Ingresa el precio del metro cuadrado: '))

    def precioTerreno2(self):
        sup_terreno = self.ancho * self.largo
        precio_sup_metro = int(sup_terreno * self.precio_metro)
        print(f'El precio por la superficie total del terreno es: ${precio_sup_metro}')
    
    def metroAlambrePerimetro(self):        
        perimetro = (self.ancho * 2) + (self.largo * 2)
        cant_pasadas = 3
        cant_alambre = perimetro * cant_pasadas
        print(f'La cantidad de metros de alambre que se requiere para rodear la superficie del terreno tres veces es: {cant_alambre} metros')          
            
   
terreno = Terreno(0,0,0)
terreno.precioTerreno2()
terreno.metroAlambrePerimetro()
