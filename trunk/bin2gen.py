from struct import pack, unpack
from apps import *


MemoriaUsuario_Bytes = []
MemoriaUsuario_Bits = []
app = -1
estado = -1

for i in range(Cantidad_Bits_Usuario):
    MemoriaUsuario_Bytes.append(False)
    
for i in range(Cantidad_Bytes_Usuario):
    MemoriaUsuario_Bits.append(False)

def OnHeader_BIT():
    MemoriaUsuario_Bits

aplicaciones = []
for i in range(Cantidad_Apps):
    aplicaciones.append(Aplicacion(i,""))


def OnHeader_APLICACION():
    numApp = buff[0];
    if numApp < Cantidad_Apps:
        aplicaciones[numApp].EstadoActual = buff[1]
    

def OnHeader_ESTADO():
    numEstado = (buff[1]<<8) + buff[0];


def OnHeader_BLOQUE():
    for i in range(Cantidad_Bloques):
        numBloque = int(buff[i*6]) + (int(buff[i*6+1])<<8)
        app = numBloque/(Cantidad_Estados*Cantidad_Bloques)
        estado = (numBloque%(Cantidad_Estados*Cantidad_Bloques))/Cantidad_Bloques
        bloque = (numBloque%(Cantidad_Estados*Cantidad_Bloques)%Cantidad_Bloques)   
        aplicaciones[app].Estados[estado].Bloques[bloque] = \
            (buff[i*6+5]<<24) +(buff[i*6+4]<<16) +(buff[i*6+3]<<8) +buff[2]
    
    
def OnHeader_CONDICION():
    aplicaciones[app].Estados[estado].Condiciones[0] = buff[0]
    aplicaciones[app].Estados[estado].Condiciones[1] = buff[1]
    aplicaciones[app].Estados[estado].Condiciones[2] = buff[2]
    

def OnHeader_RESULTADO():
    aplicaciones[app].Estados[estado].Resultados[0] = buff[0]
    aplicaciones[app].Estados[estado].Resultados[1] = buff[1]


def OnHeader_SMS():
    SMS[buff[0]] = "".join(map(chr,buff[1:]))


def OnHeader_BYTE():
    MemoriaUsuario_Bytes[ buff[0] ] = buff[1]


def OnHeader_BIT():
    MemoriaUsuario_Bits[buff[0]] = bool(buff[1])


HEADERSFUNCS = {
    Header_App:         OnHeader_APLICACION,
    Header_Bloques:     OnHeader_BLOQUE,
    Header_Estado:      OnHeader_ESTADO,
    Header_Condicion:   OnHeader_CONDICION,
    Header_Resultado:   OnHeader_RESULTADO,
    Header_SMS:         OnHeader_SMS,
    Header_BYTE:        OnHeader_BYTE,
    Header_BIT:         OnHeader_BIT
    }

archivo = open("\\users\\santiago\\documents\\proyectos\\atop\\soft\\generadorsvn\\generadorapps\\binario.cb",'rb')
buff = unpack('BBB',archivo.read(3))
while buff != "":
    if buff[0] == 0xAA:
        TIPOHEADER = buff[1]
        CANTIDAD = buff[2]
        buff = unpack('B'*(CANTIDAD),archivo.read(CANTIDAD))
        if buff != "":
            HEADERSFUNCS[TIPOHEADER]()
    else: 
        break
    try:
        buff = unpack('BBB',archivo.read(3))
    except:
        continue
    
archivo.close()

for i in aplicaciones:
    for j in i.Estados:
        print j.Bloques[:],
        print " ",
print '\n'

for i,mensaje in enumerate(SMS):
    if mensaje!="":
        print "Mensaje %d: "%i + mensaje
