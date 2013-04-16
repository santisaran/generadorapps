#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generador.py
#
#  Copyright 2013 santiago <spaleka@cylgem.com.ar>
#

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
        self.binBYTE[ self.buff[0] ][2] = self.buff[1]
        #self.MemoriaUsuario_Bytes[ self.buff[0] ] = self.buff[1]
    
    
    def OnHeader_BIT(self):
        self.binBIT[self.buff[0]][2] = bool(self.buff[1])
        #self.MemoriaUsuario_Bits[self.buff[0]] = bool(self.buff[1])
        
    def OnHeader_END(self):
        pass
    
        
    def CargarArchivo(self):
        self.HEADERSFUNCS = {
                Header_App:        self.OnHeader_APLICACION,
                Header_Bloques:    self.OnHeader_BLOQUE,
                Header_Estado:     self.OnHeader_ESTADO,
                Header_Condicion:  self.OnHeader_CONDICION,
                Header_Resultado:  self.OnHeader_RESULTADO,
                Header_SMS:        self.OnHeader_SMS,
                Header_BYTE:       self.OnHeader_BYTE,
                Header_BIT:        self.OnHeader_BIT,
                Header_END:        self.OnHeader_END
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
                self.SMS\
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
