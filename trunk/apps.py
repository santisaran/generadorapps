# -*- coding: utf-8 -*-

from struct import pack,unpack

 #bits definidos en el archivo CylocDefines.h
DefinicionesBits = (
    ("Contacto", u"Estado de la entrada contacto", "p2.13"),
    ("BtnPanic", u"Estado de la entrada Pánico", "p2.10"),
    ("pulsdesact", u"Estado de la entrada pulsdesact", "p0.17"),
    ("Puerta", u"Estado de la entrada Puerta", "p1.10"),
    ("Porton",u"Estado de la entrada Porton", "p2.11"),
    ("Trailer",u"Estado de la entrada Trailer", "p2.12"),
    ("SetCorteC",u"","p1.16"),
    ("SetCorteNA",u"","p0.25"),
    ("Aux1in",u"","p0.01"),
    ("Aux2in","",""),
    ("SetCorte",u"Indica si se debe activar el rele de corte.",""),
    ("Aux1out","",""),
    ("Aux2out","",""),
    ("an0Zonas",u"""True => usar zonas, False => devolver valor AD
\t\t\tb1|b0 |zona
\t\t\tLas zonas son 0 | 0 |a
\t\t\t              0 | 1 |b
\t\t\t              1 | 0 |c
\t\t\t              1 | 1 |d""",""),

    ("an0Zb0",u"indicador zona bit bajo",""),
    ("an0Zb1",u"indicador zona bit alto",""),
    
    ("an0ZVal",u"True => dato de zona válido",""),
    ("an0",u"""False, no hay datos correctos
True, valor válido con antirrebote. (el antirrebote se define con:
Frecan0, frecuencia de muestreo en ms de entrada analógica.
CNTan0, Contador cuantos an0 dentro del rango.
CfgCNTan0, Cantidad de muestras para validar valor An0. """,""),
    
    ("an1val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an1VALOR]",""),
    ("an2val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an2VALOR]",""),
    ("an3val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an3VALOR]",""),
    ("an4val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an4VALOR]",""),
    ("an5val", u"""True => dato válido en el vector MemoriaUsuario_Bytes[an5VALOR]""",""),
    
    ("LeerAn0",u"True => petición de lectura AD0.",""),
    ("LeerAn1",u"True => petición de lectura AD1.",""),
    ("LeerAn2",u"True => petición de lectura AD2.",""),
    ("LeerAn3",u"True => petición de lectura AD3.",""),
    ("LeerAn4",u"True => petición de lectura AD4.",""),
    ("LeerAn5",u"True => petición de lectura AD5.",""),
    
    ("LeerXYZ","",""),
    
    ("Led",u"Led prendido u apagado.",""),
    ("Destellar","",""),
    ("CLed","",""),
    
    ("Aux1CfgInOut",u"Aux1 1=salida, 0=entrada",""),
    ("Aux2CfgInOut",u"Aux2 1=salida, 0=entrada",""),

    ("ErrorLed",u"Falla salida de led.",""),
    ("ErrorCorte","",""),
    ("ErrorAux1","","" ),
    ("ErrorAux2","","" ),
    
    ("Accel_Flag_DR",u"Flag indicador de dato nuevo de aceleracion disponible",""),
    ("Accel_Flag_Choque", u"Flag de accidente. Para mas informacion, ver Registro STAT",""),
    
    ("Pulsos","",""),
    ("Buzz","",""),
    ("AntenaGPSCorto","",""),
    ("AntenaGPSPresente","",""),
    ("AntenaGSMCorto","",""),
    ("AntenaGSMPresente","","")
)



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
    if len(DefinicionesBits)>i:
        Bits.append(DefinicionesBits[i][0:2])
    else:
        Bits.append(["Bit %0.3d"%i,u"Sin Descripción"])
        
Bytes = []
for i in range(Cantidad_Bytes_Usuario):
    Bytes.append("Byte %0.3d"%i)


#Aplicacion = {"AppNum":0,"Nombre":"","EstadoActual":True,"Estados":[]}
#for i in range(Cantidad_Estados):
#    Aplicacion["Estados"].append({"Bloques":[0 for i in range(Cantidad_Bloques)],"Condiciones":[0,0,0],"Resultados":[0,0],"Nombre":"","Comentario":""})


class Aplicacion():
    def __init__(self,numero, nombre):
        self.AppNum = numero
        self.Nombre = nombre
        self.EstadoActual = 0
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
muestras = 5
tiempo = 20
Entradas = (u"Contacto", u"Aux1", u"Pánico", u"Pulsador", "Porton", "CorteNA",\
    "CorteC")
ValoresEntradas = {}
for i in Entradas:
    ValoresEntradas[i] = [muestras, tiempo]

PorZonas = 0
ValorADC = 1
nZonas = ("Asup","Ainf","Bsup","Binf","Csup","Cinf","Dsup","Dinf")
Analogica = {"Asup":100,"Ainf":90,"Bsup":80,"Binf":70,"Csup":60,"Cinf":50,\
    "Dsup":40,"Dinf":30,"tiempo":5, "muestras":5, "modo":PorZonas,"comentarios":""}

#Acerca del modo : 0 modo 4 zonas, 1 modo valor ADC.

Header_App = 0x01
Header_Bloques = 0x02
Header_Estado = 0x03
Header_Condicion = 0x04
Header_Resultado = 0x05


def GenerarBin(programa):
    binario = ""
    for app in programa:
        binario = binario + chr(0xAA) + chr(Header_App)
        binario = binario + chr(app.AppNum)
        binario = binario + chr(app.EstadoActual)
        for i,estado in enumerate(app.Estados):
            EstadoAbs = (app.AppNum*Cantidad_Estados+i)
            #print "Estado: " + str(EstadoAbs)
            binario = binario + chr(0xAA) + chr(Header_Estado)
            binario = binario + chr(EstadoAbs & 0x0FF) + chr((EstadoAbs>>8) & 0x0FF)
            binario = binario + str(chr(0xAA)) + str(chr(Header_Bloques))
            for j,bloque in enumerate(estado.Bloques):               
                BloqueAbs = app.AppNum*Cantidad_Estados*Cantidad_Bloques+i*Cantidad_Bloques+j
                #print "bloque: " + str(BloqueAbs)
                binario = binario +  chr(BloqueAbs & 0x0FF) + chr((BloqueAbs>>8) & 0x0FF)
                binario = binario +\
                    chr(bloque&0x0FF)+chr(bloque>>8&0x0FF)+\
                    chr(bloque>>16&0x0FF)+chr(bloque>>24&0x0FF)
                
                    
            binario = binario + chr(0xAA) + chr(Header_Condicion)
            for i in estado.Condiciones:
                binario = binario + chr(i)
            binario = binario + chr(0xAA) + chr(Header_Resultado)
            for i in estado.Resultados:
                binario = binario + chr(i)
    return binario

def main():
    print u"Este módulo forma parte de generador.py"

if __name__ == '__main__':
    main()
