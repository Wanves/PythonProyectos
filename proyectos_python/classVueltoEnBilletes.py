# EJERCICIO en Python 🐍 : class Vuelto en billetes 💵


class Contadora:
    def __init__(self,monto):
        print(" ")
        self.monto = int(input('Ingresa el monto en dólares: '))
        print(" ")
        
        
    def VueltoEnBilletes(self):
        cant_100 = self.monto // 100
        self.monto = self.monto % 100
        cant_50 =  self.monto // 50
        self.monto = self.monto % 50
        cant_20 =  self.monto // 20
        self.monto = self.monto % 20
        cant_10 =  self.monto // 10
        self.monto = self.monto % 10
        cant_5 =  self.monto // 5
        self.monto = self.monto % 5
        cant_2 =  self.monto // 2
        self.monto = self.monto % 2
        
        print(f"""
            La cantidad de billetes que necesitas para abonar el monto es:
            billetes de 100: {cant_100}
            billetes de 50: {cant_50}
            billetes de 20: {cant_20}
            billetes de 10: {cant_10}
            billetes de 5: {cant_5}
            billetes de 2: {cant_2}
            billetes de 1: {self.monto}   
              """)
        print(" ")


contadora = Contadora(0)
contadora.VueltoEnBilletes()