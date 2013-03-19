from struct import pack, unpack
from apps import *



class CargarBinario():
    def __init__(self):
        self.MemoriaUsuario_Bytes = []
        self.MemoriaUsuario_Bits = []
        self.app = -1
        self.estado = -1
        self.SMS = SMS[:]
        for i in range(Cantidad_Bits_Usuario):
            self.MemoriaUsuario_Bytes.append(False)
    
        for i in range(Cantidad_Bytes_Usuario):
            self.MemoriaUsuario_Bits.append(False)
        
        self.aplicaciones = []
        for i in range(Cantidad_Apps):
            self.aplicaciones.append(Aplicacion(i,""))

    def OnHeader_BIT(self):
        self.MemoriaUsuario_Bits

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
        self.MemoriaUsuario_Bytes[ self.buff[0] ] = self.buff[1]
    
    
    def OnHeader_BIT(self):
        self.MemoriaUsuario_Bits[self.buff[0]] = bool(self.buff[1])
    
        
    def CargarArchivo(self):
        self.HEADERSFUNCS = {
            Header_App:        self.OnHeader_APLICACION,
            Header_Bloques:    self.OnHeader_BLOQUE,
            Header_Estado:     self.OnHeader_ESTADO,
            Header_Condicion:  self.OnHeader_CONDICION,
            Header_Resultado:  self.OnHeader_RESULTADO,
            Header_SMS:        self.OnHeader_SMS,
            Header_BYTE:       self.OnHeader_BYTE,
            Header_BIT:        self.OnHeader_BIT
            }
        self.archivo = open("\\users\\santiago\\documents\\proyectos\\atop\\soft\\generadorsvn\\generadorapps\\binario.cb",'rb')
        self.buff = unpack('BBB',self.archivo.read(3))
        while self.buff != "":
            if self.buff[0] == 0xAA:
                TIPOHEADER = self.buff[1]
                CANTIDAD = self.buff[2]
                self.buff = unpack('B'*(CANTIDAD),self.archivo.read(CANTIDAD))
                if self.buff != "":
                    self.HEADERSFUNCS[TIPOHEADER]()
            else: 
                break
            try:
                self.buff = unpack('BBB',self.archivo.read(3))
            except:
                continue
            
        self.archivo.close()
    
    def VerApps(self):
        for i in self.aplicaciones:
            for j in i.Estados:
                print [hex(valor) for valor in j.Bloques[:]]
        print '\n'
        
        for i,mensaje in enumerate(self.SMS):
            if mensaje!="":
                print "Mensaje %d: "%i + mensaje

if __name__ == '__main__':
    Generar = CargarBinario()
    Generar.CargarArchivo()
    Generar.VerApps()
