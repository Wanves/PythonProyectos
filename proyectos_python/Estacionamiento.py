from ast import Str
import string
from numpy.core.arrayprint import array_str
import numpy as np
ocupado = []
ocupado2 = []
ocupado3 = []
valorHoraDocente = 10
valorHoraAlumno = 5
valorHoraGeneral = 20
reca = []

class SectorDocente:
  def __init__(self,lugar1,recaudadoDocente):
    self.recaudadoDocente = recaudadoDocente
    self.lugar1 = np.zeros(50,Str)
    l1 = self.lugar1
    l1[0]=["AAA111"]
    l1[5]=["AAA222"]
    # l1[0]=(0)
    # l1[5]=(0)  
    print(" ")
    print(f"Sector Docentes: {[l1]}")
    print(" ")
    
    for i in l1:
          if i != 0:
            print(f"Patente Autos estacionados sector docente {i}") 
            ocupado.append(i)
    print(f"Lugares ocupados: {len(ocupado)}")
    recaudadoDocente =   valorHoraDocente * len(ocupado)
    
    print(f"El valor recaudado en el sector docente es: {recaudadoDocente}")
    reca.append(recaudadoDocente)
s = SectorDocente(50,0)


print(" ")
# -----------------------------------------------------------
print("----------------------------------------------------------------")
print(" ")
class SectorAlumno:
    def __init__(self,lugar2):
        self.lugar2 = np.zeros(50,Str)
        l2 = self.lugar2
        l2[3]=["BBB111"]
        l2[15]=["BBB222"]
        l2[19]=["BBB333"]
        # l2[3]=(0)
        # l2[15]=(0)
        # l2[19]=(0)
        print(" ")
        print(f"Sector Alumnos: {[l2]}")
        print(" ")
        for x in l2:
          if x != 0:
            print(f"Patente Autos estacionados sector alumnos {x}")
            ocupado2.append(x)
        print(f"Lugares ocupados: {len(ocupado2)}")
        recaudadoAlumno = valorHoraAlumno * len(ocupado2 ) 
        print(f"El valor recaudado en el sector docente es: {recaudadoAlumno}")
        reca.append(recaudadoAlumno)
s = SectorAlumno(50)
print(" ")
# -----------------------------------------------------------
print("----------------------------------------------------------------")
print(" ")
class SectorGeneral:
    
    def __init__(self,lugar3):
      self.lugar3 = np.zeros(100,Str)
      l3 = self.lugar3
      l3[3]=["CCC111"]
      l3[15]=["CCC222"]
      l3[19]=["CCC333"]
      # l3[3]=(0)
      # l3[15]=(0)
      # l3[19]=(0)
      
      print(" ")
      print(f"Sector General: {[l3]}")
      print(" ")
      for j in l3:
          if j != 0:
            print(f"Patente Autos estacionados sector general {j}")
            ocupado3.append(j)
      print(f"Lugares ocupados: {len(ocupado3)}")
      recaudadoGeneral = valorHoraGeneral * len(ocupado3)
      print(f"El valor recaudado en el sector docente es: {recaudadoGeneral}") 
      reca.append(recaudadoGeneral)
s = SectorGeneral(100)
            
total_recaudacion = 0
class Registro:
  
  def __init__(self,sector,patente,horaEntrada,horaSalida):
    self.sector = sector
    self.patente = patente
    self.horaEntrada = horaEntrada
    self.horaSalida = horaSalida
    self.costoDocente = 10
    
    
  def __str__(self):
     print(" ")
     print(f"Sector:{self.sector} Patente: {self.patente} Hora de Entrada: {self.horaEntrada} Hora de salida {self.horaSalida} Horas de estadia: {self.estadia} Costo: {self.estadia * self.costoDocente}")
  def __repr__(self):
     reca = self.estadia * self.costoDocente
     global total_recaudacion
     total_recaudacion += reca*2
    
  def mostrarDato(self):
      self.estadia = (self.horaSalida - self.horaEntrada)
      return self.estadia
     
  def ingresa(self, horaEntrada):
    return horaEntrada


class Registro2:
  
  def __init__(self,sector,patente,horaEntrada,horaSalida):
    self.sector = sector
    self.patente = patente
    self.horaEntrada = horaEntrada
    self.horaSalida = horaSalida
    self.costoAlumno = 5
    
    
  def __str__(self):
     print(" ")
     print(f"Sector:{self.sector} Patente: {self.patente} Hora de Entrada: {self.horaEntrada} Hora de salida {self.horaSalida} Horas de estadia: {self.estadia} Costo: {self.estadia * self.costoAlumno}")
     print(" ")
  def __repr__(self):
     reca = self.estadia * self.costoAlumno
     global total_recaudacion
     total_recaudacion += reca*3
     
  def mostrarDato(self):
      self.estadia = (self.horaSalida - self.horaEntrada)
      return self.estadia 
     
  def ingresa(self, horaEntrada):
    return horaEntrada
    

  
    
class Registro3:
  
  def __init__(self,sector,patente,horaEntrada,horaSalida):
    self.sector = sector
    self.patente = patente
    self.horaEntrada = horaEntrada
    self.horaSalida = horaSalida
    self.costoGeneral = 20
    
  def __str__(self):
     print(" ")
     print(f"Sector:{self.sector} Patente: {self.patente} Hora de Entrada: {self.horaEntrada} Hora de salida {self.horaSalida} Horas de estadia: {self.estadia} Costo: {self.estadia * self.costoGeneral}")
     print(" ")
  def __repr__(self):
     reca = self.estadia * self.costoGeneral
     global total_recaudacion
     total_recaudacion += reca*3
    
  def mostrarDato(self):
      self.estadia = (self.horaSalida - self.horaEntrada)
      return self.estadia
    
  def ingresa(self, horaEntrada):
    return horaEntrada
    
  
  
  
  
 
rd = Registro("Docente","AAA111",18,19)
rd2 = Registro("Docente","AAA222",10,11)


print(" ")
rd.mostrarDato()
rd.__str__()
rd2.mostrarDato()
rd2.__str__()
rd.__repr__()

print("---------------------------------------------------------------")
ra = Registro2("Alumno","BBB111",9,10)
ra2 = Registro2("Alumno","BBB222",20,21)
ra3 = Registro2("Alumno","BBB333",16,17)
print(" ")
ra.mostrarDato()
ra.__str__()
ra2.mostrarDato()
ra2.__str__()
ra3.mostrarDato()
ra3.__str__()
ra.__repr__()
print("---------------------------------------------------------------")
rg = Registro3("General","CCC111",19,20)
rg2 = Registro3("General","CCC222",12,13)
rg3 = Registro3("General","CCC333",16,17)
print(" ")
rg.mostrarDato()
rg.__str__()
rg2.mostrarDato()
rg2.__str__()
rg3.mostrarDato()
rg3.__str__()
rg.__repr__()

print(f"La recaudación total es: {total_recaudacion}")
recaudadoDocente , recaudadoAlumno, recaudadoGeneral = reca
recaTotalSectores = recaudadoDocente + recaudadoAlumno + recaudadoGeneral
print(f"La recaudación total de los sectores docente, alumno y general es: {recaTotalSectores}")