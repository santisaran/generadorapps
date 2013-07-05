#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bin2gen.py
#
#########################################################################
#    Módulo encargado de cargar los datos desde un archivo binario en el  
# software generador de apps. generador.py
#
#
#  Copyright 2013 santiago <spaleka@cylgem.com.ar>
#

Unable = 0
Fecha = 1
Timer = 2
Mensual = 3

from struct import pack, unpack
from apps import *

class CargarBinario():
    def __init__(self,nombrearchivo):
        self.MemoriaUsuario_Bytes = []
        self.MemoriaUsuario_Bits = []
        self.app = -1
        self.estado = -1
        self.SMS = SMS[:]
        self.binBIT = Bits[:]
        self.binBYTE = Bytes[:]
        self.telefono = TEL[:]
        self.servers = SERVERS[:]
        self.mails = MAIL[:]
        self.timers = TIMERS[:]
        self.nombrearchivo = nombrearchivo
        #for i in range(Cantidad_Bits_Usuario):
        #   self.MemoriaUsuario_Bytes.append(-1)
    
        #for i in range(Cantidad_Bytes_Usuario):
        #   self.MemoriaUsuario_Bits.append(False)
        
        self.aplicaciones = []
        for i in range(Cantidad_Apps):
            self.aplicaciones.append(Aplicacion(i,""))

    def OnHeader_APLICACION(self):
        self.numApp = self.buff[0];
        if self.numApp < Cantidad_Apps:
            self.aplicaciones[self.numApp].EstadoActual = self.buff[1]
    
    def OnHeader_ESTADO(self):
        self.numEstado = (self.buff[1]<<8) + self.buff[0];


    def OnHeader_BLOQUE(self):
        for i in range(Cantidad_Bloques):
            self.numBloque = int(self.buff[i*6]) + (int(self.buff[i*6+1])<<8)
            self.app = self.numBloque/(Cantidad_Estados*Cantidad_Bloques)
            self.estado = (self.numBloque%(Cantidad_Estados*Cantidad_Bloques))/Cantidad_Bloques
            self.bloque = (self.numBloque%(Cantidad_Estados*Cantidad_Bloques)%Cantidad_Bloques)   
            self.aplicaciones[self.app].Estados[self.estado].Bloques[self.bloque] = \
                    (self.buff[i*6+5]<<24) + (self.buff[i*6+4]<<16) \
                    +(self.buff[i*6+3]<<8) +  self.buff[2]
        
        
    def OnHeader_CONDICION(self):
        self.aplicaciones[self.app].Estados[self.estado].Condiciones[0] = self.buff[0]
        self.aplicaciones[self.app].Estados[self.estado].Condiciones[1] = self.buff[1]
        self.aplicaciones[self.app].Estados[self.estado].Condiciones[2] = self.buff[2]
        
    
    def OnHeader_RESULTADO(self):
        self.aplicaciones[self.app].Estados[self.estado].Resultados[0] = self.buff[0]
        self.aplicaciones[self.app].Estados[self.estado].Resultados[1] = self.buff[1]
    
    
    def OnHeader_SMS(self):
        self.SMS[self.buff[0]] = "".join(map(chr,self.buff[1:]))
    
    
    def OnHeader_BYTE(self):
        self.binBYTE[ self.buff[0]][2] = self.buff[1]
        #self.MemoriaUsuario_Bytes[ self.buff[0] ] = self.buff[1]
    
    
    def OnHeader_BIT(self):
        self.binBIT[self.buff[0]][2] = bool(self.buff[1])
        #self.MemoriaUsuario_Bits[self.buff[0]] = bool(self.buff[1])
        
    def OnHeader_TEL(self):
        self.telefono[self.buff[0]] = "".join(map(chr,self.buff[1:]))
        
    def OnHeader_IP(self):
        self.servers[self.buff[0]][0] = False
        cadena = ""
        for i in map(str,self.buff[1:]):
            cadena += i+"."
        self.servers[self.buff[0]][1] = cadena[:-1]
                
    def OnHeader_WWW(self):
        self.servers[self.buff[0]][0] = True
        self.servers[self.buff[0]][1] = "".join(map(chr,self.buff[1:]))
            
    def OnHeader_MAIL(self):
        self.mails[self.buff[0]] = "".join(map(chr,self.buff[1:]))
        
    def OnHeader_TIMER(self):
        self.timers[self.buff[0]]["tipo"] = ((self.buff[1]) & 0x03)
        if self.timers[self.buff[0]]["tipo"] ==  Mensual:
            self.timers[self.buff[0]]["repeticiones"] = (self.buff[1]>>2) & 0x3F + (self.buff[2]<<6&0x0FC0)
            self.timers[self.buff[0]]["dia"] = self.buff[4]
            self.timers[self.buff[0]]["hora"] = self.buff[5]
            self.timers[self.buff[0]]["minuto"] = self.buff[6]
            self.timers[self.buff[0]]["segundo"] = self.buff[7]
            self.timers[self.buff[0]]["bit"] = self.buff[8]
            print self.timers[self.buff[0]]
        elif self.timers[self.buff[0]]["tipo"] == Fecha:
            self.timers[self.buff[0]]["anio"] = (self.buff[1]>>2) & 0x3F + (self.buff[2]<<6&0x0FC0)
            self.timers[self.buff[0]]["mes"] = self.buff[3]-1
            self.timers[self.buff[0]]["dia"] = self.buff[4]
            self.timers[self.buff[0]]["hora"] = self.buff[5]
            self.timers[self.buff[0]]["minuto"] = self.buff[6]
            self.timers[self.buff[0]]["segundo"] = self.buff[7]
            self.timers[self.buff[0]]["bit"] = self.buff[8]
            print self.timers[self.buff[0]]
        elif self.timers[self.buff[0]]["tipo"] == Timer:
            self.timers[self.buff[0]]["repeticiones"] = (self.buff[1]>>2) & 0x3F + (self.buff[2]<<6&0x0FC0)
            intervalo = self.buff[3]*256*256*256+self.buff[4]*256*256+self.buff[5]*256+self.buff[6]
            self.timers[self.buff[0]]["dia"] = intervalo/(3600*24)
            self.timers[self.buff[0]]["hora"] = intervalo%(3600*24)/3600
            self.timers[self.buff[0]]["minuto"] = intervalo%(3600)/60
            self.timers[self.buff[0]]["segundo"] = intervalo%60
            self.timers[self.buff[0]]["bit"] = self.buff[8]
            print self.timers[self.buff[0]]
    
    def OnHeaderErrorLectura(self):
        print "ERROR AL CARGAR ARCHIVO"
    
    def OnHeader_END(self):
        pass
            
    def CargarArchivo(self):
        self.HEADERSFUNCS = {
            HEADER_APP:         self.OnHeader_APLICACION,
            HEADER_BLOQUES:     self.OnHeader_BLOQUE,
            HEADER_ESTADO:      self.OnHeader_ESTADO,
            HEADER_CONDICION:   self.OnHeader_CONDICION,
            HEADER_RESULTADO:   self.OnHeader_RESULTADO,
            HEADER_SMS:         self.OnHeader_SMS,
            HEADER_BYTE:        self.OnHeader_BYTE,
            HEADER_BIT:         self.OnHeader_BIT,
            HEADER_TEL:         self.OnHeader_TEL,
            HEADER_IP:          self.OnHeader_IP,
            HEADER_WWW:         self.OnHeader_WWW,
            HEADER_MAIL:        self.OnHeader_MAIL,
            HEADER_TIMER:       self.OnHeader_TIMER,
            HEADER_END:         self.OnHeader_END,
            HEADER_ERROR_LECTURA:  self.OnHeaderErrorLectura,
            }
        self.archivo = open(self.nombrearchivo,'rb')
        lectura = self.archivo.read(3)
        while lectura != "":
            
            self.buff = unpack('BBB',lectura)
            if self.buff[0] == 0xAA:
                
                TIPOHEADER = self.buff[1]
                CANTIDAD = self.buff[2]
                lectura = self.archivo.read(CANTIDAD)
                try:
                    self.buff = unpack('B'*(CANTIDAD),lectura)
                except:
                    self.archivo.close()
                    return False
                if self.buff != "":
                
                    self.HEADERSFUNCS[TIPOHEADER]()
            else: 
                
                print "Error al cargar archivo binario"
                self.archivo.close()
                return False
                break
                
            lectura = self.archivo.read(3)
            
        self.programa = Programa(\
                self.aplicaciones ,\
                self.binBYTE,\
                self.binBIT,\
                self.SMS,\
                self.mails,\
                self.telefono,\
                self.servers,\
                )
        
        self.archivo.close()
        return True
        
    
    def VerApps(self):
        """Función que imprime los valores leidos del archivo binario"""
    
        for i in self.aplicaciones:
            for j in i.Estados:
                print [hex(resultado) for resultado in j.Bloques[:]]
        print '\n'
        
        for i,mensaje in enumerate(self.SMS):
            if mensaje!="":
                print "Mensaje %d: "%i + mensaje
                print ""
    
    def VerPrograma(self):
        """ Imprime en pantalla los datos cargados en la clase programa
        que fueron leidos desde el archivo binario
        """
        
        for i in self.programa.aplicaciones:
            for j in i.Estados:
                print [hex(resultado) for resultado in j.Bloques[:]]
        print '\n'
    
        for i,mensaje in enumerate(self.programa.SMS):
            if mensaje!="":
                print "Mensaje %d: "%i + mensaje
                print ""
        
        for i in self.programa.Bits:
            print i
            
        for i in self.programa.Bytes:
            print i

if __name__ == '__main__':
    Generar = CargarBinario()
    Generar.CargarArchivo()
    Generar.VerPrograma()
