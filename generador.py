#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generador.py
#
#  Copyright 2013 santiago <spaleka@cylgem.com.ar>
#


#TODO usar isModified() para guardar cambios.
import gui
import wx
import os
import shelve
from apps import *

VERSION = 0.1
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

global ValoresEntradas
#diccionario con los valores de las entradas
global miValoresEntradas
#copia del diccionario, con los valores del programa actual
miValoresEntradas = {}
for i in ValoresEntradas.keys():
    miValoresEntradas[i] = ValoresEntradas[i][:]

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

        for i in range(Cantidad_Apps):
            self.aplicaciones.append(Aplicacion(i,""))
            # Crea aplicaciones vacías
            item = wx.MenuItem( self.m_aplicaciones, wx.ID_ANY, \
                u"Aplicación %0.2d: %s"%(i,self.aplicaciones[i].Nombre) ,\
                wx.EmptyString, wx.ITEM_NORMAL )
            self.m_aplicaciones.AppendItem(item)
            self.AppMenuItems[i] = item
            # Agrega el item al diccionario para la aplicación i
            self.Bind ( wx.EVT_MENU, self.OnAbrirApp, id = item.GetId() )
            item.Enable ( True )
            
            #boton = wx.Button( self.scroolled, wx.ID_ANY,\
                #u"Aplicación: %0.2d"%i, wx.DefaultPosition, wx.DefaultSize, 0 )
            #self.sizerbotones.Add( boton, 0, wx.ALL, 5 )
            #boton.Bind(wx.EVT_BUTTON, self.OnImprimirApp)
        item = wx.MenuItem( self.m_aplicaciones, wx.ID_ANY, u"Copiar Aplicación",\
            wx.EmptyString, wx.ITEM_NORMAL )
        self.m_aplicaciones.AppendItem(item)
        self.Bind ( wx.EVT_MENU, self.OnCopiarApp, id = item.GetId() )


        self.sizerbotones.Fit( self.scroolled )
        for i in Entradas:
            item = wx.MenuItem( self.m_drivers, wx.ID_ANY, i,\
                wx.EmptyString, wx.ITEM_NORMAL )
            self.m_drivers.AppendItem( item )
            self.Bind ( wx.EVT_MENU, self.OnDriver, id = item.GetId() )
        item = wx.MenuItem ( self.m_drivers , wx.ID_ANY, u"Cargar desde archivo...",\
            wx.EmptyString, wx.ITEM_NORMAL )
        self.m_drivers.AppendItem ( item )
        self.Bind ( wx.EVT_MENU, self.OnCopiarDesde, id = item.GetId() )
        self.Entradas = {}

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

    def OnEditarBytes( self, event ):
        id = event.GetId()
        item = self.GetMenuBar().FindItemById(id)
        item.Enable(False)
        win = mifrmEditByte(self,item)
        win.Show()


    def OnEditarBit( self, event ):
        id = event.GetId()
        item = self.GetMenuBar().FindItemById(id)
        item.Enable(False)
        win = mifrmEditBit(self,item)
        win.Show()


    def OnDriverAnalog( self, event ):
        id = event.GetId()
        item = self.GetMenuBar().FindItemById(id)
        item.Enable(False)
        win = mifrmAnalog(self)
        win.Show()

        pass


    def OnDriver( self, event ):
        id = event.GetId()
        item = self.GetMenuBar().FindItemById(id)
        win = mifrmEntrada(self,item)
        item.Enable(False)
        win.Show()


    def OnTest(self, event):
        self.GetActiveChild()
        for i in self.aplicaciones:
            print i


    def OnAbrirApp(self,event):

        id = event.GetId()
        item = self.GetMenuBar().FindItemById(id)
        for i in self.aplicaciones:
            if u"Aplicación %0.2d: %s"%(i.AppNum,i.Nombre) ==item.GetText():
                win = mifrmEditApp(self,i)
                win.Show(True)
                item.Enable(False)
                return


    def OnImprimirApp(self, event):

        boton = event.GetEventObject()
        numero = int(boton.GetLabel()[-2:])
        print u"\n\naplicación %d: %s"% (self.aplicaciones[numero].AppNum\
            ,self.aplicaciones[numero].Nombre)
        for i in range(Cantidad_Estados):
            print str(self.aplicaciones[numero].Estados[i].Nombre) + "\n"

    def OnCopiarApp(self, event):

        dlg = miDlgCopiarApp(self)
        dlg.ShowModal()

    def OnCopiarDesde( self, event):
        global DIRCATUAL
        dlg = wx.FileDialog(
            self, message="Copiar Desde ...", defaultDir=DIRCATUAL,
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
            global miValoresEntradas
            try:
                miValoresEntradas = shelf["miValoresEntradas"]
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




    def OnNuevoPrograma ( self, event):

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
        global DIRACTUAL
        global NombreArchivo
        self.OnNuevoPrograma(event)

        if self.cancel:

            pass

        dlg = wx.FileDialog(
            self, message="Abrir archivo ...", defaultDir=DIRACTUAL,
            defaultFile="", wildcard=wildcard, style=wx.OPEN)

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
                global miValoresEntradas
                miValoresEntradas = shelf["miValoresEntradas"]
                global miAnalogica
                miAnalogica = shelf["miAnalogica"]
            except:
                pass
            shelf.close()
            self.Title = "Generador de programas: " + NombreArchivo.split(os.sep)[-1]
            for i in range(Cantidad_Apps):
                self.AppMenuItems[i].SetText(\
                    u"Aplicación %0.2d: %s"%(i,self.aplicaciones[i].Nombre))

            dlg.Destroy()

    def OnGuardarPrograma(self,event):
        global NombreArchivo
        self.Guardar()
        self.Title = "Generador de Programas: " + NombreArchivo.split(os.sep)[-1]

    def OnGuardarComo( self, event ):
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

    def OnGenerar( self , event):
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
            archivobinario.flush()
            archivobinario.close()
        elif val == wx.ID_NO:

            self.Boton = wx.ID_NO

        else:

            self.Boton = wx.ID_CANCEL

    def Guardar(self):
        #TODO generar archivo como el anterior
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
                    global miBits
                    shelf["bits"] = miBits
                    global miBytes
                    shelf["bytes"] = miBytes
                    global miValoresEntradas
                    shelf["miValoresEntradas"] = miValoresEntradas
                    global miAnalogica
                    shelf["miAnalogica"] = miAnalogica
                    shelf["version"] = VERSION
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


    def CrearNuevoPrograma(self):
        global Modificado
        Modificado = False
        global NombreArchivo
        NombreArchivo = ""
        self.aplicaciones = []
        for i in range(Cantidad_Apps):
            self.aplicaciones.append(Aplicacion(i,""))
            self.AppMenuItems[i].SetText(\
                u"Aplicación %0.2d: %s"%(i,self.aplicaciones[i].Nombre))
        self.Title = "Generador de Programas: "
        global ValoresEntradas
        global miValoresEntradas
        miValoresEntradas = {}
        for i in ValoresEntradas.keys():
            miValoresEntradas[i] = ValoresEntradas[i][:]
        global Analogica
        global miAnalogica
        miAnalogica = {}
        for i in Analogica.keys():
            miAnalogica[i] = Analogica[i]




########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Editar Apps   #######################
##############                                   #######################
########################################################################
########################################################################


class mifrmEditApp(gui.frmEditApp):

    """Frame para editar una app, recibe la app a editar"""

    def __init__(self,parent,App):

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

    def OnChoiceEstadoInicial( self, event ):
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

    def OnEditarEstado( self, event ):
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

    def OnDuplicarEstado( self, event ):
        dlg = miDlgCopiarEstado(self)
        dlg.ShowModal()


    def OnEliminarEstado( self, event ):

        sel = self.listEstados.GetSelection()
        if sel != -1:
            self.Cambios = False
            self.tempApp.Estados[sel] = Estado()
            self.EstadosDic[sel].opened = False
            self.listEstados.Delete(sel)
            self.listEstados.Insert( "%0.2d :"%sel, sel )


    def OnEliminarApp( self, event ):

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


    def OnGuardarApp( self, event ):
        self.Guardar()

    def OnCambiarNombre( self, event ):
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

    def __init__( self, parent, numEstado):

        gui.frmBloques.__init__ ( self, parent)
        self.padre = parent
        self.notBloque.NumEstado = numEstado
        self.notBloque.Estado = self.padre.tempApp.Estados[numEstado].copy()
        self.notBloque.SCTotal = []
        self.Title = "Sin Nombre"
        self.notBloque.Modificado = False
        for i in range(Cantidad_Bloques):
            self.notBloque.SCTotal.append("")
            win = mipanelBloque( self.notBloque, i , self.padre )
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


    def OnGuardar( self, event ):
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


    def OnClose ( self , event ):

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


    def OnTitulo( self, event ):
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



    def OnChoiceAccion( self, event ):
        self.padre.Modificado = True
        self.txtctrlSeudo.SetValue("")
        self.Acciones.get(event.GetString())()


    def OnChoice( self, event ):
        self.ActualizarSeudoCodigo()

    def BloqueNull( self):
        self.choiceParametro1.Enable(False)
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(False)
        self.ActualizarSeudoCodigo()


    def BloqueIncrementar( self):
        self.choiceParametro1.SetItems(miBytes)
        self.choiceParametro2.SetItems(miBytes)
        self.choiceGuardar.SetItems(miBytes)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection( self.Guardar )


    def BloqueDecrementar( self):
        self.choiceParametro1.SetItems(miBytes)
        self.choiceParametro2.SetItems(miBytes)
        self.choiceGuardar.SetItems(miBytes)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection( self.Guardar )

    def BloqueAND( self):
        self.choiceParametro1.SetItems(miBits)
        self.choiceParametro2.SetItems(miBits)
        self.choiceGuardar.SetItems(miBits)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(True)
        self.choiceParametro2.SetSelection( self.Par2 )
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection( self.Guardar )

    def BloqueOR( self):
        self.choiceParametro1.SetItems(miBits)
        self.choiceParametro2.SetItems(miBits)
        self.choiceGuardar.SetItems(miBits)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(True)
        self.choiceParametro2.SetSelection( self.Par2 )
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection( self.Guardar )

    def BloqueNOT( self):
        self.choiceParametro1.SetItems(miBits)
        self.choiceGuardar.SetItems(miBits)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection( self.Guardar )

    def BloqueSumar( self):
        self.choiceParametro1.SetItems(miBytes)
        self.choiceParametro2.SetItems(miBytes)
        self.choiceGuardar.SetItems(miBytes)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(True)
        self.choiceParametro2.SetSelection( self.Par2 )
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection( self.Guardar )

    def BloqueRestar( self):
        self.choiceParametro1.SetItems(miBytes)
        self.choiceParametro2.SetItems(miBytes)
        self.choiceGuardar.SetItems(miBytes)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(True)
        self.choiceParametro2.SetSelection( self.Par2 )
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection( self.Guardar )

    def BloqueInvertir( self):
        self.choiceParametro1.SetItems(miBytes)
        #self.choiceParametro2.SetItems(miBytes)
        self.choiceGuardar.SetItems(miBytes)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection( self.Guardar )

    def BloqueTransmitir( self):
        self.choiceParametro1.SetItems(miBytes)
        self.choiceParametro2.SetItems(miBytes)
        self.choiceGuardar.SetItems(miBytes)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(True)
        self.choiceParametro2.SetSelection( self.Par2 )
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection( self.Guardar )

    def BloqueSetBit( self):
        self.choiceParametro1.SetItems(miBits)
        #self.choiceParametro2.SetItems(miBits)
        #self.choiceGuardar.SetItems(miBits)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(False)

    def BloqueClrBit( self):
        self.choiceParametro1.SetItems(miBits)
        #self.choiceParametro2.SetItems(miBits)
        #self.choiceGuardar.SetItems(miBits)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(False)

    def BloqueClrReg( self):
        self.choiceParametro1.SetItems(miBytes)
        #self.choiceParametro2.SetItems(miBytes)
        #self.choiceGuardar.SetItems(miBytes)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(False)


    def BloqueCopiar( self):
        self.choiceParametro1.SetItems(miBytes)
        #self.choiceParametro2.SetItems(miBytes)
        self.choiceGuardar.SetItems(miBytes)
        self.choiceParametro1.Enable(True)
        self.choiceParametro1.SetSelection( self.Par1 )
        self.choiceParametro2.Enable(False)
        self.choiceGuardar.Enable(True)
        self.choiceGuardar.SetSelection( self.Guardar )


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
        self.ValorBloque = ((Bloque_SetBit<<24)|\
            int(self.choiceParametro2.GetCurrentSelection()<<8))
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
    def __init__( self, parent , numero , frmEditApp):
        """ parent: frm padre, numero = numero de estado ,
        frmEditApp = frm que posee la app actual"""
        gui.panelCondicion.__init__ ( self, parent)
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
        print self.padre.Estado.Condiciones[0]
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


    def OnChoiceComparacion( self, event ):
        self.Acciones.get(event.GetString())()
        self.ActualizarSeudoCodigo()

    def OnChoice( self, event ):
        self.ActualizarSeudoCodigo()


    def OnEnterWindow( self, event ):
        self.ActualizarSeudoCodigo()


    def BloqueNull(self):
        #Deshabilito todos los choices
        self.choiceParametro1.Enable(False)
        self.choiceParametro2.Enable(False)
        self.choiceEstadoTrue.Enable(False)
        self.choiceEstadoFalse.Enable(False)


    def Mayor(self):
        self.choiceParametro1.SetItems(miBytes)
        self.choiceParametro1.SetSelection(0)
        self.choiceParametro2.SetItems(miBytes)
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
        self.choiceParametro1.SetItems(miBytes)
        self.choiceParametro1.SetSelection(0)
        self.choiceParametro2.SetItems(miBytes)
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
        self.choiceParametro1.SetItems(miBytes)
        self.choiceParametro1.SetSelection(0)
        self.choiceParametro2.SetItems(miBytes)
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
        self.choiceParametro1.SetItems(miBits)
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
        self.choiceParametro1.SetItems(miBits)
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
    def __init__( self, parent , item):
        gui.frmEntrada.__init__ ( self, parent )
        self.padre = parent
        self.item = item
        self.Title = self.Title + self.item.GetText()
        global miValoresEntradas
        self.muestras = miValoresEntradas[self.item.GetText()][0]
        self.tiempo = miValoresEntradas[self.item.GetText()][1]
        self.txtctrlMuestras.SetValue(str(self.muestras))
        self.txtctrlTiempo.SetValue(str(self.tiempo))


    def OnGuardar( self, event ):
        global miValoresEntradas
        self.muestras = self.txtctrlMuestras.GetValue()
        self.tiempo   = self.txtctrlTiempo.GetValue()
        miValoresEntradas[self.item.GetText()][0] = self.muestras
        miValoresEntradas[self.item.GetText()][1] = self.tiempo
        global Modificado
        Modificado = True

    def OnCerrar( self, event ):
        global miValoresEntradas
        self.item.Enable(True)
        self.Destroy()

    def OnCargarDefaults( self, event ):
        global miValoresEntradas
        global ValoresEntradas
        miValoresEntradas[self.item.GetText()] = ValoresEntradas[self.item.GetText()]
        self.muestras = miValoresEntradas[self.item.GetText()][0]
        self.tiempo = miValoresEntradas[self.item.GetText()][1]
        self.txtctrlMuestras.SetValue(str(self.muestras))
        self.txtctrlTiempo.SetValue(str(self.tiempo))

    def OnChar( self, event ):
        EsNumero ( event )



########################################################################
########################################################################
##############                                   #######################
##############   Edición del Diálogo Error       #######################
##############                                   #######################
########################################################################
########################################################################

class miDlgGenError (gui.DlgGenError):
    """Diálogo de error"""
    def __init__( self, parent ):
        gui.DlgGenError.__init__ ( self, parent)

    def OnAceptar( self, event ):
        self.Destroy()


########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Editar Bits   #######################
##############                                   #######################
########################################################################
########################################################################

class mifrmEditBit ( gui.frmEditBit ):
    """Frame para editar los nombres de los bits"""
    
    
    def __init__( self, parent, item):
        gui.frmEditBit.__init__ ( self, parent)
        self.item = item
        global miBits
        self.miBits = miBits[:]
        self.BitsTextCtrl = [] #lista con los wx.TextCtrl de edición de nombre de bit.
        for i,valorBit in enumerate(self.miBits):

            texto  = wx.StaticText( self.BitScroled, wx.ID_ANY, u"Bit Nº: %d"%i, wx.DefaultPosition, wx.DefaultSize, 0 )
            texto.Wrap( -1 )
            self.gridBotones.Add( texto, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
            # En Windows no se puede hacer wx.TextCtrl readonly luego\
            # de creado, por lo que debe hacerce cuando se crea:
            if isinstance(valorBit,tuple):
                textCtrl = wx.TextCtrl( self.BitScroled, wx.ID_ANY,\
                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,  wx.TE_READONLY )    
            else:
                textCtrl = wx.TextCtrl( self.BitScroled, wx.ID_ANY, \
                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )    
            self.gridBotones.Add( textCtrl, 0, wx.ALL|wx.ALIGN_LEFT, 5 ) 
            textCtrl.SetValue(valorBit[0])
            #staticline1 = wx.StaticLine( self.BitScroled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
            #self.gridBotones.Add( staticline1, 1, wx.ALL|wx.EXPAND, 5 )            
            self.BitsTextCtrl.append(textCtrl)

        self.BitScroled.SetSizer( self.gridBotones )
        self.BitScroled.Layout()
        self.BitScroled.SetAutoLayout(True)
        self.gridBotones.Fit( self.BitScroled )
    
    
    def OnModificarTexto ( self , event ):
        event.Skip()


    def OnBitSpinCtrl( self, event ):
        """ Function doc
        Carga el valor del vector de bits en el campo nombre
        @param PARAM: event
        @return RETURN: No
        """
        spin = self.BitsSpinCtrl.GetValue()
        self.BitsTxtCtrl.SetValue(self.miBits[spin][0])


    def OnEditBit( self, event ):
        """guarda los cambios realizados"""
        global miBits
        for i,txtctrl in enumerate(self.BitsTextCtrl):
            if txtctrl.IsModified():
                self.miBits[i][0] = txtctrl.GetValue()
                
        miBits = self.miBits[:]
        global Modificado
        Modificado = True


    def OnUndoBit( self, event ):
        global miBits
        self.miBits = miBits[:]
        for i,txtctrl in enumerate(self.BitsTextCtrl):
            txtctrl.SetValue(self.miBits[i][0])


    def OnClose(    self, event ):
        self.item.Enable(True)
        event.Skip()


class infoPopup(wx.PopupTransientWindow):
    """Adds a bit of text and mouse movement to the wx.PopupWindow"""
    def __init__(self, parent, style, log,text):
        wx.PopupTransientWindow.__init__(self, parent, style)
        self.log = log
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
    def __init__( self, parent, item ):
        gui.frmEditByte.__init__ ( self, parent)
        self.item = item
        global miBytes
        self.miBytes = miBytes[:]

    def OnByteSpinCtrl( self, event ):
        spin = self.BytesSpinCtrl.GetValue()
        self.BytesTxtCtrl.SetValue(self.miBytes[spin])
        pass

    def OnText(self,event):
        self.miBytes[self.BytesSpinCtrl.GetValue()] = self.BytesTxtCtrl.GetValue()

    def OnEditByte( self, event ):
        global miBytes
        miBytes = self.miBytes[:]
        global Modificado
        Modificado = True

    def OnUndoByte( self, event ):
        global miBytes
        self.miBytes = miBytes[:]
        self.BytesTxtCtrl.SetValue(self.miBytes[self.BytesSpinCtrl.GetValue()])

    def OnClose(    self, event ):
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


    def __init__( self, parent ):
        gui.DialogoCopiarApp.__init__ ( self, parent)
        self.padre = parent
        self.CargarChoices()

    def OnChoiceAppA( self, event ):
        sel = self.choiceAppA.GetSelection()
        if not self.padre.AppMenuItems[sel].IsEnabled():
            self.choiceAppA.SetSelection(-1)
            dlg = wx.MessageDialog(self, u"Cierre la Edición de esta aplicación\n"+\
                u"antes de copiarla",caption="Error al copiar",
                style=wx.OK, pos=wx.DefaultPosition)
            dlg.ShowModal()


    def OnChoiceAppB( self, event ):
        sel = self.choiceAppB.GetSelection()
        if not self.padre.AppMenuItems[sel].IsEnabled():
            self.choiceAppB.SetSelection(-1)
            dlg = wx.MessageDialog(self, u"Cierre la Edición de esta aplicación\n"+\
                u"antes de copiarla",caption="Error al copiar",
                style=wx.OK, pos=wx.DefaultPosition)
            dlg.ShowModal()


    def OnCopiar( self, event ):
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

    def OnCerrar( self, event ):
        self.Destroy()

    def CargarChoices(self):
        choices = []
        for i in self.padre.aplicaciones:
            choices.append("%0.2d: %s"%(i.AppNum,i.Nombre))
        self.choiceAppA.SetItems(choices)
        self.choiceAppB.SetItems(choices)


class miDlgCopiarEstado ( gui.DlgCopiarEstado ):
    """Copiar un estado a otro, copia todo menos el número de estado"""

    def __init__(self, parent):
        super(miDlgCopiarEstado,self).__init__(parent)
        self.padre = parent
        self.NumApp = parent.tempApp.AppNum
        self.CargarChoices()

    def OnCopiar( self, event ):
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

    def CargarChoices ( self ):
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

    def OnCerrar( self , event ):
        self.Destroy()


class mifrmAnalog ( gui.frmAnalog ):

    def __init__( self, parent ):
        gui.frmAnalog.__init__ ( self, parent)
        self.padre = parent
        global miAnalogica
        self.tempAnalogica = miAnalogica.copy()
        self.zonas = {\
            "Asup":[self.spinAsup,0],\
            "Ainf":[self.spinAinf,0],\
            "Bsup":[self.spinBsup,0],\
            "Binf":[self.spinBinf,0],\
            "Csup":[self.spinCsup,0],\
            "Cinf":[self.spinCinf,0],\
            "Dsup":[self.spinDsup,0],\
            "Dinf":[self.spinDinf,0]\
            }
        for zona in self.zonas.keys():
            self.zonas[zona][1] = self.tempAnalogica[zona]
        for zona in self.zonas.keys():
            self.zonas[zona][0].SetValue(\
                self.zonas[zona][1])
        self.txtctrlMuestras.SetValue(str(self.tempAnalogica["muestras"]))
        self.txtctrlTiempo.SetValue(str(self.tempAnalogica["tiempo"]))
        self.txtctrlComentarios.SetValue(self.tempAnalogica["comentarios"])
        self.cambios = False

    def On4zonas( self, event ):
        for zona in self.zonas.keys():
            self.zonas[zona][0].Enable(True)
        self.cambios = True
        self.radbtnValorADC.SetValue(False)
        #event.Skip()

    def OnValorADC( self, event ):
        for zona in self.zonas.keys():
            self.zonas[zona][0].Enable(False)
        self.cambios = True
        self.radbtn4zonas.SetValue(False)

    def OnGuardar( self, event ):
        self.Guardar()

    def Guardar(self):
        if not self.DatosValidos():
            dlg = wx.MessageDialog(self, u"Límites de zonas\nincorrectos",\
                caption="Error al guardar", style=wx.OK, pos=wx.DefaultPosition)
            dlg.ShowModal()
        else:
            global miAnalogica
            miAnalogica = self.tempAnalogica.copy()
            self.cambios = False
            self.leerDatos()
            global Modificado
            Modificado = True


    def OnCargarDefault( self, event ):
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

    def OnClose( self, event ):
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

    def OnInfo( self, event ):
        win = miFrameZonas(self)
        win.Show()

    def OnCambios (self, event):
        self.cambios = True
        event.Skip()

    def OnChar( self, event ):
        self.cambios = True
        EsNumero( event)

    def OnSpin ( self, event ):
        self.cambios = True
        event.Skip()

    def DatosValidos( self ):

        self.leerDatos()
        if ((self.zonas["Asup"][1]>self.zonas["Ainf"][1]) and\
            (self.zonas["Ainf"][1]>self.zonas["Bsup"][1]) and\
            (self.zonas["Bsup"][1]>self.zonas["Binf"][1]) and\
            (self.zonas["Binf"][1]>self.zonas["Csup"][1]) and\
            (self.zonas["Csup"][1]>self.zonas["Cinf"][1]) and\
            (self.zonas["Cinf"][1]>self.zonas["Dsup"][1]) and\
            (self.zonas["Dsup"][1]>self.zonas["Dinf"][1])):
            return True
        else:
            return False

    def leerDatos( self ):

        for zona in self.zonas.keys():
            valor = self.zonas[zona][0].GetValue()
            self.zonas[zona][1] = 0 if (valor == "") else int(valor)
            self.tempAnalogica[zona]=self.zonas[zona][1]

        tiempo = self.txtctrlTiempo.GetValue()
        self.tempAnalogica["tiempo"] = 0 if tiempo == "" else int(tiempo)

        muestras = self.txtctrlMuestras.GetValue()
        self.tempAnalogica["muestras"] = 0 if muestras == "" else int(muestras)

        self.tempAnalogica["modo"] = PorZonas if self.radbtn4zonas.IsEnabled()\
            else ValorADC

        self.tempAnalogica["comentarios"] = self.txtctrlComentarios.GetValue()

    def OnEnter( self , event):
        pass


class miFrameZonas(gui.FrameZonas):

    def __init__(self, parent):
        super(miFrameZonas, self).__init__(parent)

    def OnClose( self, event ):
        self.Destroy()

def EsNumero( event):

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
