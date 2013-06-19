#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generador.py
#
#  Copyright 2013 santiago <spaleka@cylgem.com.ar>
#6


#TODO usar isModified() para guardar cambios.
#TODO independizar MODIFIDACO para cada ventana
#TODO guardar SMS en binario

import os
import shelve

import wx
import wx.lib.masked as  masked

import gui

import const

from apps import *
from generarheader import tupleBits,tupleBytes

const.VERSION = 0.1

#Indices de las listas Bytes y Bits
const.Valor = 2
const.Nombre = 0
const.Def = 1
const.mod = 3
const.defavan = 4

global DIRACTUAL
#DIRACTUAL = os.getenv("HOME")
DIRACTUAL = os.getcwd()
#Variables globales
global miEstados
# Nombres de la lista de estados posibles
miEstados = Estados[:]
# Al inicio la toma del modulo apps.py

global miBits
# Lista de nombres de Bits
miBits = Bits[:]

global miBytes
# Lista de nombres de los Bytes
miBytes= Bytes[:]

global miSMS
miSMS = SMS[:]

global miTEL
miTEL = TEL[:]

global miSERVERS
miSERVERS = SERVERS[:]

global miMAIL                    
miMAIL = MAIL[:]

global miTimers
miTimers = TIMERS[:]

global Analogica
#Diccionario con los valores de cfg de la entra analógica
global miAnalogica
miAnalogica = {}
for i in Analogica.keys():
    miAnalogica[i] = Analogica[i]

global Modificado
# Variable que indica que el programa ha sido modificado
Modificado = False

global NombreArchivo
# Variable con el nombre del programa actual.
NombreArchivo = ""

#Tipos de archivo que muestran los diálos abrir/guardar
wildcard = "Archivo Programa Cyloc (*.cyl)|*.cyl|"\
           "Todos los archivos (*.*)|*.*"
           
wildcardbin = "Archivo Binario Cyloc (*.cb)|*.cb|"\
           "Todos los archivos (*.*)|*.*"            

binwildcard = "Archivo binario Cyloc (*.cb)|*.cb|"\
            "Todos los archivos (*.*)|*.*"


class MiFrame(gui.frmPpal):
    """Frame principal"""
    def __init__(self):
        super(MiFrame,self).__init__(None)
        self.aplicaciones = []
        # Lista con las aplicaciones actuales
        self.AppMenuItems = {}
        # Diccionario con referencia a los item del menú Aplicaciones
        
        self.numtimers = 0
        
        for i in range(Cantidad_Apps):
            self.aplicaciones.append(Aplicacion(i,""))
            # Crea aplicaciones vacías
            item = wx.MenuItem(self.m_aplicaciones, wx.ID_ANY, \
                u"Aplicación %0.2d: %s"%(i,self.aplicaciones[i].Nombre) ,\
                wx.EmptyString, wx.ITEM_NORMAL )
            self.m_aplicaciones.AppendItem(item)
            self.AppMenuItems[i] = item
            # Agrega el item al diccionario para la aplicación i
            self.Bind ( wx.EVT_MENU, self.OnAbrirApp, id = item.GetId() )
            item.Enable ( True )
            
            #boton = wx.Button(self.scroolled, wx.ID_ANY,\
            #    u"Aplicación: %0.2d"%i, wx.DefaultPosition, wx.DefaultSize, 0 )
            #self.sizerbotones.Add( boton, 0, wx.ALL, 5 )
            #boton.Bind(wx.EVT_BUTTON, self.OnImprimirApp)
        item = wx.MenuItem(self.m_aplicaciones, wx.ID_ANY, u"Copiar Aplicación",\
            wx.EmptyString, wx.ITEM_NORMAL )
        self.m_aplicaciones.AppendItem(item)
        self.Bind ( wx.EVT_MENU, self.OnCopiarApp, id = item.GetId() )


        self.sizerbotones.Fit(self.scroolled )
        for i in Entradas:
            item = wx.MenuItem(self.m_drivers, wx.ID_ANY, i,\
                wx.EmptyString, wx.ITEM_NORMAL )
            self.m_drivers.AppendItem( item )
            self.Bind ( wx.EVT_MENU, self.OnDriver, id = item.GetId() )
        item = wx.MenuItem (self.m_drivers , wx.ID_ANY, u"Cargar desde archivo...",\
            wx.EmptyString, wx.ITEM_NORMAL )
        self.m_drivers.AppendItem ( item )
        self.Bind (wx.EVT_MENU, self.OnCopiarDesde, id = item.GetId()) 
        

    def AgregarVentana(self):
        pass

    #funciones de eventos en frame principal

    def OnCerrar(self, event):
        global Modificado
        global NombreArchivo
        self.cancel = False
        if Modificado:

            if NombreArchivo == "":

                dlg = wx.MessageDialog(self, u"Guardar Programa?",\
                    caption=u"Cerrar Programa Actual",
                    style=wx.YES | wx.NO |wx.CANCEL,
                    pos=wx.DefaultPosition)
            else:

                dlg = wx.MessageDialog(self, u"Guardar Cambios?",\
                    caption=u"Cerrar Programa Actual",
                    style=wx.YES | wx.NO | wx.CANCEL,
                    pos=wx.DefaultPosition)

            val = dlg.ShowModal()
            dlg.Destroy()
            
            if val == wx.ID_YES:
            
                self.Guardar()
            
            elif val == wx.ID_NO:
            
                self.Destroy()
                
            elif val == wx.ID_CANCEL:
                
                return
        
        self.Destroy()
        event.Skip()

    def OnEditarBytes(self, event):
        id_ = event.GetId()
        item = self.GetMenuBar().FindItemById(id_)
        item.Enable(False)
        win = mifrmEditByte(self,item)
        win.Show()


    def OnEditarBit(self, event):
        bitid = event.GetId()
        item = self.GetMenuBar().FindItemById(bitid)
        item.Enable(False)
        win = mifrmEditBit(self, item)
        win.Show()
        
    def OnEditarSMS(self, event):
        smsid = event.GetId()
        item = self.GetMenuBar().FindItemById(smsid)
        item.Enable(False)
        win = mifrmSMS(self, item)
        win.Show()
        
    def OnEditarIp(self, event):
        ipsid = event.GetId()
        item = self.GetMenuBar().FindItemById(ipsid)
        item.Enable(False)
        win = mifrmIPs(self, item)
        win.Show()
        
    def OnEditarTEL(self, event):
        telid = event.GetId()
        item = self.GetMenuBar().FindItemById(telid)
        item.Enable(False)
        win = mifrmTEL(self, item)
        win.Show()
    
    def OnEditarMAIL(self, event):
        mailid = event.GetId()
        item = self.GetMenuBar().FindItemById(mailid)
        item.Enable(False)
        win = mifrmMAIL(self, item)
        win.Show()


    def OnDriverAnalog(self, event):
        driverid = event.GetId()
        item = self.GetMenuBar().FindItemById(driverid)
        item.Enable(False)
        win = mifrmAnalog(self)
        win.Show()


    def OnDriver(self, event):
        driverid = event.GetId()
        item = self.GetMenuBar().FindItemById(driverid)
        win = mifrmEntrada(self,item)
        item.Enable(False)
        win.Show()


    def OnAbrirApp(self, event):

        appid = event.GetId()
        item = self.GetMenuBar().FindItemById(appid)
        for i in self.aplicaciones:
            if u"Aplicación %0.2d: %s"%(i.AppNum,i.Nombre) ==item.GetText():
                win = mifrmEditApp(self,i)
                win.Show(True)
                item.Enable(False)
                return

    def OnNuevoTimer(self,event):
        i = self.numtimers + 1
        win = mifrmNuevoTimer(self,i)
        win.Show()
 
        
        

    #def OnImprimirApp(self, event):

     #   boton = event.GetEventObject()
      #  numero = int(boton.GetLabel()[-2:])
       # print u"\n\naplicación %d: %s"% (self.aplicaciones[numero].AppNum\
        #    ,self.aplicaciones[numero].Nombre)
#        for i in range(Cantidad_Estados):
 #           print str(self.aplicaciones[numero].Estados[i].Nombre)
  #          for j in range(Cantidad_Bloques):
   #             print str(hex(self.aplicaciones[numero].Estados[i].Bloques[j]))
    #        print ""

    def OnCopiarApp(self, event):

        dlg = miDlgCopiarApp(self)
        dlg.ShowModal()

    def OnCopiarDesde(self, event):
        global DIRACTUAL
        dlg = wx.FileDialog(
            self, message="Copiar Desde ...", defaultDir=DIRACTUAL,
            defaultFile="", wildcard=wildcard, style=wx.OPEN)

        dlg.SetFilterIndex(2)

        if dlg.ShowModal() == wx.ID_OK:

            path = dlg.GetPath()
            try:
                shelf = shelve.open(path)
            except:
                dlg = wx.MessageDialog(self, u"No es un archivo válido",\
                    caption="Error al abrir archivo",\
                    pos=wx.DefaultPosition)
                dlg.ShowModal()
                dlg.Destroy()
                return
            global miBytes
            try:
                miBytes = shelf["bytes"] 
            except:
                print "El archivo no tiene valores de entradas"
                pass
            global miAnalogica
            try:
                miAnalogica = shelf["miAnalogica"]
            except:
                print "El archivo no tiene cfg analógica"
                pass
            shelf.close()
        dlg.Destroy()


    def OnNuevoPrograma (self, event):

        global Modificado
        global NombreArchivo
        self.cancel = False
        if Modificado:

            if NombreArchivo == "":

                dlg = wx.MessageDialog(self, u"Guardar Programa?",\
                    caption=u"Cerrar Programa Actual",
                    style=wx.YES | wx.NO |wx.CANCEL,
                    pos=wx.DefaultPosition)
            else:

                dlg = wx.MessageDialog(self, u"Guardar Cambios?",\
                    caption=u"Cerrar Programa Actual",
                    style=wx.YES | wx.NO | wx.CANCEL,
                    pos=wx.DefaultPosition)

            val = dlg.ShowModal()
            dlg.Destroy()

            if val == wx.ID_YES:
                self.Guardar()

                if self.Boton == wx.ID_CANCEL:
                    return
                   
                self.CrearNuevoPrograma()
                
            elif val == wx.ID_NO:
                
                self.CrearNuevoPrograma()
        else:
            
            self.CrearNuevoPrograma()

    def OnAbrirPrograma(self, event):
        """Abre un programa .cyl y lo carga en el espacio de trabajo actual"""
        
        global DIRACTUAL
        global NombreArchivo
        self.OnNuevoPrograma(event)

        if self.cancel:
            pass

        dlg = wx.FileDialog(
            self, message="Abrir archivo ...", defaultDir=DIRACTUAL,
            defaultFile="", wildcard=wildcard, style=wx.OPEN
            )

        dlg.SetFilterIndex(2)

        if dlg.ShowModal() == wx.ID_OK:

            path = dlg.GetPath()
            NombreArchivo = path
            shelf = shelve.open(NombreArchivo)
            try:
                self.aplicaciones = shelf["programa"]
                global miBits
                miBits = shelf["bits"]
                
                global miBytes
                miBytes = shelf["bytes"]
                    
                global miAnalogica
                miAnalogica = shelf["miAnalogica"]

                global miSMS
                miSMS = shelf["SMS"]

                global miTEL
                miTEL = shelf["TEL"]

                global miSERVERS
                miSERVERS = shelf["SERVERS"]

                global miMAIL
                miMAIL = shelf["MAIL"]

            except:
                print "Error abriendo archivo"
                pass

            shelf.close()
            self.Title = "Generador de programas: " + NombreArchivo.split(os.sep)[-1]
            for i in range(Cantidad_Apps):
                self.AppMenuItems[i].SetText(\
                    u"Aplicación %0.2d: %s"%(i,self.aplicaciones[i].Nombre))

            dlg.Destroy()

    def OnGuardarPrograma(self, event):
        global NombreArchivo
        self.Guardar()
        self.Title = "Generador de Programas: " + NombreArchivo.split(os.sep)[-1]

    def OnGuardarComo(self, event):
        global Modificado
        global NombreArchivo
        self.archivoActual = NombreArchivo[:]
        NombreArchivo = ""
        Modificado = True
        self.Guardar()
        print NombreArchivo
        if self.Boton == wx.ID_OK:
            self.Title = "Generador de Programas: " + NombreArchivo.split(os.sep)[-1]
        else:
            NombreArchivo = self.archivoActual[:]

    def OnGenerar(self, event):
        """Genera un archivo de configuración binario con todos los datos, 
            debe colocarse en la tarjeta sd"""
        global DIRACTUAL
        dlg = wx.FileDialog(
            self, message="Generar en...", defaultDir=DIRACTUAL,
            defaultFile="", wildcard=binwildcard, style=wx.SAVE|wx.FD_OVERWRITE_PROMPT)
        dlg.SetFilterIndex(2)
        val = dlg.ShowModal()

        if val == wx.ID_OK:

            path = dlg.GetPath()
            if path[-2:] != "cb":
                path = path + ".cb"

            archivobinario = open(path,'wb')
            binario = GenerarBin(self.aplicaciones)
            
            for i in range(Cantidad_Bytes_Usuario):
                if miBytes[i][const.Valor] != "-1":
                    #Si el valor del byte se deja en -1, no se modifica
                    binario = binario + str(chr(0xAA)) + str(chr(HEADER_BYTE)) + \
                        str(chr(2)) + str(chr(i)) + str(chr(int(miBytes[i][const.Valor])))
                
            for i in range(Cantidad_Bits_Usuario):
                if miBits[i][const.Valor] != "-1":
                    #Si el valor del bit se deja en -1, no se modifica
                    binario = binario + str(chr(0xAA)) + str(chr(HEADER_BIT)) + \
                        str(chr(2)) + str(chr(i)) + str(chr(int(miBits[i][const.Valor])))
            
            #Agregar Sms al binario:
            # 0xAA, HEADER_SMS, SIZE, NºSMS, SMS
            #Solo Agrega SMS que no estén vacíos
            for i in range(Cantidad_SMS):
                if miSMS[i] != "":
                    binario +=  str(chr(0xAA)) + str(chr(HEADER_SMS))
                    nextstring = ""
                    nextstring += str(chr(i)) + str(miSMS[i].encode('latin1','ignore'))
                    binario += chr(len(nextstring)) + nextstring                
            
            #Agregar Ips al binario:
            # 0xAA, HEADER_IP, SIZE, NºIP,IP
            # o 0xAA, HEADER_WWW, SIZE, NºSERVERS, SERVERS
            #Solo Agrega IPs que no estén vacías
            for i in range(Cantidad_WEBs):
                
                if miSERVERS[i][0]:
                    cadena = miSERVERS[i][1].encode('latin1','ignore').strip()
                    if cadena != "":
                        binario +=  str(chr(0xAA)) + str(chr(HEADER_WWW))
                        nextstring = ""
                        nextstring += str(chr(i)) + cadena
                        cadena = ""
                        binario += chr(len(nextstring)) + nextstring
                    
                else: 
                    binario +=  str(chr(0xAA)) + str(chr(HEADER_IP))
                    nextstring = ""
                    cadena = ""
                    for j in map(chr,map(int,miSERVERS[i][1].split('.'))):
                        cadena += str(j) 
                    nextstring += str(chr(i)) + cadena
                    binario += chr(len(nextstring)) + nextstring
                                
            #Agregar direcciones Mail al binario:
            # 0xAA, HEADER_MAIL, SIZE, NºMAIL, direccionMail
            #Solo Agrega Mails que no estén vacíos
            for i in range(Cantidad_MAIL):
                if miMAIL[i] != "":
                    binario +=  str(chr(0xAA)) + str(chr(HEADER_MAIL))
                    cadena = str(miMAIL[i].encode('latin1','ignore'))
                    nextstring = str(chr(i)) + cadena.strip()
                    binario += chr(len(nextstring)) + nextstring
            
            #Agregar números de teléfono al binario:
            # 0xAA, HEADER_TEL, SIZE, NºTEL,
            #Solo Agrega teléfonos que no estén vacíos
            for i in range(Cantidad_TEL):
                if miTEL[i] != "":
                    binario +=  str(chr(0xAA)) + str(chr(HEADER_TEL))
                    nextstring = str(chr(i)) + miTEL[i].strip().encode('latin1','ignore')
                    binario += chr(len(nextstring)) + nextstring
                                                           
            binario +=  str(chr(0xAA)) + str(chr(HEADER_END)) + chr(0)           
            
            archivobinario.write(binario)
            archivobinario.flush()
            archivobinario.close()
            
        elif val == wx.ID_NO:
            
            self.Boton = wx.ID_NO

        else:

            self.Boton = wx.ID_CANCEL

    def Guardar(self):
        #TODO generar archivo como el anterior
        #TODO ver por que no guarda sms con acentos.
        global NombreArchivo
        global Modificado
        global DIRACTUAL
        self.Boton = None
        if Modificado:
            if NombreArchivo == "":
                dlg = wx.FileDialog(
                    self, message="Salvar archivo a ...", defaultDir=DIRACTUAL,
                    defaultFile="", wildcard=wildcard, style=wx.SAVE|wx.FD_OVERWRITE_PROMPT)
                dlg.SetFilterIndex(2)
                val = dlg.ShowModal()
                if val == wx.ID_OK:

                    path = dlg.GetPath()

                    if path[-3:] != "cyl":

                        path = path + ".cyl"

                    NombreArchivo = path
                    shelf = shelve.open(NombreArchivo)
                    shelf["programa"] = self.aplicaciones
                    
                    global miSMS
                    shelf["SMS"] = miSMS
                    
                    global miBits
                    shelf["bits"] = miBits
                    
                    global miBytes
                    shelf["bytes"] = miBytes
  
                    global miTEL
                    shelf["TEL"] = miTEL
                    
                    global miSERVERS
                    shelf["SERVERS"] = miSERVERS
                    
                    global miMAIL
                    shelf["MAIL"] = miMAIL
                    
                    global miAnalogica
                    shelf["miAnalogica"] = miAnalogica
                    
                    shelf["version"] = const.VERSION
                    shelf.close()
                    Modificado = False
                    dlg.Destroy()
                    self.Boton = wx.ID_OK

                elif val == wx.ID_NO:
                    self.Boton = wx.ID_NO

                else:
                    self.Boton = wx.ID_CANCEL

            else:

                shelf = shelve.open(NombreArchivo)
                shelf["programa"] = self.aplicaciones
                shelf.close()


    def CrearNuevoPrograma(self, aplicaciones = False,\
                            BitsVal = False, BytesVal = False, SMSVal = False,\
                            MailsVal=False,TelVal=False, ServersVal=False):
        global Modificado
        Modificado = False
        global NombreArchivo
        NombreArchivo = ""
        self.aplicaciones = []
        if aplicaciones == False:
            for i in range(Cantidad_Apps):
                self.aplicaciones.append(Aplicacion(i,""))
        else:
            for i in range(Cantidad_Apps):
                self.aplicaciones.append(aplicaciones[i].copy())
        for i in range(Cantidad_Apps):
            self.AppMenuItems[i].SetText(\
                u"Aplicación %0.2d: %s"%(i,self.aplicaciones[i].Nombre))
        
        self.Title = "Generador de Programas: "
        global ValoresEntradas
        
        
        global Analogica
        
        global miAnalogica
        miAnalogica = {}
        for i in Analogica.keys():
            miAnalogica[i] = Analogica[i]
        
        if BitsVal == False:            
            global miBits
            miBits = Bits[:]
        else:            
            miBits = BitsVal[:]
        
        if BytesVal == False:            
            global miBytes
            miBytes = Bytes[:]
        else:
            miBytes = BytesVal[:]
        
        if SMSVal == False:
            global miSMS
            miSMS = SMS[:]        
        else:
            miSMS = SMSVal[:]
            
        if MailsVal == False:
            global miMAIL
            miMAIL = MAIL[:]
        else:
            miMAIL = MailsVal[:]
            
        if TelVal == False:
            global miTEL
            miTEL = TEL[:]
        else:
            miTEL = TelVal[:]

        if ServersVal == False:
            global miSERVERS
            miSERVERS = SERVERS[:]
        else:
            miSERVERS = ServersVal[:]
            
    
    def OnImportarDesdeBin(self, event):
        """Importar datos desde un archivo binario"""
        self.OnNuevoPrograma(event)
        if self.cancel:
            pass
        
        dlg = wx.FileDialog(
            self, message="Abrir archivo ...", defaultDir=DIRACTUAL,
            defaultFile="", wildcard=wildcardbin, style=wx.OPEN
            )
        
        dlg.SetFilterIndex(2)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            import bin2gen
            NuevoPrograma = bin2gen.CargarBinario(path)
            if NuevoPrograma.CargarArchivo():
                self.CrearNuevoPrograma(NuevoPrograma.aplicaciones,\
                                        NuevoPrograma.binBIT,\
                                        NuevoPrograma.binBYTE,\
                                        NuevoPrograma.SMS,
                                        NuevoPrograma.mails,\
                                        NuevoPrograma.telefono,\
                                        NuevoPrograma.servers)
        dlg.Destroy()
        
        
########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Editar Apps   #######################
##############                                   #######################
########################################################################
########################################################################


class mifrmEditApp(gui.frmEditApp):

    """Frame para editar una app, recibe la app a editar"""

    def __init__(self, parent,App):

        super(mifrmEditApp,self).__init__(parent)
        self.padre = parent
        self.tempApp = App.copy()
        # Crea una copia de la app actual
        # Para no sobreescribir los datos originales en caso de cancelar
        self.textoPrograma.SetLabel("Programa %d: "%self.tempApp.AppNum+self.tempApp.Nombre)
        #self.SCTotal = []   # lista con el texto total de seudo código.
        self.Title = self.tempApp.Nombre
        self.EstadosDic = {}
        self.Cambios = False
        self.CargarLista()
        self.choiceEstadoInicial.SetItems(Estados)
        self.choiceEstadoInicial.SetSelection(self.tempApp.EstadoActual)
        #cargar los estados en un diccionario

    #diccionario de lista de estados {0:{"nombre":nombre,"opened":False/True}}

    def OnChoiceEstadoInicial(self, event):
        self.tempApp.EstadoActual = self.choiceEstadoInicial.GetSelection()


    def CargarLista(self):
        self.listEstados.Clear()
        for i in range(Cantidad_Estados):
            self.EstadosDic[i] = self.tempApp.Estados[i].copy()
            self.EstadosDic[i].opened = False
            self.EstadosDic[i].ventana = None
            titulo = self.EstadosDic[i].Nombre
            titulo = "%0.2d"%i + " : " + titulo
            self.listEstados.Append(titulo)

    def OnEditarEstado(self, event):
        self.Cambios = True
        sel = self.listEstados.GetSelection()
        if sel != -1:
            text = self.listEstados.GetString(sel)
            if self.EstadosDic [ int(text[0:2])].opened == False:
                self.EstadosDic [ int(text[0:2])].opened = True
                win = mifrmBloques(self,int(text[0:2]))
                self.EstadosDic[int(text[0:2])].ventana = win
                win.Show()
            else:
                #Poner el foco en la ventana de edición
                self.EstadosDic[int(text[0:2])].ventana.SetFocus()

    def OnDuplicarEstado(self, event):
        dlg = miDlgCopiarEstado(self)
        dlg.ShowModal()


    def OnEliminarEstado(self, event):

        sel = self.listEstados.GetSelection()
        if sel != -1:
            self.Cambios = False
            self.tempApp.Estados[sel] = Estado()
            self.EstadosDic[sel].opened = False
            self.listEstados.Delete(sel)
            self.listEstados.Insert( "%0.2d :"%sel, sel )


    def OnEliminarApp(self, event):

        dlg = wx.MessageDialog(self, u"Desea borrar la\nAplicación actual?",\
            caption="Borrar Aplicación",\
            style=wx.YES | wx.NO,\
            pos=wx.DefaultPosition)
        val = dlg.ShowModal()
        if val == wx.ID_YES:
            num = self.tempApp.AppNum
            self.tempApp = Aplicacion(num,"")
            self.padre.aplicaciones[num] = self.tempApp
            print u"Eliminada App: %d: %s"%\
                (self.tempApp.AppNum,self.tempApp.Nombre)
            self.padre.AppMenuItems[self.tempApp.AppNum].SetText(\
                u"Aplicación %0.2d: %s"%(self.tempApp.AppNum,self.tempApp.Nombre))
            self.padre.AppMenuItems[num].Enable()
            self.Destroy()


    def OnGuardarApp(self, event):
        self.Guardar()

    def OnCambiarNombre(self, event):
        self.Cambios = True
        text = self.tempApp.Nombre
        renamed = wx.GetTextFromUser(u"Renombrar Aplicación", "Renombrar", text)
        if renamed != '':
            self.tempApp.Nombre = renamed
            #item = self.AppMenuItems[self.tempApp.AppNum]
            self.textoPrograma.SetLabel(u"Aplicación %d: "%self.tempApp.AppNum+renamed)

    def OnClose(self,event):
        if self.Cambios:
            dlg = wx.MessageDialog(self, u"Guardar Aplicación?",\
            caption=u"Cerrar Edición de Aplicación",
            style=wx.YES | wx.NO,
            pos=wx.DefaultPosition)
            val = dlg.ShowModal()
            if val == wx.ID_YES:
                self.Guardar()
        self.padre.AppMenuItems[self.tempApp.AppNum].Enable(True)
        self.Destroy()

    def Guardar(self):
        self.padre.aplicaciones[self.tempApp.AppNum] = self.tempApp.copy()
        self.padre.AppMenuItems[self.tempApp.AppNum].SetText(\
            u"Aplicación %0.2d: %s"%(self.tempApp.AppNum,self.tempApp.Nombre))
        self.Cambios = False
        global Modificado
        Modificado = True


########################################################################
########################################################################
################                                   #####################
################     Edición del Frame Bloques     #####################
################                                   #####################
########################################################################
########################################################################

class mifrmBloques( gui.frmBloques):

    def __init__(self, parent, numEstado):

        gui.frmBloques.__init__ (self, parent)
        self.padre = parent
        self.notBloque.NumEstado = numEstado
        self.notBloque.Estado = self.padre.tempApp.Estados[numEstado].copy()
        self.notBloque.SCTotal = []
        self.Title = "Sin Nombre"
        self.notBloque.Modificado = False
        for i in range(Cantidad_Bloques):
            self.notBloque.SCTotal.append("")
            win = mipanelBloque(self.notBloque, i , self.padre )
            self.notBloque.AddPage(win,"Bloque: %d"%i)
        self.notBloque.SCTotal.append("")

        # la lista SCTotal tiene en total Cantidad_Bloques + 1 elementos.
        win = mipanelCondicion(self.notBloque,Cantidad_Bloques,self.padre)
        self.notBloque.AddPage(win,"Condicion")
        #Cargar el valor actual de el nombre del estado
        self.txtctrlTitulo.SetValue(\
            self.notBloque.Estado.Nombre)
        self.txtctrlComentario.SetValue(\
            self.notBloque.Estado.Comentario)


    def OnGuardar(self, event):
        self.Guardar()


    def Guardar(self):

        #self.padre.tempApp.Estados[self.notBloque.estado] = \
        #    self.padre.tempApp.Estados[self.notBloque.estado].copy()
        #nombre del estado
        self.padre.tempApp.Estados[self.notBloque.NumEstado] =\
            self.notBloque.Estado.copy()
        nombre = "%0.2d"%self.notBloque.NumEstado + " : " + self.Title
        self.padre.EstadosDic[self.notBloque.NumEstado].opened = True
        self.padre.listEstados.Delete(self.notBloque.NumEstado)
        self.padre.listEstados.Insert(nombre, self.notBloque.NumEstado)
        self.padre.EstadosDic[self.notBloque.NumEstado].Nombre = self.Title
        self.padre.EstadosDic[self.notBloque.NumEstado].opened = True
        self.notBloque.Modificado = False
        global Modificado
        Modificado = True
        self.comentario = self.txtctrlComentario.GetValue()
        self.padre.tempApp.Estados[self.notBloque.NumEstado].Comentario = self.comentario


    def OnClose (self, event):
        """Quita la ventana actual de la lista de ventanas abiertas"""

        if self.notBloque.Modificado == True:
            dlg = wx.MessageDialog(self, u"Guardar Estado?",\
            caption=u"Cerrar Edición Estado",
            style=wx.YES | wx.NO,
            pos=wx.DefaultPosition)
            val = dlg.ShowModal()
            if val == wx.ID_YES:
                self.Guardar()
        self.padre.EstadosDic[self.notBloque.NumEstado].opened = False
        self.padre.EstadosDic[self.notBloque.NumEstado].ventana = None
        self.Destroy()


    def OnTitulo(self, event):
        self.notBloque.Modificado = True
        self.Title = self.txtctrlTitulo.GetValue()
        self.notBloque.Estado.Nombre = self.Title

########################################################################
########################################################################
##############                                   #######################
##############       Edición del Panel Bloque    #######################
##############                                   #######################
########################################################################
########################################################################

class mipanelBloque(gui.panelBloque):

    def __init__(self, parent,numero,frmEditApp):

        gui.panelBloque.__init__(self,parent)
        self.numero = numero
        self.padre  = parent
        self.frmEditApp = frmEditApp
        self.ValorBloque = frmEditApp.tempApp.Estados[self.padre.NumEstado].Bloques[numero]
        self.Tipo = (self.ValorBloque & 0xff000000)>>24
        self.Guardar = (self.ValorBloque & 0x00ff0000)>>16
        self.Par2 = (self.ValorBloque & 0x0000ff00)>>8
        self.Par1 = (self.ValorBloque & 0x000000ff)

        self.GeneradoresCodigo = {
                        "Null"          :  self.SCNull,
                        "Incrementar"   :  self.SCIncrementar,
                        "Decrementar"   :  self.SCDecrementar,
                        "AND_2_BIT"     :  self.SCAND,
                        "OR_2_BIT"      :  self.SCOR,
                        "NOT_BIT"       :  self.SCNOT,
                        "Sumar_2_Reg"   :  self.SCSumar,
                        "Restar_2_Reg"  :  self.SCRestar,
                        "Invertir_Reg"  :  self.SCInvertir,
                        "Transmitir_BB" :  self.SCTransmitir,
                        "SetBit"        :  self.SCSetBit,
                        "ClrBit"        :  self.SCClrBit,
                        "ClrReg"        :  self.SCClrReg,
                        "CopiarRegistro":  self.SCCopiar
                        }

        #Carga los bloques posibles en la selección
        self.choiceAccion.SetItems(BloquesPosibles)
        #Seteo el valor actual elegido para este bloque
        self.choiceAccion.SetSelection(self.Tipo)

        self.Acciones = {
                        "Null"          :  self.BloqueNull,
                        "Incrementar"   :  self.BloqueIncrementar,
                        "Decrementar"   :  self.BloqueDecrementar,
                        "AND_2_BIT"     :  self.BloqueAND,
                        "OR_2_BIT"      :  self.BloqueOR,
                        "NOT_BIT"       :  self.BloqueNOT,
                        "Sumar_2_Reg"   :  self.BloqueSumar,
                        "Restar_2_Reg"  :  self.BloqueRestar,
                        "Invertir_Reg"  :  self.BloqueInvertir,
                        "Transmitir_BB" :  self.BloqueTransmitir,
                        "SetBit"        :  self.BloqueSetBit,
                        "ClrBit"        :  self.BloqueClrBit,
                        "ClrReg"        :  self.BloqueClrReg,
                        "CopiarRegistro":  self.BloqueCopiar
                        }

        #Ejecuto la acción predeterminada para este bloque
        self.Acciones[BloquesDic[self.Tipo]]()
        self.ActualizarSeudoCodigo()
        self.padre.Modificado = False

    def ActualizarSeudoCodigo(self):
        self.padre.SCTotal[self.numero] = \
            self.GeneradoresCodigo[GetTexto(self.choiceAccion)]()
        self.padre.Modificado = True
        #CARGA EL VALOR DEL BLOQUE
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque


    def OnChoiceAccion(self, event):
        self.padre.Modificado = True
        self.txtctrlSeudo.SetValue("")
        self.Acciones.get(event.GetString())()


    def OnChoice(self, event):
        self.ActualizarSeudoCodigo()


    def BloqueNull(self):
        self.choiceParametro1.Enable(False)
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(False)
        self.ActualizarSeudoCodigo()


    def BloqueIncrementar(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceGuardar.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection(self.Guardar )


    def BloqueDecrementar(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceGuardar.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection(self.Guardar )


    def BloqueAND(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBits])
        self.choiceParametro2.SetItems([i[const.Nombre] for i in miBits])
        self.choiceGuardar.SetItems([i[const.Nombre] for i in miBits])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(True)
        self.choiceParametro2.SetSelection(self.Par2 )
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection(self.Guardar )


    def BloqueOR(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBits])
        self.choiceParametro2.SetItems([i[const.Nombre] for i in miBits])
        self.choiceGuardar.SetItems([i[const.Nombre] for i in miBits])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(True)
        self.choiceParametro2.SetSelection(self.Par2 )
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection(self.Guardar )


    def BloqueNOT(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBits])
        self.choiceGuardar.SetItems([i[const.Nombre] for i in miBits])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection(self.Guardar )


    def BloqueSumar(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceGuardar.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(True)
        self.choiceParametro2.SetSelection(self.Par2 )
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection(self.Guardar )


    def BloqueRestar(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceGuardar.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(True)
        self.choiceParametro2.SetSelection(self.Par2 )
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection(self.Guardar )


    def BloqueInvertir(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        #self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceGuardar.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection(self.Guardar )


    def BloqueTransmitir(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceGuardar.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(True)
        self.choiceParametro2.SetSelection(self.Par2 )
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection(self.Guardar )

    def BloqueSetBit(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBits])
        #self.choiceParametro2.SetItems([i[const.Nombre] for i in miBits])
        #self.choiceGuardar.SetItems([i[const.Nombre] for i in miBits])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(False)


    def BloqueClrBit(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBits])
        #self.choiceParametro2.SetItems([i[const.Nombre] for i in miBits])
        #self.choiceGuardar.SetItems([i[const.Nombre] for i in miBits])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(False)


    def BloqueClrReg(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        #self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        #self.choiceGuardar.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(False)


    def BloqueCopiar(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        #self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceGuardar.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection(self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection(self.Guardar )


    def SCNull(self):
        """ Función encargada de generar el seudocódigo
        para la función Null
        """
        self.ValorBloque = Bloque_Null<<24
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return None


    def SCIncrementar(self):
        """ Función encargada de generar el seudocódigo
        para la función incrementar
        """
        cadena = GetTexto(self.choiceGuardar) + " = " +\
                GetTexto(self.choiceParametro1) + " + 1"
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_Incrementar<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection()))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena


    def SCDecrementar(self):
        """ Función encargada de generar el seudocódigo
            para la función decrementar
        """
        cadena = GetTexto(self.choiceGuardar) + " = " +\
            GetTexto(self.choiceParametro1) + " - 1"
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_Decrementar<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection()))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena


    def SCAND(self):
        """Función encargada de generar el seudocódigo
            para la función AND
        """
        cadena = GetTexto(self.choiceGuardar) + " = " +\
            GetTexto(self.choiceParametro1) + " & " +\
            GetTexto(self.choiceParametro2)
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_AND_2_BIT<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection())|\
            int(self.choiceParametro2.GetCurrentSelection()<<8))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena


    def SCOR(self):
        """Función encargada de generar el seudocódigo
            para la función OR
        """
        cadena = GetTexto(self.choiceGuardar) + " = " +\
            GetTexto(self.choiceParametro1) + " | " +\
            GetTexto(self.choiceParametro2)
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_OR_2_BIT<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection())|\
            int(self.choiceParametro2.GetCurrentSelection()<<8))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena


    def SCNOT(self):
        """Función encargada de generar el seudocódigo
        para la función NOT
        """
        cadena = GetTexto(self.choiceGuardar) + " = NOT(" +\
            GetTexto(self.choiceParametro1) + ")"
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_NOT_BIT<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection()))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena


    def SCSumar(self):
        """Función encargada de generar el seudocódigo
        para la función sumar
        """
        cadena = GetTexto(self.choiceGuardar) + " = " +\
            GetTexto(self.choiceParametro1) + " + " +\
            GetTexto(self.choiceParametro2)
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_Sumar_2_Reg<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection())|\
            int(self.choiceParametro2.GetCurrentSelection()<<8))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena


    def SCRestar(self):
        """Función encargada de generar el seudocódigo
        para la función restar
        """
        cadena = GetTexto(self.choiceGuardar) + " = " +\
            GetTexto(self.choiceParametro1) + " - " +\
            GetTexto(self.choiceParametro2)
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_Restar_2_Reg<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection())|\
            int(self.choiceParametro2.GetCurrentSelection()<<8))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena


    def SCInvertir(self):
        """Función encargada de generar el seudocódigo
        para la función invertir
        """
        cadena = GetTexto(self.choiceGuardar) + " = ~(" +\
            GetTexto(self.choiceParametro1) + ")"
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_Invertir_Reg<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection()))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena

    def SCTransmitir(self):
        """Función encargada de generar el seudocódigo
        para la función transmitir
        """
        self.ValorBloque = ((Bloque_Transmitir_BB<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection())|\
            int(self.choiceParametro2.GetCurrentSelection()<<8))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return None


    def SCSetBit(self):
        """Función encargada de generar el seudocódigo
        para la función set bit
        """
        cadena = GetTexto(self.choiceParametro1) + " = 1"
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = 0
        self.ValorBloque = ((Bloque_SetBit<<24)|\
            int(self.choiceParametro1.GetCurrentSelection()))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque

        return cadena


    def SCClrBit(self):
        """Función encargada de generar el seudocódigo
        para la función clr bit
        """
        cadena = GetTexto(self.choiceParametro1) + " = 0"
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_ClrBit<<24)|\
            int(self.choiceParametro1.GetCurrentSelection()))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena


    def SCClrReg(self):
        """Función encargada de generar el seudocódigo
        para la función clr reg
        """
        cadena = GetTexto(self.choiceParametro1) + " = 0"
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_ClrReg<<24)|\
            int(self.choiceParametro1.GetCurrentSelection()))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena


    def SCCopiar(self):
        """Función encargada de generar el seudocódigo
        para la función copiar reg
        """
        cadena = GetTexto(self.choiceGuardar) + " = "+\
            GetTexto(self.choiceParametro1)
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_CopiarRegistro<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection()))
        self.padre.Estado.Bloques[self.numero] = self.ValorBloque
        return cadena

########################################################################
########################################################################
##############                                   #######################
##############       Edición del Panel Condición #######################
##############                                   #######################
########################################################################
########################################################################

class mipanelCondicion ( gui.panelCondicion ):
    def __init__(self, parent , numero , frmEditApp):
        """ parent: frm padre, numero = numero de estado ,
        frmEditApp = frm que posee la app actual"""
        gui.panelCondicion.__init__ (self, parent)
        self.numero = numero
        self.padre = parent
        self.frmEditApp = frmEditApp
        self.AppNum = frmEditApp.tempApp.AppNum

        self.choiceAccion.SetItems ( CondicionesPosibles )
        self.choiceParametro1.Enable ( False )
        self.choiceParametro2.Enable ( False )
        self.choiceEstadoTrue.Enable ( False )
        self.choiceEstadoFalse.Enable( False )
        self.ValorCondiciones = [Condicion_NULL,0,0]
        self.ValorResultados = [0,0]
        #self.SCTotal = self.padre.SCTotal
        #self.Condicion = frmEditApp.app.Estados[0].Condiciones
        self.Acciones = {
                        "NULL"      : self.BloqueNull,
                        "Mayor"     : self.Mayor,
                        "Menor"     : self.Menor,
                        "Igual"     : self.Igual,
                        "Bit_True"  : self.BitTrue,
                        "Bit_False" : self.BitFalse
                        }

        self.GeneradoresCodigo = {
                        "NULL"      : self.SCNull,
                        "Mayor"     : self.SCMayor,
                        "Menor"     : self.SCMenor,
                        "Igual"     : self.SCIgual,
                        "Bit_True"  : self.SCBitTrue,
                        "Bit_False" : self.SCBitFalse
                        }
        self.Acciones[CondicionesPosibles[\
            self.padre.Estado.Condiciones[0]]]()

        self.choiceAccion.SetSelection (\
            frmEditApp.tempApp.Estados[self.padre.NumEstado].Condiciones[0])
        self.choiceParametro1.SetSelection (\
            frmEditApp.tempApp.Estados[self.padre.NumEstado].Condiciones[1])
        self.choiceParametro2.SetSelection (\
            frmEditApp.tempApp.Estados[self.padre.NumEstado].Condiciones[2])
        self.choiceEstadoTrue.SetSelection (\
            frmEditApp.tempApp.Estados[self.padre.NumEstado].Resultados[0])
        self.choiceEstadoFalse.SetSelection (\
            frmEditApp.tempApp.Estados[self.padre.NumEstado].Resultados[1])

        self.padre.Modificado = False


    def SCNull(self):
        """ Función encargada de generar el seudocódigo
        para la condición NULL
        """
        cadena = ""
        self.ValorCondiciones = [Condicion_NULL,0,0]
        return cadena

    def SCMayor(self):
        """ Función encargada de generar el seudocódigo
        para la condición mayor
        """
        cadena = "if (" + GetTexto(self.choiceParametro1) + " > " +\
                GetTexto(self.choiceParametro2) + ")\n" +\
                "\t\tEstadoApp = " + GetTexto(self.choiceEstadoTrue)\
                + "\n\telse:\n\t\tEstadoApp = " + GetTexto(self.choiceEstadoFalse)
        self.ValorCondiciones[0] = Condicion_Mayor
        self.ValorCondiciones[1] = self.choiceParametro1.GetCurrentSelection()
        self.ValorCondiciones[2] = self.choiceParametro2.GetCurrentSelection()
        self.ValorResultados[0] = self.choiceEstadoTrue.GetCurrentSelection()
        self.ValorResultados[1] = self.choiceEstadoFalse.GetCurrentSelection()
        self.padre.Estado.Condiciones = self.ValorCondiciones[:]
        self.padre.Estado.Resultados = self.ValorResultados[:]
        return cadena

    def SCMenor(self):
        """ Función encargada de generar el seudocódigo
        para la condicion menor
        """
        cadena = "if (" + GetTexto(self.choiceParametro1) + " < " +\
                GetTexto(self.choiceParametro2) + ")\n" +\
                "\t\tEstadoApp = " + GetTexto(self.choiceEstadoTrue)\
                + "\n\telse:\n\t\tEstadoApp = " + GetTexto(self.choiceEstadoFalse)
        self.ValorCondiciones[0] = Condicion_Menor
        self.ValorCondiciones[1] = self.choiceParametro1.GetCurrentSelection()
        self.ValorCondiciones[2] = self.choiceParametro2.GetCurrentSelection()
        self.ValorResultados[0] = self.choiceEstadoTrue.GetCurrentSelection()
        self.ValorResultados[1] = self.choiceEstadoFalse.GetCurrentSelection()
        self.padre.Estado.Condiciones = self.ValorCondiciones[:]
        self.padre.Estado.Resultados = self.ValorResultados[:]
        return cadena

    def SCIgual(self):
        """ Función encargada de generar el seudocódigo
        para la condición igual
        """
        cadena = "if (" + GetTexto(self.choiceParametro1) + " == " +\
                GetTexto(self.choiceParametro2) + ")\n" +\
                "\t\tEstadoApp = " + GetTexto(self.choiceEstadoTrue)\
                + "\n\telse:\n\t\tEstadoApp = " + GetTexto(self.choiceEstadoFalse)
        self.ValorCondiciones[0] = Condicion_Igual
        self.ValorCondiciones[1] = self.choiceParametro1.GetCurrentSelection()
        self.ValorCondiciones[2] = self.choiceParametro2.GetCurrentSelection()
        self.ValorResultados[0] = self.choiceEstadoTrue.GetCurrentSelection()
        self.ValorResultados[1] = self.choiceEstadoFalse.GetCurrentSelection()
        self.padre.Estado.Condiciones = self.ValorCondiciones[:]
        self.padre.Estado.Resultados = self.ValorResultados[:]
        return cadena

    def SCBitTrue(self):
        """ Función encargada de generar el seudocódigo
        para la condición bit true
        """
        cadena = "if (" + GetTexto(self.choiceParametro1) + \
                " == True)\n\t\tEstadoApp = " + GetTexto(self.choiceEstadoTrue)\
                + "\n\telse:\n\t\tEstadoApp = " + GetTexto(self.choiceEstadoFalse)
        self.ValorCondiciones[0] = Condicion_Bit_True
        self.ValorCondiciones[1] = self.choiceParametro1.GetCurrentSelection()
        self.ValorCondiciones[2] = 0
        self.ValorResultados[0] = self.choiceEstadoTrue.GetCurrentSelection()
        self.ValorResultados[1] = self.choiceEstadoFalse.GetCurrentSelection()
        self.padre.Estado.Condiciones = self.ValorCondiciones[:]
        self.padre.Estado.Resultados = self.ValorResultados[:]
        return cadena

    def SCBitFalse(self):
        """ Función encargada de generar el seudocódigo
        para la condición bit true
        """
        cadena = "if (" + GetTexto(self.choiceParametro1) + \
                " == False)\n\t\tEstadoApp = " + GetTexto(self.choiceEstadoTrue)\
                + "\n\telse:\n\t\tEstadoApp = " + GetTexto(self.choiceEstadoFalse)
        self.ValorCondiciones[0] = Condicion_Bit_False
        self.ValorCondiciones[1] = self.choiceParametro1.GetCurrentSelection()
        self.ValorCondiciones[2] = 0
        self.ValorResultados[0] = self.choiceEstadoTrue.GetCurrentSelection()
        self.ValorResultados[1] = self.choiceEstadoFalse.GetCurrentSelection()
        self.padre.Estado.Condiciones = self.ValorCondiciones[:]
        self.padre.Estado.Resultados = self.ValorResultados[:]
        return cadena

    def ActualizarSeudoCodigo(self):
        self.padre.SCTotal[self.numero] = self.GeneradoresCodigo[GetTexto(self.choiceAccion)]()
        self.padre.Modificado = True
        self.txtctrlSeudo.SetValue("")
        for i in range(len(self.padre.SCTotal)-1):
            if self.padre.SCTotal[i]:
                self.txtctrlSeudo.AppendText("Bloque "+str(i)+": \n\t"+ \
                    self.padre.SCTotal[i] + "\n\n")
        if self.padre.SCTotal[-1]:
            self.txtctrlSeudo.AppendText("Condicion: \n" +\
                self.padre.SCTotal[-1])


    def OnChoiceComparacion(self, event):
        self.Acciones.get(event.GetString())()
        self.ActualizarSeudoCodigo()

    def OnChoice(self, event):
        self.ActualizarSeudoCodigo()


    def OnEnterWindow(self, event):
        self.ActualizarSeudoCodigo()


    def BloqueNull(self):
        #Deshabilito todos los choices
        self.choiceParametro1.Enable(False)
        self.choiceParametro2.Enable(False)
        self.choiceEstadoTrue.Enable(False)
        self.choiceEstadoFalse.Enable(False)


    def Mayor(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.SetSelection(0)
        self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro2.SetSelection(0)
        self.choiceEstadoTrue.SetItems(miEstados)
        self.choiceEstadoTrue.SetSelection(0)
        self.choiceEstadoFalse.SetItems(miEstados)
        self.choiceEstadoFalse.SetSelection(0)
        #Habilito choices usables
        self.choiceParametro1.Enable(True)
        self.choiceParametro2.Enable(True)
        self.choiceEstadoTrue.Enable(True)
        self.choiceEstadoFalse.Enable(True)


    def Menor(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.SetSelection(0)
        self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro2.SetSelection(0)
        self.choiceEstadoTrue.SetItems(miEstados)
        self.choiceEstadoTrue.SetSelection(0)
        self.choiceEstadoFalse.SetItems(miEstados)
        self.choiceEstadoFalse.SetSelection(0)
        #Habilito choices usables
        self.choiceParametro1.Enable(True)
        self.choiceParametro2.Enable(True)
        self.choiceEstadoTrue.Enable(True)
        self.choiceEstadoFalse.Enable(True)

    def Igual(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro1.SetSelection(0)
        self.choiceParametro2.SetItems([i[const.Nombre] for i in miBytes])
        self.choiceParametro2.SetSelection(0)
        self.choiceEstadoTrue.SetItems(miEstados)
        self.choiceEstadoTrue.SetSelection(0)
        self.choiceEstadoFalse.SetItems(miEstados)
        self.choiceEstadoFalse.SetSelection(0)
        #Habilito choices usables
        self.choiceParametro1.Enable(True)
        self.choiceParametro2.Enable(True)
        self.choiceEstadoTrue.Enable(True)
        self.choiceEstadoFalse.Enable(True)

    def BitTrue(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBits])
        self.choiceParametro1.SetSelection(0)
        self.choiceEstadoTrue.SetItems(miEstados)
        self.choiceEstadoTrue.SetSelection(0)
        self.choiceEstadoFalse.SetItems(miEstados)
        self.choiceEstadoFalse.SetSelection(0)
        #Habilito choices usables
        self.choiceParametro1.Enable(True)
        self.choiceParametro2.Enable(False)
        self.choiceEstadoTrue.Enable(True)
        self.choiceEstadoFalse.Enable(True)

    def BitFalse(self):
        self.choiceParametro1.SetItems([i[const.Nombre] for i in miBits])
        self.choiceParametro1.SetSelection(0)
        self.choiceEstadoTrue.SetItems(miEstados)
        self.choiceEstadoTrue.SetSelection(0)
        self.choiceEstadoFalse.SetItems(miEstados)
        self.choiceEstadoFalse.SetSelection(0)
        #Habilito choices usables
        self.choiceParametro1.Enable(True)
        self.choiceParametro2.Enable(False)
        self.choiceEstadoTrue.Enable(True)
        self.choiceEstadoFalse.Enable(True)


# DIALOGO DE ENTRADAS
# Se usa el mismo dialogo para todas las entradas, cambiandole el nombre a cada una.

########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Entrada       #######################
##############                                   #######################
########################################################################
########################################################################

class  mifrmEntrada (gui.frmEntrada):

    """Diálogo para configurar entradas"""

    def __init__(self, parent , item):
        gui.frmEntrada.__init__ (self, parent )
        self.padre = parent
        self.item = item
        self.entrada = self.item.GetText()
        self.Title = self.Title + self.item.GetText()
        global miBytes
        for i,(a,b,c,d) in enumerate(miBytes):
            if a == EntradasBytes[self.entrada][0]:
                # self.muestras queda con el valor del numero de byte que 
                # corresponde a la entrada actual. (contacto, puerta, porton, etc) 
                self.muestras = i 
            if a == EntradasBytes[self.entrada][1]:
                # self.muestras queda con el valor del numero de byte que 
                # corresponde a la entrada actual. (contacto, puerta, porton, etc) 
                self.tiempo = i
        self.txtctrlMuestras.SetValue(str(miBytes[self.muestras][const.Valor]))
        self.txtctrlTiempo.SetValue(str(miBytes[self.tiempo][const.Valor]))


    def OnGuardar(self, event):
        miBytes[self.muestras][2] = self.txtctrlMuestras.GetValue()
        miBytes[self.tiempo][2]   = self.txtctrlTiempo.GetValue()
        global Modificado
        Modificado = True
       
        

    def OnCerrar(self, event):
        self.item.Enable(True)
        self.Destroy()

    def OnCargarDefaults(self, event):
        global miBytes
        miBytes[self.muestras][2] = MuestrasDefault
        miBytes[self.tiempo][2] = TiempoDefault
        self.txtctrlMuestras.SetValue(str(miBytes[self.muestras][2]))
        self.txtctrlTiempo.SetValue(str(miBytes[self.tiempo][2]))

    def OnChar(self, event):
        EsNumero ( event)



########################################################################
########################################################################
##############                                   #######################
##############   Edición del Diálogo Error       #######################
##############                                   #######################
########################################################################
########################################################################

class miDlgGenError (gui.DlgGenError):
    """Diálogo de error"""
    def __init__(self, parent ):
        gui.DlgGenError.__init__ (self, parent)

    def OnAceptar(self, event):
        self.Destroy()


########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Editar Bits   #######################
##############                                   #######################
########################################################################
########################################################################

class mifrmEditBit ( gui.frmEditBit ):
    """Frame para editar los nombres y valores de los bits"""    
    
    def __init__(self, parent, item):
        
        gui.frmEditBit.__init__ (self, parent)
        self.item = item
        global miBits
        self.modificado = False
        self.miBits = miBits[:]
        self.BitsTextCtrl = [] #lista con los wx.TextCtrl de edición de nombre de bit.
        self.BitsValues = [] #lista con los wx.SpinCtrl
        for i,valorBit in enumerate(self.miBits):

            texto  = wx.StaticText(self.BitScrolled, wx.ID_ANY, \
                u"Bit Nº: %d"%i, wx.DefaultPosition, wx.DefaultSize, 0 )
            texto.Wrap( -1 )
            self.gridBotones.Add( texto, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
            # En Windows no se puede hacer wx.TextCtrl readonly luego\
            # de creado, por lo que debe hacerce cuando se crea:

            if valorBit[const.mod] == 0:
                textCtrl = wx.TextCtrl(self.BitScrolled, wx.ID_ANY,\
                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,wx.TE_READONLY)
                spinValue =  wx.SpinCtrl(self.BitScrolled, wx.ID_ANY, \
                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,\
                    wx.SP_ARROW_KEYS, -1, 1,  int(self.miBits[i][const.Valor]) )
                if i<2:
                    #evita la edición de los bits true y false
                    spinValue.Enable(False) 
                                       
            else:
                textCtrl = wx.TextCtrl(self.BitScrolled, wx.ID_ANY, \
                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
                spinValue =  wx.SpinCtrl(self.BitScrolled, wx.ID_ANY, \
                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, \
                    wx.SP_ARROW_KEYS, -1, 1, int(self.miBits[i][const.Valor]))
                
            self.gridBotones.Add( textCtrl, 0, wx.ALL|wx.EXPAND, 5 )
            self.gridBotones.Add( spinValue, 0, wx.ALL, 5 )
            textCtrl.SetValue(valorBit[const.Nombre])
            textCtrl.Bind( wx.EVT_RIGHT_DOWN, self.OnBtnDerecho )
            spinValue.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl )
            self.BitsTextCtrl.append( textCtrl )
            self.BitsValues.append( spinValue ) 

        self.BitScrolled.SetSizer(self.gridBotones )
        self.BitScrolled.Layout()
        self.BitScrolled.SetAutoLayout(True)
        self.gridBotones.Fit(self.BitScrolled )
        
    def OnSpinCtrl (self, event):
        self.modificado = True
        event.Skip()        
    
    def OnBtnDerecho (self, event):
        txtctrl = event.GetEventObject()
        texto = self.miBits[self.BitsTextCtrl.index(txtctrl)][1]
        win = infoPopup(self, wx.SIMPLE_BORDER,texto)
        pos = txtctrl.ClientToScreen( (0,0) )
        sz =  txtctrl.GetSize()
        win.Position(pos, (0, sz[1]))
        win.Popup()
    
    def OnModificarTexto (self, event):
        event.Skip()

    def OnEditBit(self, event):
        """guarda los cambios realizados"""
        self.GuardarDatos()
            

    def GuardarDatos (self ):
        """guarda los cambios realizados"""
        global miBits
        for i,txtctrl in enumerate(self.BitsTextCtrl):
            if txtctrl.IsModified():
                self.miBits[i][const.Nombre] = txtctrl.GetValue()
                txtctrl.SetModified(False)
            self.miBits[i][const.Valor] = str(self.BitsValues[i].GetValue())
        miBits = self.miBits[:]
        self.modificado = False
        global Modificado
        Modificado = True


    def OnUndoBit(self, event):
        global miBits
        self.miBits = miBits[:]
        for i,txtctrl in enumerate(self.BitsTextCtrl):
            txtctrl.SetValue(self.miBits[i][const.Nombre])


    def OnClose(self, event):
        if self.modificado == False:
            for i in range(Cantidad_Bits_Usuario):
                if self.BitsTextCtrl[i].IsModified():
                    self.modificado = True
                    break
        if self.modificado:
            dlg = wx.MessageDialog(self, u"Guardar cambios?",\
            caption=u"Cerrar Edición Bits",
            style=wx.YES | wx.NO,
            pos=wx.DefaultPosition)
            val = dlg.ShowModal()
            if val == wx.ID_YES:
                self.GuardarDatos()
        self.item.Enable(True)
        event.Skip()


class infoPopup(wx.PopupTransientWindow):
    """Adds a bit of text and mouse movement to the wx.PopupWindow"""
    def __init__(self, parent, style,text):
        wx.PopupTransientWindow.__init__(self, parent, style)
        self.SetBackgroundColour("#FFB6C1")
        st = wx.StaticText(self, -1,text,
                          pos=(10,10))
        sz = st.GetBestSize()
        self.SetSize( (sz.width+20, sz.height+20) )

    def ProcessLeftDown(self, evt):
        return False

    def OnDismiss(self):
        pass



########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Editar Bytes  #######################
##############                                   #######################
########################################################################
########################################################################

class mifrmEditByte ( gui.frmEditByte ):
    """Frame para editar los nombres de los bytes"""
    
    def __init__(self, parent, item ):
        
        gui.frmEditByte.__init__ (self, parent)
        self.item = item
        global miBytes
        self.miBytes = miBytes[:]
        self.BytesTextCtrl = [] #lista con los wx.TextCtrl de edición de nombre de byte
        self.BytesValues = []
        self.modificado = False
        for i,valorByte in enumerate(self.miBytes):

            texto  = wx.StaticText(self.ByteScrolled, wx.ID_ANY, u"Bit Nº: %d"%i, wx.DefaultPosition, wx.DefaultSize, 0 )
            texto.Wrap( -1 )
            self.gridBotones.Add( texto, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
            # En Windows no se puede hacer wx.TextCtrl readonly luego\
            # de creado, por lo que debe hacerce cuando se crea:
            
            if valorByte[const.mod] == 0:
                
                textCtrl = wx.TextCtrl(self.ByteScrolled, wx.ID_ANY,\
                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,  wx.TE_READONLY )
                textValue =  wx.SpinCtrl(self.ByteScrolled, wx.ID_ANY,\
                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,\
                    wx.SP_ARROW_KEYS, -1, 255, int(self.miBytes[i][const.Valor]))
                                        
            else:
                
                textCtrl = wx.TextCtrl(self.ByteScrolled, wx.ID_ANY, \
                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
                textValue =  wx.SpinCtrl(self.ByteScrolled, wx.ID_ANY,\
                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,\
                    wx.SP_ARROW_KEYS, -1, 255, int(self.miBytes[i][const.Valor]))
                
            self.gridBotones.Add( textCtrl, 0, wx.ALL|wx.EXPAND, 5 )
            self.gridBotones.Add( textValue, 0, wx.ALL, 5 )
            textCtrl.SetValue(valorByte[const.Nombre])
            
            textValue.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl )
            textCtrl.Bind( wx.EVT_RIGHT_DOWN, self.OnBtnDerecho )
            
            self.BytesTextCtrl.append(textCtrl)
            self.BytesValues.append(textValue)
            
        self.ByteScrolled.SetSizer(self.gridBotones )
        self.ByteScrolled.Layout()
        self.ByteScrolled.SetAutoLayout(True)
        self.gridBotones.Fit(self.ByteScrolled )
        
        
    def OnSpinCtrl (self, event):
        self.modificado = True
        event.Skip()
        
    def OnBtnDerecho (self, event):
        txtctrl = event.GetEventObject()
        texto = self.miBytes[self.BytesTextCtrl.index(txtctrl)][1]
        win = infoPopup(self, wx.SIMPLE_BORDER,texto)
        
        pos = txtctrl.ClientToScreen( (0,0) )
        sz =  txtctrl.GetSize()
        win.Position(pos, (0, sz[1]))
        win.Popup()

    def OnByteSpinCtrl(self, event):
        spin = self.BytesSpinCtrl.GetValue()
        self.BytesTxtCtrl.SetValue(self.miBytes[spin])
        pass

    def OnText(self,event):
        self.miBytes[self.BytesSpinCtrl.GetValue()] = self.BytesTxtCtrl.GetValue()

    def OnEditByte(self, event):
        self.GuardarDatos()
        
    def GuardarDatos (self ):
        """guarda los cambios realizados"""
        global miBytes
        for i,txtctrl in enumerate(self.BytesTextCtrl):
            if txtctrl.IsModified():
                self.miBytes[i][const.Nombre] = txtctrl.GetValue()
                txtctrl.SetModified(False)
            self.miBytes[i][const.Valor] = str(self.BytesValues[i].GetValue())
        miBytes = self.miBytes[:]
        global Modificado
        Modificado = True  #Avisar modificación al programa global.
        self.modificado = False  #guardadas modificaciones en Bytes.
        

    def OnUndoByte(self, event):
        global miBytes
        self.miBytes = miBytes[:]
        for i,txtctrl in enumerate(self.BytesTextCtrl):
            txtctrl.SetValue(self.miBytes[i][const.Nombre])

    def OnClose(self, event):
        if self.modificado == False:
            for i in range(Cantidad_Bytes_Usuario):
                if self.BytesTextCtrl[i].IsModified():
                    self.modificado = True
                    break
        if self.modificado:
            dlg = wx.MessageDialog(self, u"Guardar cambios?",\
            caption=u"Cerrar Edición Bytes",
            style=wx.YES | wx.NO,
            pos=wx.DefaultPosition)
            val = dlg.ShowModal()
            if val == wx.ID_YES:
                global miBytes
                for i,txtctrl in enumerate(self.BytesTextCtrl):
                    if txtctrl.IsModified():
                        self.miBytes[i][const.Nombre] = txtctrl.GetValue()
                        miBytes = self.miBytes[:]
        self.modificado = False            
                
        self.item.Enable(True)
        event.Skip()

########################################################################
########################################################################
##############                                     #####################
##############   Edición del Diálogo Copiar Apps   #####################
##############                                     #####################
########################################################################
########################################################################


class miDlgCopiarApp ( gui.DialogoCopiarApp ):


    def __init__(self, parent ):
        gui.DialogoCopiarApp.__init__ (self, parent)
        self.padre = parent
        self.CargarChoices()

    def OnChoiceAppA(self, event):
        sel = self.choiceAppA.GetSelection()
        if not self.padre.AppMenuItems[sel].IsEnabled():
            self.choiceAppA.SetSelection(-1)
            dlg = wx.MessageDialog(self, u"Cierre la Edición de esta aplicación\n"+\
                u"antes de copiarla",caption="Error al copiar",
                style=wx.OK, pos=wx.DefaultPosition)
            dlg.ShowModal()


    def OnChoiceAppB(self, event):
        sel = self.choiceAppB.GetSelection()
        if not self.padre.AppMenuItems[sel].IsEnabled():
            self.choiceAppB.SetSelection(-1)
            dlg = wx.MessageDialog(self, u"Cierre la Edición de esta aplicación\n"+\
                u"antes de copiarla",caption="Error al copiar",
                style=wx.OK, pos=wx.DefaultPosition)
            dlg.ShowModal()


    def OnCopiar(self, event):
        selA = self.choiceAppA.GetSelection()
        selB = self.choiceAppB.GetSelection()
        if (selA == -1) or (selB == -1):
            dlg = wx.MessageDialog(self, u"Seleccionar Aplicaciones\n",\
                caption="Error al copiar", style=wx.OK, pos=wx.DefaultPosition)
            dlg.ShowModal()
        else:
            num = self.padre.aplicaciones[selA].AppNum
            self.padre.aplicaciones[selA] = self.padre.aplicaciones[selB].copy()
            self.padre.aplicaciones[selA].AppNum = num
            self.padre.AppMenuItems[num].SetText(u"Aplicación %0.2d: %s"%(num,self.padre.aplicaciones[selA].Nombre))
            self.txtctrlCopia.AppendText("Copiado %s en %s\n"%(selB,selA))
            self.CargarChoices()
            global Modificado
            Modificado = True

    def OnCerrar(self, event):
        self.Destroy()

    def CargarChoices(self):
        choices = []
        for i in self.padre.aplicaciones:
            choices.append("%0.2d: %s"%(i.AppNum,i.Nombre))
        self.choiceAppA.SetItems(choices)
        self.choiceAppB.SetItems(choices)

########################################################################
########################################################################
##############                                      ####################
##############   Edición del Dialogo copiar estado  ####################
##############                                      ####################
########################################################################
########################################################################

class miDlgCopiarEstado ( gui.DlgCopiarEstado ):
    """Copiar un estado a otro, copia todo menos el número de estado"""

    def __init__(self, parent):
        super(miDlgCopiarEstado,self).__init__(parent)
        self.padre = parent
        self.NumApp = parent.tempApp.AppNum
        self.CargarChoices()

    def OnCopiar(self, event):
        selA = self.choiceEstA.GetSelection()
        selB = self.choiceEstB.GetSelection()
        if (selA == -1) or (selB == -1):
            dlg = wx.MessageDialog(self, u"Seleccionar Estados\n",\
                caption="Error al copiar", style=wx.OK, pos=wx.DefaultPosition)
            dlg.ShowModal()
        else:
            #num = self.padre.EstadosDic[selA].
            self.padre.tempApp.Estados[self.choices[1][selA]] = \
                self.padre.tempApp.Estados[self.choices[1][selB]].copy()

            self.txtctrlCopia.AppendText("Copiado %s en %s\n"%(\
                GetTexto(self.choiceEstB),GetTexto(self.choiceEstA)))
            self.CargarChoices()
            self.padre.CargarLista()

    def CargarChoices (self ):
        self.choices = [[],[]]
        for i in range(Cantidad_Estados):
            #Los estados que están siendo editados no son puestos en la
            #lista.
            if not self.padre.EstadosDic[i].opened:
                titulo = self.padre.EstadosDic[i].Nombre
                titulo = "%0.2d"%i + " : " + titulo
                #Agrega el nombre y el estado a la lista choices
                self.choices[0].append(titulo)
                self.choices[1].append(i)

        self.choiceEstA.SetItems(self.choices[0])
        self.choiceEstB.SetItems(self.choices[0])

    def OnCerrar(self, event):
        self.Destroy()

########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Analog        #######################
##############                                   #######################
########################################################################
########################################################################

class mifrmAnalog ( gui.frmAnalog ):

    def __init__(self, parent ):
        gui.frmAnalog.__init__ (self, parent)
        self.padre = parent
        global miAnalogica
        self.tempAnalogica = miAnalogica.copy()
        for llave in nZonas:
            # busca dentro de los bytes definidos cual es el que corresponde a cada límite
            # y carga los datos en el vector de bytes (MemoriaUsuario_Bytes)
            for i in range(len(DefinicionesBytes)):
                if miBytes[i][const.Nombre] == llave:
                    self.tempAnalogica[llave]  = miBytes[i][const.Valor]
                    
        for i in range(len(DefinicionesBits)):
            if miBits[i][const.Nombre] == "an0Zonas":
                self.tempAnalogica["modo"] = miBits[i][const.Valor] 
                break
                
        for i in range(len(DefinicionesBytes)):
            if miBytes[i][const.Nombre] == EntradasAn[0]:
                self.tempAnalogica["tiempo"] = miBytes[i][const.Valor]
            if miBytes[i][const.Nombre] == EntradasAn[1]:
                self.tempAnalogica["muestras"] = miBytes[i][const.Valor]
                
                    
        #diccionario con los objetos spin para obtener los datos de los límites
        self.zonas = {\
            nZonas[0]:[self.spinAsup,0],\
            nZonas[1]:[self.spinAinf,0],\
            nZonas[2]:[self.spinBsup,0],\
            nZonas[3]:[self.spinBinf,0],\
            nZonas[4]:[self.spinCsup,0],\
            nZonas[5]:[self.spinCinf,0],\
            nZonas[6]:[self.spinDsup,0],\
            nZonas[7]:[self.spinDinf,0]\
            }
        
        for zona in self.zonas.keys():
        
            self.zonas[zona][1] = self.tempAnalogica[zona]
        
        for zona in self.zonas.keys():
        
            self.zonas[zona][0].SetValue(int(self.zonas[zona][1]))
            
        self.txtctrlMuestras.SetValue(int(self.tempAnalogica["muestras"]))
        self.txtctrlTiempo.SetValue(int(self.tempAnalogica["tiempo"]))
        self.txtctrlComentarios.SetValue(self.tempAnalogica["comentarios"])
        
        for zona in self.zonas.keys():
            self.zonas[zona][0].Enable(False)
        self.radbtnValorADC.SetValue(False)
        self.radbtn4zonas.SetValue(False)
        
        if self.tempAnalogica["modo"] != "-1":
            print "modo distinto a -1"
            if self.tempAnalogica["modo"] == False:
                for zona in self.zonas.keys():
                    self.zonas[zona][0].Enable(True)
                self.radbtn4zonas.SetValue(True)
            elif self.tempAnalogica["modo"] == True: 
                self.radbtnValorADC.SetValue(True)
                for zona in self.zonas.keys():
                    self.zonas[zona][0].Enable(False)                
        self.cambios = False
        

    def On4zonas(self, event):
        for zona in self.zonas.keys():
            self.zonas[zona][0].Enable(True)
        self.cambios = True
        self.radbtnValorADC.SetValue(False)
        event.Skip()

    def OnValorADC(self, event):
        for zona in self.zonas.keys():
            self.zonas[zona][0].Enable(False)
        self.cambios = True
        self.radbtn4zonas.SetValue(False)
        event.Skip()

    def OnGuardar(self, event):
        self.Guardar()

    def Guardar(self):
        if not self.DatosValidos():
            dlg = wx.MessageDialog(self, u"Límites de zonas\nincorrectos",\
                caption="Error al guardar", style=wx.OK, pos=wx.DefaultPosition)
            dlg.ShowModal()
        else:
            global miAnalogica
            miAnalogica = self.tempAnalogica.copy()
            
            for llave in nZonas:
                # busca dentro de los bytes definidos cual es el que corresponde a cada límite
                # y carga los datos en el vector de bytes (MemoriaUsuario_Bytes)
                for i in range(len(DefinicionesBytes)):
                    if miBytes[i][const.Nombre] == llave:
                        miBytes[i][const.Valor] = self.tempAnalogica[llave]
            
            self.cambios = False
            self.leerDatos()
            global Modificado
            Modificado = True


    def OnCargarDefault(self, event):
        self.cambios = True
        global Analogica
        self.tempAnalogica = Analogica.copy()
        for zona in self.zonas.keys():
            self.zonas[zona][1] = self.tempAnalogica[zona]
        for zona in self.zonas.keys():
            self.zonas[zona][0].SetValue(\
                self.zonas[zona][1])
        self.txtctrlMuestras.SetValue(str(self.tempAnalogica["muestras"]))
        self.txtctrlTiempo.SetValue(str(self.tempAnalogica["tiempo"]))
        self.txtctrlComentarios.SetValue("")

    def OnClose(self, event):
        if not self.cambios:
            self.padre.m_drivers_analog.Enable(True)
            self.Destroy()
        else:
            dlg = wx.MessageDialog(self, u"Guardar cambios?",\
                caption=u"Cerrar Edición Analógica",
                style=wx.YES | wx.NO,
                pos=wx.DefaultPosition)
            val = dlg.ShowModal()
            if val == wx.ID_YES:
                self.Guardar()
            self.Destroy()
            self.padre.m_drivers_analog.Enable(True)

    def OnInfo(self, event):
        win = miFrameZonas(self)
        win.Show()

    def OnCambios (self, event):
        self.cambios = True
        event.Skip()

    def OnChar(self, event):
        self.cambios = True
        EsNumero( event)

    def OnSpin (self, event):
        self.cambios = True
        event.Skip()

    def DatosValidos(self ):

        self.leerDatos()
        #si todas las zonas son -1 no verifica datos válidos. (no se modificarán los datos
        # precargados en el programa.
        if ((self.zonas[nZonas[0]][1] == -1) and (self.zonas[nZonas[0]][1] == -1) and\
                (self.zonas[nZonas[0]][1] == -1) and (self.zonas[nZonas[0]][1] == -1) and\
                (self.zonas[nZonas[0]][1] == -1) and (self.zonas[nZonas[0]][1] == -1) and\
                (self.zonas[nZonas[0]][1] == -1)):
            return True
            
        if ((self.zonas[nZonas[0]][1]>self.zonas[nZonas[1]][1]) and\
            (self.zonas[nZonas[1]][1]>self.zonas[nZonas[2]][1]) and\
            (self.zonas[nZonas[2]][1]>self.zonas[nZonas[3]][1]) and\
            (self.zonas[nZonas[3]][1]>self.zonas[nZonas[4]][1]) and\
            (self.zonas[nZonas[4]][1]>self.zonas[nZonas[5]][1]) and\
            (self.zonas[nZonas[5]][1]>self.zonas[nZonas[6]][1]) and\
            (self.zonas[nZonas[6]][1]>self.zonas[nZonas[7]][1])):
            return True
        else:
            return False

    def leerDatos(self):

        for zona in self.zonas.keys():
            resultado = self.zonas[zona][0].GetValue()
            self.zonas[zona][1] = 0 if (resultado == "") else int(resultado)
            self.tempAnalogica[zona]=self.zonas[zona][1]

        tiempo = self.txtctrlTiempo.GetValue()
        self.tempAnalogica[EntradasAn[0]] = -1 if tiempo == "" else int(tiempo)
        muestras = self.txtctrlMuestras.GetValue()
        self.tempAnalogica[EntradasAn[1]] = -1 if muestras == "" else int(muestras)
        
        self.tempAnalogica["modo"] = PorZonas if self.radbtn4zonas.GetValue()\
                else ValorADC
        for i in range(len(DefinicionesBits)):
            if miBits[i][const.Nombre] == "an0Zonas":
                miBits[i][const.Valor] = self.tempAnalogica["modo"]
                break
        self.tempAnalogica["comentarios"] = self.txtctrlComentarios.GetValue()
        
    def OnEnter(self, event):
        pass

########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Editar Zonas  #######################
##############                                   #######################
########################################################################
########################################################################

class miFrameZonas(gui.FrameZonas):

    def __init__(self, parent):
        super(miFrameZonas, self).__init__(parent)

    def OnClose(self, event):
        self.Destroy()

########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Editar SMSs   #######################
##############                                   #######################
########################################################################
########################################################################

class mifrmSMS ( gui.frmCfgServers ):
    """Frame para editar SMS"""
    def __init__(self, parent , item):
        gui.frmCfgServers.__init__ (self, parent )
        self.item = item
        self.SetTitle(u"Edición de mensajes SMS")
        self.item.Enable(False)
        global miSMS
        self.miSMS = miSMS[:]
        self.ListaSMS = []
        for i in range(Cantidad_SMS):
            smsnum = wx.StaticText(self.CfgScrolled, wx.ID_ANY, u"SMS %i"%i, wx.DefaultPosition, wx.DefaultSize, 0 )
            smsnum.Wrap( -1 )
            self.GridCfg.Add( smsnum, wx.GBPosition( i, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
            texto = wx.TextCtrl(self.CfgScrolled, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
            texto.SetMaxLength( 160 ) 
            texto.SetValue(self.miSMS[i].decode('latin1','ignore'))
            self.GridCfg.Add( texto, wx.GBPosition( i, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
            botonborrar = wx.Button(self.CfgScrolled, wx.ID_ANY, u"Borrar SMS", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.GridCfg.Add( botonborrar, wx.GBPosition( i, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
            botonborrar.Bind(wx.EVT_BUTTON , self.OnBorrarSMS)
            self.ListaSMS.append([texto,botonborrar]) #Asocio el boton borrar con el texto
        self.CfgScrolled.SetSizer(self.GridCfg )
        self.CfgScrolled.Layout()
        self.CfgScrolled.SetAutoLayout(True)
        self.GridCfg.Fit(self.CfgScrolled )
            
    def OnClose(self, event):
        cambios = False
        for i,[txtctrl,boton] in enumerate(self.ListaSMS):
            if txtctrl.IsModified():
                cambios = True
                break
        if cambios:
            dlg = wx.MessageDialog(self, u"Guardar cambios?",\
            caption=u"Cerrar Edición SMS",
            style=wx.YES | wx.NO,
            pos=wx.DefaultPosition)
            val = dlg.ShowModal()
            if val == wx.ID_YES:
                global miSMS
                for i,[txtctrl,boton] in enumerate(self.ListaSMS):
                    if txtctrl.IsModified():
                        self.miSMS[i] = txtctrl.GetValue()
                        miSMS = self.miSMS[:]
        
        self.item.Enable(True)
        self.Destroy()
        
    def OnBorrarSMS (self, event):
        btn = event.GetEventObject()
        for texto ,boton in self.ListaSMS:
            if btn is boton:
                texto.SetValue("")
                texto.SetModified(True)
                
    def OnGuardarSMS(self, event):
        global miSMS
        for i,[txtctrl,btn] in enumerate(self.ListaSMS):
            if txtctrl.IsModified():
                self.miSMS[i] = txtctrl.GetValue().encode('latin','ignore')
        miSMS = self.miSMS[:]
        for [txtctrl,btn] in self.ListaSMS:
            txtctrl.SetModified(False)
        global Modificado
        Modificado = True
        
    def OnUndo (self, event) :
        global miSMS
        self.miSMS= miSMS[:]
        for i,[txtctrl,btn] in enumerate(self.ListaSMS):
            txtctrl.SetValue(self.miSMS[i])
    
    def OnCargarSms(self, event):
        global DIRACTUAL
        dlg = wx.FileDialog(
            self, message="Copiar Desde ...", defaultDir=DIRACTUAL,
            defaultFile="", wildcard=wildcard, style=wx.OPEN)
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                shelf = shelve.open(path)
            except:
                dlg = wx.MessageDialog(self, u"No es un archivo válido",\
                    caption="Error al abrir archivo",\
                    pos=wx.DefaultPosition)
                dlg.ShowModal()
                dlg.Destroy()
                return
            global miSMS
            try: 
                self.miSMS = shelf["SMS"]
                for i,[txtctrl,btn] in enumerate(self.ListaSMS):
                    txtctrl.SetValue(self.miSMS[i])
                    txtctrl.SetModified(True)
            except:
                pass
            shelf.close()
        dlg.Destroy()

########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Editar IPs    #######################
##############                                   #######################
########################################################################
########################################################################

class mifrmIPs ( gui.frmCfgServers ):
    """Frame para editar IP"""
    def __init__(self, parent , item):
        gui.frmCfgServers.__init__ (self, parent )
        self.item = item
        self.SetTitle(u"Edición de servidores IP")
        self.item.Enable(False)
        global miSERVERS
        self.miSERVERS = miSERVERS[:]
        
        self.ListaIPs = []
        #self.GridCfg = wx.FlexGridSizer( 0, 6, 0, 0 ) #Agrego dos columnas para centrar 
        #self.GridCfg.AddGrowableCol(0)
        #self.GridCfg.AddGrowableCol(2)
        self.GridCfg.RemoveGrowableCol(1)
        self.GridCfg.AddGrowableCol(2)
        for i in range(Cantidad_WEBs):  
         
            ipnum = wx.StaticText(self.CfgScrolled, wx.ID_ANY, u"IP %i"%i, wx.DefaultPosition, wx.DefaultSize, 0 )
            ipnum.Wrap( -1 )
            self.GridCfg.Add( ipnum , wx.GBPosition( i, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
            ChkBoxIp = wx.CheckBox( self.CfgScrolled, wx.ID_ANY, u"Usar IP", wx.DefaultPosition, wx.DefaultSize, 0 )
            ChkBoxIp.SetValue(not self.miSERVERS[i][0])
            
            self.GridCfg.Add( ChkBoxIp, wx.GBPosition( i, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
            
            ipaddr = masked.IpAddrCtrl( self.CfgScrolled, -1, style = wx.TE_PROCESS_TAB )
            netaddr = wx.TextCtrl(self.CfgScrolled, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0) 
            netaddr.SetMaxLength( 160 ) 
            if self.miSERVERS[i][0]:
            #Verifico si el campo a cargar es una IP o una www
                self.GridCfg.Add( netaddr , wx.GBPosition( i, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
                netaddr.SetValue(self.miSERVERS[i][1].decode('latin1','ignore'))

                ipaddr.Hide()
            else:
                self.GridCfg.Add( ipaddr , wx.GBPosition( i, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
                try:
                    ipaddr.SetValue(self.miSERVERS[i][1])
                except:
                    ipaddr.SetValue("0.0.0.0")
                netaddr.Hide()
                
            botonborrar = wx.Button(self.CfgScrolled, wx.ID_ANY, u"Borrar IP", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.GridCfg.Add( botonborrar, wx.GBPosition( i, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
            botonborrar.Bind(wx.EVT_BUTTON , self.OnBorrarIP)
            self.ListaIPs.append([ipaddr,netaddr,ChkBoxIp,botonborrar]) #Asocio el boton borrar con el texto
            self.Bind(wx.EVT_CHECKBOX, self.OnChekIP, id=ChkBoxIp.GetId())
            
        self.CfgScrolled.SetSizer(self.GridCfg )
        self.CfgScrolled.Layout()
        #self.CfgScrolled.SetAutoLayout(True)
        
        self.GridCfg.Fit(self.CfgScrolled )
           
           
    def OnChekIP(self,event):
        chkbox = event.GetEventObject()
        for ipaddr ,netaddr, chkboxip, boton in self.ListaIPs:
            if chkbox is chkboxip:
                if not chkbox.GetValue():
                    x,y = self.GridCfg.GetItemPosition(ipaddr)
                    ipaddr.Hide()
                    netaddr.Show()
                    self.GridCfg.Detach(ipaddr)
                    self.GridCfg.Add(netaddr,wx.GBPosition(x,y), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )                 
                else:
                    x,y = self.GridCfg.GetItemPosition(netaddr)
                    ipaddr.Show()
                    netaddr.Hide()
                    self.GridCfg.Detach(netaddr)
                    self.GridCfg.Add(ipaddr,wx.GBPosition(x,y), wx.GBSpan( 1, 1 ), wx.ALL, 5  )            
        self.CfgScrolled.Layout() 

            
    def OnClose(self, event):
        cambios = False
        for i,[ipaddr ,netaddr, chkboxip, boton] in enumerate(self.ListaIPs):
            if ipaddr.IsModified():
                cambios = True
                break
        if cambios:
            dlg = wx.MessageDialog(self, u"Guardar cambios?",\
            caption=u"Cerrar Edición IPs",
            style=wx.YES | wx.NO,
            pos=wx.DefaultPosition)
            val = dlg.ShowModal()
            if val == wx.ID_YES:
                self.Guardar()
        
        self.item.Enable(True)
        self.Destroy()
        
    def OnBorrarIP (self, event):
        btn = event.GetEventObject()
        for ipaddr ,netaddr, chkboxip, boton in self.ListaIPs:
            if btn is boton:
                ipaddr.Clear()
                ipaddr.SetModified(True)
                netaddr.Clear()
                netaddr.SetModified(True)
                                
    def OnGuardar(self, event):
        global miSERVERS
        self.Guardar()
        
    def Guardar(self):
        for i,[ipaddr ,netaddr, chkboxip, boton] in enumerate(self.ListaIPs):
        
            if chkboxip.GetValue():
            #Chekear si es una dirección IP o web
                        
                self.miSERVERS[i][0]=False
                self.miSERVERS[i][1] = ipaddr.GetValue()
                miSERVERS = self.miSERVERS[:]
            else:    
                self.miSERVERS[i][0]=True
                self.miSERVERS[i][1] = netaddr.GetValue()
                miSERVERS = self.miSERVERS[:]
               
        for [ipaddr ,netaddr, chkboxip, boton] in self.ListaIPs:
            ipaddr.SetModified(False)
            netaddr.SetModified(False)
            global Modificado
            Modificado = True
        
    def OnUndo (self, event):
        global miSERVERS
        self.miSERVERS = miSERVERS[:]
        for i,[ipaddr ,netaddr, chkboxip, boton] in enumerate(self.ListaIPs):
            self.GridCfg.Detach(ipaddr)
            self.GridCfg.Detach(netaddr)
            if self.miSERVERS[i][0]:
            #Verifico si el campo a cargar es una IP o una www
                self.GridCfg.Add( netaddr , wx.GBPosition( i, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
                netaddr.SetValue(self.miSERVERS[i][1].decode('latin1','ignore'))
                netaddr.Show()
                ipaddr.Hide()
                chkboxip.SetValue(False)
            else:
                self.GridCfg.Add( ipaddr , wx.GBPosition( i, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
                try:
                    ipaddr.SetValue(self.miSERVERS[i][1])
                except:
                    ipaddr.SetValue("0.0.0.0")
                ipaddr.Show()
                netaddr.Hide()
                chkboxip.SetValue(True)
    
    def OnCargar(self, event):
        global DIRACTUAL
        dlg = wx.FileDialog(
            self, message="Copiar Desde ...", defaultDir=DIRACTUAL,
            defaultFile="", wildcard=wildcard, style=wx.OPEN)
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                shelf = shelve.open(path)
            except:
                dlg = wx.MessageDialog(self, u"No es un archivo válido",\
                    caption="Error al abrir archivo",\
                    pos=wx.DefaultPosition)
                dlg.ShowModal()
                dlg.Destroy()
                return
            global miSERVERS
            try: 
                self.miSERVERS = shelf["IP"]
                for i,[ipaddr ,netaddr, chkboxip, boton] in enumerate(self.ListaIPs):
                    if self.miSERVERS[i][0]:
                        #Verifico si el campo a cargar es una IP o una www
                        self.GridCfg.Add( netaddr , wx.GBPosition( i, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
                        netaddr.SetValue(self.miSERVERS[i][1].decode('latin1','ignore'))
                        ipaddr.Hide()
                    else:
                        self.GridCfg.Add( ipaddr , wx.GBPosition( i, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
                        try:
                            ipaddr.SetValue(self.miSERVERS[i][1])
                        except:
                            ipaddr.SetValue("0.0.0.0")
                            netaddr.Hide()
            except:
                pass
            shelf.close()
        dlg.Destroy()

########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Editar TELs   #######################
##############                                   #######################
########################################################################
########################################################################

class mifrmTEL ( gui.frmCfgServers ):
    """Frame para editar TEL"""
    def __init__(self, parent , item):
        gui.frmCfgServers.__init__ (self, parent )
        self.item = item
        self.SetTitle(u"Edición de números telefónicos")
        self.item.Enable(False)
        global miTEL
        self.miTEL = miTEL[:]
        self.ListaTELs = []
        control = ("Phone No","##############","",'F',"",'','','')
        for i in range(Cantidad_TEL):
            telnum = wx.StaticText(self.CfgScrolled, wx.ID_ANY, u"TEL %i"%i, wx.DefaultPosition, wx.DefaultSize, 0 )
            telnum.Wrap( -1 )
            self.GridCfg.Add( telnum, wx.GBPosition( i, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
            
            teladdr  = masked.TextCtrl( self.CfgScrolled , -1, "",
                                                mask         = control[1],
                                                excludeChars = control[2],
                                                formatcodes  = control[3],
                                                includeChars = "",
                                                validRegex   = control[4],
                                                validRange   = control[5],
                                                choices      = control[6],
                                                choiceRequired = True,
                                                defaultValue = control[7],
                                                demo         = True,
                                                name         = control[0])  
            teladdr.SetValue(self.miTEL[i])
            self.GridCfg.Add( teladdr,  wx.GBPosition( i, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
            botonborrar = wx.Button(self.CfgScrolled, wx.ID_ANY, u"Borrar TEL", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.GridCfg.Add( botonborrar,  wx.GBPosition( i, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
            botonborrar.Bind(wx.EVT_BUTTON , self.OnBorrarTEL)
            self.ListaTELs.append([teladdr,botonborrar]) #Asocio el boton borrar con el texto


        self.CfgScrolled.SetSizer(self.GridCfg )
        self.CfgScrolled.Layout()
        self.CfgScrolled.SetAutoLayout(True)
        self.GridCfg.Fit(self.CfgScrolled )
            
    def OnClose(self, event):
        cambios = False
        for i,[txtctrl,boton] in enumerate(self.ListaTELs):
            if txtctrl.GetValue().strip() != self.miTEL[i].strip(): 
                cambios = True
                break
        if cambios:
            dlg = wx.MessageDialog(self, u"Guardar cambios?",\
                                   caption=u"Cerrar Edición Teléfonos",
                                   style=wx.YES | wx.NO,
                                   pos=wx.DefaultPosition)
            val = dlg.ShowModal()
            if val == wx.ID_YES:
                global miTEL
                for i,[txtctrl,boton] in enumerate(self.ListaTELs):
                    if txtctrl.IsModified():
                        self.miTEL[i] = txtctrl.GetValue()
                        miTEL = self.miTEL[:]
        
        self.item.Enable(True)
        self.Destroy()
        
    def OnBorrarTEL (self, event):
        btn = event.GetEventObject()
        for teladdr ,boton in self.ListaTELs:
            if btn is boton:
                teladdr.Clear()
                teladdr.SetModified(True)
                
    def OnGuardar(self, event):
        global miTEL
        for i,[teladdr,btn] in enumerate(self.ListaTELs):
            if teladdr.IsModified():
                self.miTEL[i] = teladdr.GetValue()
        miTEL = self.miTEL[:]
        print miTEL        
        global Modificado
        Modificado = True
        
    def OnUndo (self, event) :
        global miTEL
        self.miTEL= miTEL[:]
        for i,[txtctrl,btn] in enumerate(self.ListaTELs):
            txtctrl.SetValue(self.miTEL[i])
    
    def OnCargar(self, event):
        global DIRACTUAL
        dlg = wx.FileDialog(
            self, message="Copiar Desde ...", defaultDir=DIRACTUAL,
            defaultFile="", wildcard=wildcard, style=wx.OPEN)
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                shelf = shelve.open(path)
            except:
                dlg = wx.MessageDialog(self, u"No es un archivo válido",\
                    caption="Error al abrir archivo",\
                    pos=wx.DefaultPosition)
                dlg.ShowModal()
                dlg.Destroy()
                return
            global miTEL
            try: 
                self.miTEL = shelf["TEL"]
                for i,[txtctrl,btn] in enumerate(self.ListaTELs):
                    txtctrl.SetValue(self.miTEL[i])
                    txtctrl.SetModified(True)
            except:
                pass
            shelf.close()
        dlg.Destroy()





########################################################################
########################################################################
##############                                   #######################
##############    Edición del Frame Editar       #######################
##############    timers                         #######################
##############                                   #######################
########################################################################
########################################################################

class mifrmNuevoTimer ( gui.frmTimers ):
    """Frame para crear timers"""
    def __init__(self,parent,item):
        gui.frmTimers.__init__(self,parent)
        self.item = item
    
    def OnFecha(self,event):
        
        self.panelTimer.Enable(False)
        self.panelFecha.Enable(True)
        event.Skip()
        
    def OnTimer(self,event):
        
        self.panelFecha.Enable(False)
        self.panelTimer.Enable(True)
        event.Skip()


########################################################################
########################################################################
##############                                   #######################
##############    Edición del Frame Editar       #######################
##############      Mails                        #######################
##############                                   #######################
########################################################################
########################################################################

class mifrmMAIL ( gui.frmCfgServers ):
    """Frame para editar Direcciones mail"""
    def __init__(self, parent , item):
        gui.frmCfgServers.__init__ (self, parent )
        self.item = item
        self.SetTitle(u"Edición de e-mails")
        self.item.Enable(False)
        global miMAIL
        self.miMAIL = miMAIL[:]
        self.ListaMAILs = [] 
        for i in range(Cantidad_MAIL):
              
            mailnum = wx.StaticText(self.CfgScrolled, wx.ID_ANY, u"Dirección %i"%i, wx.DefaultPosition, wx.DefaultSize, 0 )
            mailnum.Wrap( -1 )
            self.GridCfg.Add( mailnum, wx.GBPosition( i, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
            mailaddr = masked.Ctrl( self.CfgScrolled, -1, "",
                                    autoformat       = 'EMAIL',
                                    demo             = True,
                                    name             = 'EMAIL')
 
            mailaddr.SetValue(self.miMAIL[i].decode('latin1','ignore')) 
            self.GridCfg.Add( mailaddr, wx.GBPosition( i, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
            botonborrar = wx.Button(self.CfgScrolled, wx.ID_ANY, u"Borrar MAIL", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.GridCfg.Add( botonborrar,wx.GBPosition( i, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
            botonborrar.Bind(wx.EVT_BUTTON , self.OnBorrarMAIL)
            self.ListaMAILs.append([mailaddr,botonborrar]) #Asocio el boton borrar con el texto
            
        self.CfgScrolled.SetSizer(self.GridCfg )
        self.CfgScrolled.Layout()
        self.CfgScrolled.SetAutoLayout(True)
        self.GridCfg.Fit(self.CfgScrolled )
            
    def OnClose(self, event):
        cambios = False
        for i,[txtctrl,boton] in enumerate(self.ListaMAILs):
            if txtctrl.GetValue().strip() != miMAIL[i].strip():
                cambios = True
                break
        if cambios:
            dlg = wx.MessageDialog(self, u"Guardar cambios?",\
            caption=u"Cerrar Edición MAILs",
            style=wx.YES | wx.NO,
            pos=wx.DefaultPosition)
            val = dlg.ShowModal()
            if val == wx.ID_YES:
                global miMAIL
                for i,[txtctrl,boton] in enumerate(self.ListaMAILs):
                    if txtctrl.IsModified():
                        self.miMAIL[i] = txtctrl.GetValue().strip()
                        miMAIL = self.miMAIL[:]
        
        self.item.Enable(True)
        self.Destroy()
        
    def OnBorrarMAIL (self, event):
        btn = event.GetEventObject()
        for ipaddr ,boton in self.ListaMAILs:
            if btn is boton:
                ipaddr.Clear()
                ipaddr.SetModified(True)
                
    def OnGuardar(self, event):
        global miMAIL
        for i,[ipaddr,btn] in enumerate(self.ListaMAILs):
            if ipaddr.IsModified():
                self.miMAIL[i] = ipaddr.GetValue()
        miMAIL = self.miMAIL[:]
        print miMAIL
        for [ipaddr,btn] in self.ListaMAILs:
            ipaddr.SetModified(False)
        global Modificado
        Modificado = True
        
    def OnUndo (self, event) :
        global miMAIL
        self.miMAIL= miMAIL[:]
        for i,[txtctrl,btn] in enumerate(self.ListaMAILs):
            txtctrl.SetValue(self.miMAIL[i])
    
    def OnCargar(self, event):
        global DIRACTUAL
        dlg = wx.FileDialog(
            self, message="Copiar Desde ...", defaultDir=DIRACTUAL,
            defaultFile="", wildcard=wildcard, style=wx.OPEN)
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                shelf = shelve.open(path)
            except:
                dlg = wx.MessageDialog(self, u"No es un archivo válido",\
                    caption="Error al abrir archivo",\
                    pos=wx.DefaultPosition)
                dlg.ShowModal()
                dlg.Destroy()
                return
            global miMAIL
            try: 
                self.miMAIL = shelf["IP"]
                for i,[txtctrl,btn] in enumerate(self.ListaMAILs):
                    txtctrl.SetValue(self.miMAIL[i])
                    txtctrl.SetModified(True)
            except:
                pass
            shelf.close()
        dlg.Destroy()


def EsNumero(event):

    keycode = event.GetKeyCode()
    if keycode < 255:
    # valid ASCII
        if chr(keycode).isdigit():
            # Valid alphanumeric character
            event.Skip()
        elif keycode < 31 or keycode == 127 or keycode == '\n':
            event.Skip()
    elif keycode > 255:
        event.Skip()

def GetTexto(elec):
    return elec.GetString(elec.GetSelection())



aplicacion = wx.App(0)
frame_usuario = MiFrame()
frame_usuario.Show()
aplicacion.MainLoop()
