# -*- coding: utf-8 -*-
import copy
#Defines compartidos con C si se hace modificación, hace la misma modificación en el codigo c
Estados = ( "ESTADO0","ESTADO1","ESTADO2","ESTADO3","ESTADO4","ESTADO5","ESTADO6",\
    "ESTADO7","ESTADO8","ESTADO9")


ESTADO0=0
ESTADO1=1
ESTADO2=2
ESTADO3=3
ESTADO4=4
ESTADO5=5
ESTADO6=6
ESTADO7=7
ESTADO8=8
ESTADO9=9

Cantidad_Apps    = 20
Cantidad_Estados = 10
Cantidad_Bloques = 5
Cantidad_Bits_Usuario = 256
Cantidad_Bytes_Usuario = 256

#/*
#* BLOQUES:
#*  [31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1  0 ]
#*         |  TIPO BLOQUE    |     parametro3        |   parametro2       |       parametro1         |
#*/
#// Defines Tipos de Bloques (Ojo si se cambia algo cambiar también el archivo CylocDefines.h)

#// Almacenado en los bits [29:24] de la informacion de los bloques (uint32_t)

BloquesPosibles = (u"Null",u"Incrementar",u"Decrementar",u"AND_2_BIT",\
    u"OR_2_BIT",u"NOT_BIT",u"Sumar_2_Reg",u"Restar_2_Reg",u"Invertir_Reg",\
    u"Transmitir_BB",u"SetBit",u"ClrBit",u"ClrReg",u"CopiarRegistro")

BloquesDic = {}

for i in range(len(BloquesPosibles)):
    BloquesDic[i] = BloquesPosibles[i]

Bloque_Null             =   0
Bloque_Incrementar      =   1
Bloque_Decrementar      =   2
Bloque_AND_2_BIT        =   3
Bloque_OR_2_BIT         =   4
Bloque_NOT_BIT          =   5
Bloque_Sumar_2_Reg      =   6
Bloque_Restar_2_Reg     =   7
Bloque_Invertir_Reg     =   8
Bloque_Transmitir_BB    =   9
Bloque_SetBit           =   10
Bloque_ClrBit           =   11
Bloque_ClrReg           =   12
Bloque_CopiarRegistro   =   13

#// Defines Tipos de Condiciones
CondicionesPosibles = ("NULL","Mayor","Menor","Igual","Bit_True","Bit_False")
Condicion_NULL      =   0
Condicion_Mayor     =   1
Condicion_Menor     =   2
Condicion_Igual     =   3
Condicion_Bit_True  =   4
Condicion_Bit_False =   5

PARAMETRO1 = 0
PARAMETRO2 = 0
PARAMETRO3 = 0


# información para la generación del archivo binario.
# lista = [AA,tamaño,tipo de dato, ]
# el tamaño es en bytes de la lista completa (incluye AA)
    
# Hay 10 estados por aplicación, por lo que en total existen 10*20 estados = 200 estados
# Por cada estado hay 5 bloques por lo que existen 5+200 bloques
# Una condición de 3 bytes por estado 200 condiciones (600 bytes)
# Un resultado  de 2 bytes por estado 200 resultados  (400 bytes)
    
    
# lista = [AA,tamaño, Estado , appnº, estadoapp, appnº, estadoapp......, appnº, estadoapp]
# lista = [AA,tamaño, Bloques,bloquenº(16bit),bloque(32bit),bloquenº(16bit),bloque(32bit),.... bloquenº(16bit),bloque(32bit)]
# lista = [AA,tamaño, Condiciones, nº(8bit) , 
# lista = [AA,tamaño, Resultados, 
    
# Tipo de dato:
tipoEstado          = 0x00
tipoBloque          = 0x02  
tipoCondiciones     = 0x22
tipoResultados      = 0x33
tipoAppCompleta     = 0x44
Bits = []
for i in range(Cantidad_Bits_Usuario):
    Bits.append("Bit %0.3d"%i)
Bytes = []
for i in range(Cantidad_Bytes_Usuario):
    Bytes.append("Byte %0.3d"%i)
        

#Aplicacion = {"AppNum":0,"Nombre":"","EstadoActual":True,"Estados":[]}
#for i in range(Cantidad_Estados):
#    Aplicacion["Estados"].append({"Bloques":[0 for i in range(Cantidad_Bloques)],"Condiciones":[0,0,0],"Resultados":[0,0],"Nombre":"","Comentario":""})


class Aplicacion(object):
    def __init__(self,numero, nombre):
        self.AppNum = numero
        self.Nombre = nombre
        self.EstadoActual = None
        class Estado():
            def __init__(self):
                self.Bloques     = [Bloque_Null,Bloque_Null,Bloque_Null,Bloque_Null,Bloque_Null]
                self.Condiciones = [Condicion_NULL,PARAMETRO1,PARAMETRO2]
                self.Resultados  = [ESTADO0,ESTADO0]
                self.Nombre = ""
                self.Comentario = ""
            def copy(self):
                EST = Estado()
                EST.Bloques = self.Bloques[:]
                EST.Condiciones = self.Condiciones[:]
                EST.Resultados = self.Resultados[:]
                EST.Nombre = "%s"%self.Nombre
                EST.Comentario = "%s"%self.Comentario
                return EST
        self.Estados = []
        for i in range(Cantidad_Estados):
            self.Estados.append(Estado())
    
    def copy(self):
        App = Aplicacion(self.AppNum,self.Nombre)
        App.EstadoActual = self.EstadoActual
        App.Estados = []
        for i in self.Estados:
            App.Estados.append(i.copy())
        return App
        
        
def main():
    app1 = Aplicacion(1,"ap")
    app2 = app1.copy()

    app1.Nombre = "aplicacion1"
    print app1.Nombre
    print app2.Nombre
    app1.AppNum = 2
    print app1.AppNum
    print app2.AppNum
    app1.EstadoActual = 2
    print app1.EstadoActual
    print app2.EstadoActual
    
    app1.Estados[0].Bloques[0] = 255
    print app1.Estados[0].Bloques[0]
    print app2.Estados[0].Bloques[0]
    
    app1.Estados[0].Nombre = "unnombre"
    print app1.Estados[0].Nombre
    print app2.Estados[0].Nombre

    
    
    raw_input()
    
    print "Estados app1"
    for i in app1.Estados:
        print i
        print i.Bloques
        print i.Condiciones
        print i.Resultados
        print i.Nombre
        print i.Comentario
    
    print "\n\nEstados app2"
    for i in app2.Estados:
        print i
        print i.Bloques
        print i.Condiciones
        print i.Resultados
        print i.Nombre
        print i.Comentario

if __name__ == '__main__':
	main()
