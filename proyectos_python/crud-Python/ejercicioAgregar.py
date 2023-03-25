
codigo = []
producto = []
precio = []

CodigoR = open('Codigo.txt','r')
ProductoR = open('Producto.txt','r')
PrecioR = open('Precio.txt','r')

for cr in CodigoR.readline().split(','):
    if cr != '':
        codigo.append(cr)
        
for pr in ProductoR.readline().split(','):
    if pr != '':
        producto.append(pr)
        
for prr in PrecioR.readline().split(','):
    if prr != '':
        precio.append(float(prr))
    
CodigoR.close() 
ProductoR.close() 
PrecioR.close()   

print(" ")
print("------------------------------------------------------")
print(" ")
menu__principal = int(input("Menú Principal: \n 1- ver planilla \n 2- Ingresar producto \n 3- Eliminar producto \n 4-Modificar producto \n 0- Salir: \n"))

while menu__principal != 0:
    
    if menu__principal == 1:
        for x in range(len(codigo)):
            print(f"Código: {codigo[x]}   |  Producto: {producto[x]}  |  Precio: ${precio[x]}  |")
       
    elif menu__principal == 2:
        print(f"Ingresando producto")
        codigo.append(input("Ingresa el código del producto: ").upper())
        producto.append(input("Ingresa el producto: ").title())
        precio.append(float(input("Ingresa el precio del producto: ")))
        
    elif menu__principal == 3:
        cod = input("Ingresa el código a eliminar").upper()
        for i in range(len(codigo)-1,-1,-1):
            if codigo[i] == cod:
                codigo.pop(i)
                producto.pop(i)
                precio.pop(i)
                
        print(f"Producto: {cod}---Eliminado correctamente")
        
        
        
    elif menu__principal == 4:
        cod = input("Ingresa el código a modificar:  ").upper()
        
        for x in range(len(codigo)):
            if codigo[x] == cod:
                codigo[x] = input("Ingresa el nuevo código del producto: ").upper() 
                producto[x] = input("Ingresa el nuevo producto: ").title()    
                precio[x] = float(input("Ingresa el precio del nuevo producto: ")) 
                
        print(f"Producto {cod} modificado correctamente")
        
        
    else:
        print(f"Error---Estas intentando ingresar un valor no requerido")
    menu__principal = int(input("Menú Principal: \n 1- ver planilla \n 2- Ingresar producto \n 3- Eliminar producto \n 4-Modificar producto \n 0- Salir: \n"))    
print("Fin del programa")


CodigoT = open('Codigo.txt','w')
ProductoT = open('Producto.txt','w')
PrecioT = open('Precio.txt','w')

for x in range(len(codigo)):
    CodigoT.write(codigo[x]+',')
    ProductoT.write(producto[x]+',')
    PrecioT.write(str(precio[x])+',')
    
CodigoT.close() 
ProductoT.close() 
PrecioT.close()   