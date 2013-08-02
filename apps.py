#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from struct import pack,unpack


# Defines compartidos con C si se hace modificación, hace la misma modificación en el codigo c
Estados = ("ESTADO0", "ESTADO1", "ESTADO2", "ESTADO3", "ESTADO4", "ESTADO5", "ESTADO6", \
    "ESTADO7", "ESTADO8", "ESTADO9")

_ESTADO0 = 0
_ESTADO1 = 1
_ESTADO2 = 2
_ESTADO3 = 3
_ESTADO4 = 4
_ESTADO5 = 5
_ESTADO6 = 6
_ESTADO7 = 7
_ESTADO8 = 8
_ESTADO9 = 9

Cantidad_Apps = 20
Cantidad_Estados = 10
Cantidad_Bloques = 5
Cantidad_Bits_Usuario = 256
Cantidad_Bytes_Usuario = 256
Cantidad_SMS = 20
Cantidad_WEBs = 16
Cantidad_TEL = 10
Cantidad_MAIL = 10
Cantidad_Timers = 20

# bits definidos en el archivo CylocDefines.h
DefinicionesBits = (
# NombredelBit, descripción, valor inicial, editable, descripción avanzada (para c)
    ("False",u"Bit que permanece en 0 siempre","0",0,""),
    ("True",u"Bit que permanece en 1 siempre","1",0,""),
    ("Contacto", u"Estado de la entrada contacto", "-1", 0, "p2.13"),
    ("BtnPanic", u"Estado de la entrada Pánico", "-1", 0, "p2.10"),
    ("pulsdesact", u"Estado de la entrada pulsdesact", "-1", 0, "p0.17"),
    ("Puerta", u"Estado de la entrada Puerta", "-1", 0, "p1.10"),
    ("Porton", u"Estado de la entrada Porton", "-1", 0, "p2.11"),
    ("Trailer", u"Estado de la entrada Trailer", "-1", 0, "p2.12"),
    ("SetCorteC", u"", "-1", 0, "p1.16"),
    ("SetCorteNA", u"", "-1", 0, "p0.25"),
    ("Aux1in", u"", "-1", 0, "p0.01"),
    ("Aux2in", "", "-1", 0, ""),
    ("SetCorte", u"Indica si se debe activar el rele de corte.", "-1", 0, ""),
    ("Aux1out", "", "-1", 0, ""),
    ("Aux2out", "", "-1", 0, ""),
    ("an0Zonas", u"""True => usar zonas, False => devolver valor AD
\t\t              \tb1|b0 |zona
\t\tLas zonas son \t 0 | 0 | a
\t\t              \t 0 | 1 | b
\t\t              \t 1 | 0 | c
\t\t              \t 1 | 1 | d""", "-1", 0, ""),

    ("an0Zb0", u"indicador zona bit bajo", "-1", 0, ""),
    ("an0Zb1", u"indicador zona bit alto", "-1", 0, ""),
    
    ("an0ZVal", u"True => dato de zona válido", "-1", 0, ""),
    ("an0", u"""False, no hay datos correctos
True, valor válido con antirrebote. (el antirrebote se define con:
Frecan0, frecuencia de muestreo en ms de entrada analógica.
CNTan0, Contador cuantos an0 dentro del rango.
CfgCNTan0, Cantidad de muestras para validar valor An0. """, "-1", 0, ""),
    
    ("an1val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an1VALOR]", "-1", 0, ""),
    ("an2val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an2VALOR]", "-1", 0, ""),
    ("an3val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an3VALOR]", "-1", 0, ""),
    ("an4val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an4VALOR]", "-1", 0, ""),
    ("an5val", u"""True => dato válido en el vector MemoriaUsuario_Bytes[an5VALOR]""", "-1", 0, ""),
    
    ("LeerAn0", u"True => petición de lectura AD0.", "-1", 0, ""),
    ("LeerAn1", u"True => petición de lectura AD1.", "-1", 0, ""),
    ("LeerAn2", u"True => petición de lectura AD2.", "-1", 0, ""),
    ("LeerAn3", u"True => petición de lectura AD3.", "-1", 0, ""),
    ("LeerAn4", u"True => petición de lectura AD4.", "-1", 0, ""),
    ("LeerAn5", u"True => petición de lectura AD5.", "-1", 0, ""),
    
    ("LeerXYZ", "", "-1", 0, ""),
    
    ("Led", u"Led prendido u apagado.", "-1", 0, ""),
    ("Destellar", "", "-1", 0, ""),
    ("CLed", "", "-1", 0, ""),
    
    ("Aux1CfgInOut", u"Aux1 1=salida, 0=entrada", "-1", 0, ""),
    ("Aux2CfgInOut", u"Aux2 1=salida, 0=entrada", "-1", 0, ""),

    ("ErrorLed", u"Falla salida de led.", "-1", 0, ""),
    ("ErrorCorte", "", "-1", 0, ""),
    ("ErrorAux1", "", "-1", 0, ""),
    ("ErrorAux2", "", "-1", 0, ""),
    
    ("Accel_Flag_DR", u"Flag indicador de dato nuevo de aceleracion disponible", "-1", 0, ""),
    ("Accel_Flag_Choque", u"Flag de accidente. Para mas informacion, ver Registro STAT", "-1", 0, ""),
    
    ("Pulsos", "", "-1", 0, ""),
    ("Buzz", "", "-1", 0, ""),
    ("AntenaGPSCorto", "", "-1", 0, ""),
    ("AntenaGPSPresente", "", "-1", 0, ""),
    ("AntenaGSMCorto", "", "-1", 0, ""),
    ("AntenaGSMPresente", "", "-1", 0, ""),
)

DefinicionesBits = DefinicionesBits + \
    tuple([["sendSMS%d" % i, u"Envía Mensaje de Texto Nº %d" % i, "-1", 0, ""] for i in range(Cantidad_SMS)])

DefinicionesBits = DefinicionesBits + (("BitSendSMSPwoff","", "-1", 0, ""),("BitSendSMSGPSoff","", "-1", 0, ""),("BitSendSMSOutZone","", "-1", 0, ""))

MuestrasDefault = 5
TiempoDefault = 20

# Entradas disponibles en el localizador:

_contacto = u"Contacto"
_aux1 = u"Aux1"
_aux2 = u"Aux2"
_panico = u"Pánico"
_pulsador = u"Pulsador"
_porton = u"Portón"
_corteNA = u"CorteNA"
_corteC = u"CorteC"
_puerta = u"Puerta"
_trailer = u"Trailer"
_an0Zai = u"an0Zai"
_an0Zas = u"an0Zas"
_an0Zbi = u"an0Zbi" 
_an0Zbs = u"an0Zbs"      
_an0Zci = u"an0Zci"      
_an0Zcs = u"an0Zcs"     
_an0Zdi = u"an0Zdi"     
_an0Zds = u"an0Zds"          
_cntan0 = "CNTan0"  
_cfgcntan0 = "CfgCNTan0"
_frecan0 = "Frecan0"

Entradas = (_contacto, _aux1 , _aux2, _panico, _pulsador, _puerta, _porton , \
            _trailer, _corteNA, _corteC)

EntradasAn = (_frecan0, _cfgcntan0)

EntradasBytes = {_contacto: ["FrecContacto", "CfgCNTContacto"], _aux1:["FrecAux1in", "CfgCNTAux1in"], \
                 _aux2:["FrecAux2in", "CfgCNTAux2in"], _panico:["FrecBtnPanic", "CfgCNTBtnPanic"], \
                 _pulsador:["Frecpulsdesact", "CfgCNTpulsdesact"], _porton:["Frecporton", "CfgCNTporton"], \
                 _corteNA:["FrecCorteNA", "CfgCNTCorteNA"], _corteC:["FrecCorteC", "CfgCNTCorteC"], \
                 _puerta: ["Frecpuerta", "CfgCNTpuerta"], _trailer:["Frectrailer", "CfgCNTTrailer"],
                }



DefinicionesBytes = (\
    (EntradasBytes[_contacto][0], u"Frecuencia de muestreo contacto", "-1", 0),
    ("CNTContacto", u"Contador cuantos Contacto iguales", "-1", 0),
    (EntradasBytes[_contacto][1], u"Cantidad de muestras para validar Contacto", "-1", 0),
    (EntradasBytes[_aux1][0], u"Frecuencia de muestreo en ms de Aux1in", "-1", 0),
    ("CNTAux1in", u"Contador de Aux1in iguales", "-1", 0),
    (EntradasBytes[_aux1][1], u"Cantidad de muestras para validar Aux1in", "-1", 0),
    (EntradasBytes[_aux2][0], u"Frecuencia de muestreo en ms de Aux2in", "-1", 0),
    ("CNTAux2in", u"Contador de Aux2in iguales", "-1", 0),
    (EntradasBytes[_aux2][1], u"Cantidad de muestras para validar Aux2in", "-1", 0),
    (EntradasBytes[_panico][0], u"Frecuencia de muestreo en ms de btn pánico", "-1", 0),
    ("CNTBtnPanic", u"Contador cuantos btn pánico iguales", "-1", 0),
    (EntradasBytes[_panico][1], u"Cantidad de muestras para validar btn pánico", "-1", 0),
    (EntradasBytes[_pulsador][0], u"Frecuencia de muestreo en ms del puls desactivacion", "-1", 0),
    ("CNTpulsdesact", u"Contador cuantos puls desact iguales", "-1", 0),
    (EntradasBytes[_pulsador][1], u"Cantidad de muestras para validar puls desactivacion", "-1", 0),
    (EntradasBytes[_puerta][0], u"Frecuencia de muestreo en ms de puerta", "-1", 0),
    ("CNTpuerta", u"Contador cuantos puerta iguales", "-1", 0),
    (EntradasBytes[_puerta][1], u"Cantidad de muestras para validar puerta", "-1", 0),
    (EntradasBytes[_porton][0], u"Frecuencia de muestreo en ms de portón", "-1", 0),
    ("CNTporton", u"Contador cuantos portón iguales", "-1", 0),
    (EntradasBytes[_porton][1], u"Cantidad de muestras para validar portón", "-1", 0),
    (EntradasBytes[_trailer][0], u"Frecuencia de muestreo en ms de trailer", "-1", 0),
    ("CNTtrailer", u"Contador cuantos trailer iguales", "-1", 0),
    (EntradasBytes[_trailer][1], u"Cantidad de muestras para validar trailer", "-1", 0),
    (EntradasBytes[_corteNA][0], u"Frecuencia de muestreo en ms de CorteNA", "-1", 0),
    ("CNTCorteNA", u"Contador cuantos CorteNA iguales", "-1", 0),
    (EntradasBytes[_corteNA][1], u"Cantidad de muestras para validar CorteNA", "-1", 0),
    (EntradasBytes[_corteC][0], u"Frecuencia de muestreo en ms de CorteC", "-1", 0),
    ("CNTCorteC", u"Contador cuantos CorteC iguales", "-1", 0),
    (EntradasBytes[_corteC][1], u"Cantidad de muestras para validar CorteC", "-1", 0),
    ("TiempoCorte", u"Tiempo entre activacion y lectura de la realimentacion", "-1", 0),
    ("TiempoAux1", u"", "-1", 0),
    ("TiempoAux2", u"", "-1", 0),
    ("CorteReintentos", u"", "-1", 0),
    ("Aux1Reintentos", u"", "-1", 0),
    ("Aux2Reintentos", u"", "-1", 0),
    (_frecan0, u"Frecuencia de muestreo en ms de entrada analógica", "-1", 0),
    ("FrecVccTest", u"Frecuencia de muestreo en ms de entrada Vcc", "-1", 0),
    (_cntan0, u"Contador cuantos an0 dentro del rango", "-1", 0),
    (_cfgcntan0, u"Cantidad de muestras para validar AD0", "-1", 0),
    ("an0VALOR", u"Valor de la conversión para AD0", "-1", 0),
    (_an0Zai, u"Límite inferior zona A", "-1", 0),
    (_an0Zas, u"Límite superior zona A", "-1", 0),
    (_an0Zbi, u"Límite inferior zona B", "-1", 0),
    (_an0Zbs, u"Límite superior zona B", "-1", 0),
    (_an0Zci, u"Límite inferior zona C", "-1", 0),
    (_an0Zcs, u"Límite superior zona C", "-1", 0),
    (_an0Zdi, u"Límite inferior zona D", "-1", 0),
    (_an0Zds, u"Límite superior zona D", "-1", 0),
    ("an1VALOR", u"Valor de la conversión para AD1", "-1", 0),
    ("an2VALOR", u"Valor de la conversión para AD2", "-1", 0),
    ("an3VALOR", u"Valor de la conversión para AD3", "-1", 0),
    ("an4VALOR", u"Valor de la conversión para AD4", "-1", 0),
    ("an5VALOR", u"Valor de la conversión para AD5", "-1", 0),
    ("an0ZONA", u"", "-1", 0),
    ("VccVALOR", u"", "-1", 0),
    ("FrecLed", u"Frecuencia de encendido ms de LED", "-1", 0),
    ("CfgCNTLed", u"Configuración cantidad de destellos led cada vez que es disparado", "-1", 0),
    ("CNTLed", u"", "-1", 0),
    ("DutyLed", u"porcentaje apagado encendido 50ms de paso", "-1", 0),
    ("CfgCNTCLed", u"", "-1", 0),
    ("TMRLed", u"Timer incrementado cada 1ms", "-1", 0),
    ("Accel_X_MSB", u"MSB de la aceleracion Actual eje X", "-1", 0),
    ("Accel_X_LSB", u"LSB de la aceleracion Actual eje X", "-1", 0),
    ("Accel_Y_MSB", u"MSB de la aceleracion Actual eje Y", "-1", 0),
    ("Accel_Y_LSB", u"LSB de la aceleracion Actual eje Y", "-1", 0),
    ("Accel_Z_MSB", u"MSB de la aceleracion Actual eje Z", "-1", 0),
    ("Accel_Z_LSB", u"LSB de la aceleracion Actual eje Z", "-1", 0),
    ("Accel_StChoque", u"Copia del registro STATE del detector de transitorios del acelerometro\nActualizado solo cuando hay un choque", "-1", 0),
    ("Frecbuzz", u"", "-1", 0),
    ("CfgCNTbuzz", u"", "-1", 0),
    ("CNTbuzz", u"", "-1", 0),
    ("Frecoscbuzz", u"", "-1", 0),
    ("Dutyenc", u"", "-1", 0)
)


SMS = []
for i in range(Cantidad_SMS):
    SMS.append("")
    
TEL = []
for i in range(Cantidad_TEL):
    TEL.append(u"")
                    
TIMERS = []
for i in range(Cantidad_Timers):
    # 
    # evento único:
    # tipo=2 , año, mes, día, hora, minuto, segundo, setear bit , nombre 
    #
    # evento repetitivo:
    # tipo=1 , repeticiones ,días[15:8],días[7:0], horas, minutos, segundos, setear bit , nombre
    TIMERS.append({"tipo":0,"repeticiones":0,"anio":2013,"mes":06,"dia":25,"hora":0,"minuto":0,"segundo":0,"bit":72,"nombre":""})

SERVERS = []
for i in range(Cantidad_WEBs):
    #el primer campo es true si se trata de una dirección web
    #o false si es una dirección IP
    SERVERS.append([True,""])
                    
MAIL= []
for i in range(Cantidad_MAIL):
    MAIL.append("")
    
# /*
# * BLOQUES:
# *  [31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1  0 ]
# *         |  TIPO BLOQUE    |     parametro3        |   parametro2       |       parametro1         |
# */
# // Defines Tipos de Bloques (Ojo si se cambia algo cambiar también el archivo CylocDefines.h)

# // Almacenado en los bits [29:24] de la informacion de los bloques (uint32_t)


BloquesPosibles = (u"Null", u"Incrementar", u"Decrementar", u"AND_2_BIT", \
    u"OR_2_BIT", u"NOT_BIT", u"Sumar_2_Reg", u"Restar_2_Reg", u"Invertir_Reg", \
    u"Transmitir_BB", u"SetBit",u"Set3Bits", u"ClrBit",u"Clr3Bit", u"ClrReg", u"CopiarRegistro",\
    u"CargarValor")

BloquesDic = {}

for i in range(len(BloquesPosibles)):
    BloquesDic[i] = BloquesPosibles[i]

Bloque_Null = 0
Bloque_Incrementar = 1
Bloque_Decrementar = 2
Bloque_AND_2_BIT = 3
Bloque_OR_2_BIT = 4
Bloque_NOT_BIT = 5
Bloque_Sumar_2_Reg = 6
Bloque_Restar_2_Reg = 7
Bloque_Invertir_Reg = 8
Bloque_Transmitir_BB = 9
Bloque_SetBit = 10
Bloque_Set3Bit = 11
Bloque_ClrBit = 12
Bloque_Clr3Bit = 13
Bloque_ClrReg = 14
Bloque_CopiarRegistro = 15
Bloque_CargarValor = 16

# // Defines Tipos de Condiciones
CondicionesPosibles = ("NULL", "Mayor", "Menor", "Igual", "Bit_True", "Bit_False")
Condicion_NULL = 0
Condicion_Mayor = 1
Condicion_Menor = 2
Condicion_Igual = 3
Condicion_Bit_True = 4
Condicion_Bit_False = 5

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
tipoEstado = 0x00
tipoBloque = 0x02
tipoCondiciones = 0x22
tipoResultados = 0x33
tipoAppCompleta = 0x44

Bits = []
for i in range(Cantidad_Bits_Usuario):
    if len(DefinicionesBits) > i:
        Bits.append(list(DefinicionesBits[i][0:4]))
    else:
        Bits.append(["Bit %0.3d" % i, u"Sin Descripción", "-1", 1])
        
Bytes = []
for i in range(Cantidad_Bytes_Usuario):
    if len(DefinicionesBytes) > i:
        Bytes.append(list(DefinicionesBytes[i]))
        # copia los valores de Definiciones bytes en una lista de listas.
    else:
        Bytes.append(["Byte %0.3d" % i, "", "-1", 1])


# Aplicacion = {"AppNum":0,"Nombre":"","EstadoActual":True,"Estados":[]}
# for i in range(Cantidad_Estados):
#    Aplicacion["Estados"].append({"Bloques":[0 for i in range(Cantidad_Bloques)],"Condiciones":[0,0,0],"Resultados":[0,0],"Nombre":"","Comentario":""})


class Aplicacion():
    """Clase que contiene todos los datos de una aplicacion"""
    def __init__(self, numero, nombre):
        self.AppNum = numero
        self.Nombre = nombre
        self.EstadoActual = 0
        self.Estados = []
        for i in range(Cantidad_Estados):
            self.Estados.append(Estado())

    def copy(self):
        App = Aplicacion(self.AppNum, self.Nombre)
        App.EstadoActual = self.EstadoActual
        App.Estados = []
        for i in self.Estados:
            App.Estados.append(i.copy())
        return App


class Estado():
    """variables de la clase estado"""
    def __init__(self):
        self.Bloques = [Bloque_Null, Bloque_Null, Bloque_Null, Bloque_Null, Bloque_Null]
        self.Condiciones = [Condicion_NULL, PARAMETRO1, PARAMETRO2]
        self.Resultados = [_ESTADO0, _ESTADO0]
        self.Nombre = ""
        self.Comentario = ""
    def copy(self):
        EST = Estado()
        EST.Bloques = self.Bloques[:]
        EST.Condiciones = self.Condiciones[:]
        EST.Resultados = self.Resultados[:]
        EST.Nombre = "%s" % self.Nombre
        EST.Comentario = "%s" % self.Comentario
        return EST
                
class Programa():
    """Clase que contiene un programa completo, con N aplicaciones, valores
    bits, valores bytes, nombres de bytes y bits y SMSs.
    recibe como parámetros una lista de aplicaciones, una lista de listas con
    la configuracion de bits, una lista de listas con la configuracion de los 
    bytes, y una lista con los mensajes de texto"""
    def __init__(self, aplicaciones=False , cfgBits=False ,\
            cfgBytes=False , cfgSMS=False , cfgMails=False,\
            cfgTel=False, cfgServers=False):
        
        self.aplicaciones = []
        if (aplicaciones != False) and (len(aplicaciones) == Cantidad_Apps):
            """solo cargar si es una lista completa de aplicaciones"""
            for app in aplicaciones:
                self.aplicaciones.append(app.copy())
        else:
            """cargar aplicaciones vacías"""
            for i in range(Cantidad_Apps):
                self.aplicaciones.append(Aplicacion(i, ""))
        
        self.Bits = []
        if cfgBits != False:
            self.Bits = cfgBits[:]
        else:
            self.Bits = Bits[:]
        
        self.Bytes = []
        if cfgBytes != False:
            self.Bytes = cfgBytes[:]
        else:
            self.Bytes = Bytes[:]
        
        self.SMS = []
        if cfgSMS != False:
            self.SMS = cfgSMS[:]
        else:
            self.SMS = SMS[:]
            
        self.Mails = []
        if cfgMails != False:
            self.Mails = cfgMails
        
        self.Tel = []
        if cfgTel != False:
            self.Tel = cfgTel
        
        self.Servers = []
        if cfgServers != False:
            self.Servers = cfgServers
            
            
        print "Programa creado"        

PorZonas = False
ValorADC = True
nZonas = (_an0Zas, _an0Zai, _an0Zbs, _an0Zbi, _an0Zcs, _an0Zci, _an0Zds, _an0Zdi)        

Analogica = { nZonas[0]:100, nZonas[1]:90, nZonas[2]:80, nZonas[3]:70, nZonas[4]:60, nZonas[5]:50, \
        nZonas[6]:40, nZonas[7]:30, "tiempo":5, "muestras":5, "modo":PorZonas, \
        "comentarios":""}

# Acerca del modo : 0 modo 4 zonas, 1 modo valor ADC.

HEADER_APP = 0x01
HEADER_BLOQUES = 0x02
HEADER_ESTADO = 0x03
HEADER_CONDICION = 0x04
HEADER_RESULTADO = 0x05
HEADER_SMS = 0x06
HEADER_BYTE = 0x07
HEADER_BIT = 0x08
HEADER_TEL = 0x09
HEADER_IP = 0x0a
HEADER_WWW = 0x0b
HEADER_MAIL = 0x0c
HEADER_TIMER = 0x0d
HEADER_END = 0x0e
HEADER_ERROR_LECTURA = 0x0f

def GenerarBin(programa):
    binario = ""
    for app in programa:
        binario = binario + chr(0xAA) + chr(HEADER_APP)
        # Enviar encabezado de tipo App y tamaño
        nextstring = ""
        nextstring += chr(app.AppNum) + chr(app.EstadoActual)
        binario += chr(len(nextstring)) + nextstring
        
        for i, estado in enumerate(app.Estados):
            EstadoAbs = (app.AppNum * Cantidad_Estados + i)
            # print "Estado: " + str(EstadoAbs)
            
            binario = binario + chr(0xAA) + chr(HEADER_ESTADO)
            nextstring = ""
            nextstring += chr(EstadoAbs & 0x0FF) + chr((EstadoAbs >> 8) & 0x0FF)
            binario += chr(len(nextstring)) + nextstring
            
            binario += str(chr(0xAA)) + str(chr(HEADER_BLOQUES))
            nextstring = ""
            for j, bloque in enumerate(estado.Bloques):
                BloqueAbs = app.AppNum * Cantidad_Estados * Cantidad_Bloques + i * Cantidad_Bloques + j
                nextstring += chr(BloqueAbs & 0x0FF) + chr((BloqueAbs >> 8) & 0x0FF)
                nextstring += chr(bloque & 0x0FF) + chr(bloque >> 8 & 0x0FF) + \
                    chr(bloque >> 16 & 0x0FF) + chr(bloque >> 24 & 0x0FF)
            binario += chr(len(nextstring)) + nextstring
                    
            binario = binario + chr(0xAA) + chr(HEADER_CONDICION)
            nextstring = ""
            for i in estado.Condiciones:
                nextstring += chr(i)
            binario += chr(len(nextstring)) + nextstring
            
            nextstring = ""
            binario += chr(0xAA) + chr(HEADER_RESULTADO)
            for i in estado.Resultados:
                nextstring += chr(i)
            binario += chr(len(nextstring)) + nextstring
            
    return binario

def main():   
    print u"Este módulo forma parte de generador.py"

if __name__ == '__main__':
    main()
