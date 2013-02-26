#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generador.py
#
#  Copyright 2013 santiago <spaleka@cylgem.com.ar>
#

import gui
import wx
from apps import *

#Modulo para serialización de objetos python.
import shelve
shelf = shelve.open("generador.dat")
global miEstados
miEstados = Estados[:]
global miBits
miBits = Bits[:]
global miBytes
miBytes= Bytes[:]

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




class MiFrame(gui.frmPpal):
    """Frame principal"""
    def __init__(self):
        gui.frmPpal.__init__(self, None )
        self.programas = []
        #if shelf.has_key("programas"):
        #    self.programas = shelf["programas"]
        #self.numeroAppActual = 0
        self.AppMenuItems = {}
        for i in range(Cantidad_Apps):
            self.programas.append(Aplicacion(i,""))
#creo una copia de el diccionario Aplicación donde voy a trabajar
            self.programas[i].AppNum = i
            item = wx.MenuItem( self.m_programas, wx.ID_ANY, \
                u"Programa %0.2d: %s"%(i,self.programas[i].Nombre) ,\
                wx.EmptyString, wx.ITEM_NORMAL )
            self.m_programas.AppendItem(item)
            self.AppMenuItems[i] = item
            self.Bind ( wx.EVT_MENU, self.OnAbrirPrograma, id = item.GetId() )
            item.Enable ( True )
            boton = wx.Button( self.scroolled, wx.ID_ANY,\
                u"Aplicacion: %0.2d"%i, wx.DefaultPosition, wx.DefaultSize, 0 )
            self.sizerbotones.Add( boton, 0, wx.ALL, 5 )
            boton.Bind(wx.EVT_BUTTON, self.OnImprimirApp)
        item = wx.MenuItem( self.m_programas, wx.ID_ANY, u"Copiar Programa",\
            wx.EmptyString, wx.ITEM_NORMAL )
        self.m_programas.AppendItem(item)
        self.Bind ( wx.EVT_MENU, self.OnCopiarPrograma, id = item.GetId() )
        self.sizerbotones.Fit( self.scroolled )
        for i in Entradas:
            item = wx.MenuItem( self.m_drivers, wx.ID_ANY, i, wx.EmptyString, wx.ITEM_NORMAL )
            self.m_drivers.AppendItem( item )
            self.Bind( wx.EVT_MENU, self.OnDriver, id = item.GetId() )

    def DisableDriverSubMenu(self,elemento):
        pass

    def AgregarVentana(self):
        pass

    #funciones de eventos en frame principal

    def OnExit(self, evt):
        self.Close(True)

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
        for i in self.programas:
            print i

    def OnAbrirPrograma(self,event):
        id = event.GetId()
        item = self.GetMenuBar().FindItemById(id)
        for i in self.programas:
            if u"Programa %0.2d: %s"%(i.AppNum,i.Nombre) ==item.GetText():
                win = mifrmEditApp(self,i)
                win.Show(True)
                item.Enable(False)
                return

    def OnImprimirApp(self, event):
        boton = event.GetEventObject()
        numero = int(boton.GetLabel()[-2:])
        print u"\n\naplicación %d: %s"% (self.programas[numero].AppNum\
            ,self.programas[numero].Nombre)
        for i in range(Cantidad_Estados):
            print str(self.programas[numero].Estados[i].Nombre) + "\n"

    def OnCopiarPrograma(self, event):
        dlg = miDlgCopiarApp(self)
        dlg.ShowModal()




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

        gui.frmEditApp.__init__(self,parent)
        self.padre = parent
        self.tempApp = App.copy()
        # Crea una copia de la app actual
        # Para no sobreescribir los datos originales en caso de cancelar
        self.textoPrograma.SetLabel("Programa %d: "%self.tempApp.AppNum+self.tempApp.Nombre)
        self.SCTotal = []   # lista con el texto total de seudo código.
        self.Title = self.tempApp.Nombre
        self.EstadosDic = {}
        self.Cambios = False
        self.CargarLista()
        #cargar los estados en un diccionario

    #diccionario de lista de estados {0:{"nombre":nombre,"opened":False/True}}
    
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
            print "Borrando aplicación %d:"%sel
            self.tempApp.Estados[sel] = Estado()
            self.EstadosDic[sel].opened = False
            self.listEstados.Delete(sel)
            self.listEstados.Insert( "%0.2d :"%sel, sel )


    def OnEliminarPrograma( self, event ):

        dlg = wx.MessageDialog(self, u"Desea borrar la\nAplicación actual?",\
            caption="Borrar Aplicación",\
            style=wx.YES | wx.NO,\
            pos=wx.DefaultPosition)
        val = dlg.ShowModal()
        if val == wx.ID_YES:
            num = self.tempApp.AppNum
            self.tempApp = Aplicacion(num,"")
            self.padre.programas[num] = self.tempApp
            print u"Eliminada App: %d: %s"%\
                (self.tempApp.AppNum,self.tempApp.Nombre)
            self.padre.AppMenuItems[self.tempApp.AppNum].SetText(\
                u"Programa %0.2d: %s"%(self.tempApp.AppNum,self.tempApp.Nombre))
            self.padre.AppMenuItems[num].Enable()
            self.Destroy()


    def OnGuardarPrograma( self, event ):
        self.Guardar()

    def OnCambiarNombre( self, event ):
        self.Cambios = True
        text = self.tempApp.Nombre
        renamed = wx.GetTextFromUser('Renombrar Programa', 'Renombrar', text)
        if renamed != '':
            self.tempApp.Nombre = renamed
            #item = self.AppMenuItems[self.tempApp.AppNum]
            self.textoPrograma.SetLabel("Programa %d: "%self.tempApp.AppNum+renamed)


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


    def HacerEstadoNull(self,estado):
        pass
        #self.app.Estados
        #Aplicacion.Estados[estado] = \
         #   {"Bloques" : [0 for i in range(Cantidad_Bloques)],\
          #  "Condiciones" : [0,0,0],\
       #     "Resultados" : [0,0],\
        #    "Nombre" : "",\
         #   "Comentario" : ""}

    def Guardar(self):
        self.padre.programas[self.tempApp.AppNum] = self.tempApp.copy()
        self.padre.AppMenuItems[self.tempApp.AppNum].SetText(\
            u"Programa %0.2d: %s"%(self.tempApp.AppNum,self.tempApp.Nombre))
        self.Cambios = False



########################################################################
########################################################################
##############                                   #######################
##############   Edición del Frame Bloques       #######################
##############                                   #######################
########################################################################
########################################################################

class mifrmBloques( gui.frmBloques):

    def __init__( self, parent, numEstado):

        gui.frmBloques.__init__ ( self, parent)
        self.padre = parent
        self.notBloque.estado = numEstado
        self.Title = "Sin Nombre"
        self.notBloque.Modificado = False
        for i in range(Cantidad_Bloques):
            self.padre.SCTotal.append("")
            win = mipanelBloque( self.notBloque, i , self.padre )
            self.notBloque.AddPage(win,"Bloque: %d"%i)
        self.padre.SCTotal.append("")
        # la lista SCTotal tiene en total Cantidad_Bloques + 1 elementos.
        win = mipanelCondicion(self.notBloque,Cantidad_Bloques,self.padre)
        self.notBloque.AddPage(win,"Condicion")
        #Cargar el valor actual de el nombre del estado
        self.txtctrlTitulo.SetValue(\
            self.padre.tempApp.Estados[self.notBloque.estado].Nombre)
        self.txtctrlComentario.SetValue(\
            self.padre.tempApp.Estados[self.notBloque.estado].Comentario)


    def OnGuardar( self, event ):
        self.Guardar()


    def Guardar(self):

        #self.padre.tempApp.Estados[self.notBloque.estado] = \
        #    self.padre.tempApp.Estados[self.notBloque.estado].copy()
        #nombre del estado
        nombre = "%0.2d"%self.notBloque.estado + " : " + self.Title
        self.padre.EstadosDic[self.notBloque.estado].opened = True
        self.padre.listEstados.Delete(self.notBloque.estado)
        self.padre.listEstados.Insert(nombre, self.notBloque.estado)
        self.padre.EstadosDic[self.notBloque.estado].Nombre = self.Title
        self.padre.EstadosDic[self.notBloque.estado].opened = True
        self.notBloque.Modificado = False
        self.comentario = self.txtctrlComentario.GetValue()
        self.padre.tempApp.Estados[self.notBloque.estado].Comentario = self.comentario


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
        self.padre.EstadosDic[self.notBloque.estado].opened = False
        self.padre.EstadosDic[self.notBloque.estado].ventana = None
        self.Destroy()


    def OnTitulo( self, event ):
        self.notBloque.Modificado = True
        self.Title = self.txtctrlTitulo.GetValue()
        self.padre.tempApp.Estados[self.notBloque.estado].Nombre = self.Title

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
        self.ValorBloque = frmEditApp.tempApp.Estados[self.padre.estado].Bloques[numero]

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
        self.frmEditApp.SCTotal[self.numero] = \
            self.GeneradoresCodigo[GetTexto(self.choiceAccion)]()
        self.padre.Modificado = True
        #CARGA EL VALOR DEL BLOQUE
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
        #print "0x%X"%self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero]


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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
        return cadena

    def SCTransmitir(self):
        """Función encargada de generar el seudocódigo
        para la función transmitir
        """
        self.ValorBloque = ((Bloque_Transmitir_BB<<24)|\
            int(self.choiceGuardar.GetCurrentSelection()<<16)|\
            int(self.choiceParametro1.GetCurrentSelection())|\
            int(self.choiceParametro2.GetCurrentSelection()<<8))
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
        return None

    def SCSetBit(self):
        """Función encargada de generar el seudocódigo
        para la función set bit
        """
        cadena = GetTexto(self.choiceParametro1) + " = 1"
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_SetBit<<24)|\
            int(self.choiceParametro2.GetCurrentSelection()<<8))
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque

        return cadena

    def SCClrBit(self):
        """Función encargada de generar el seudocódigo
        para la función clr bit
        """
        cadena = GetTexto(self.choiceParametro1) + " = 0"
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_ClrBit<<24)|\
            int(self.choiceParametro1.GetCurrentSelection()))
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
        return cadena

    def SCClrReg(self):
        """Función encargada de generar el seudocódigo
        para la función clr reg
        """
        cadena = GetTexto(self.choiceParametro1) + " = 0"
        self.txtctrlSeudo.SetValue(cadena)
        self.ValorBloque = ((Bloque_ClrReg<<24)|\
            int(self.choiceParametro1.GetCurrentSelection()))
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Bloques[self.numero] = self.ValorBloque
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
        self.choiceEstadoFalse.Enable ( False )
        self.ValorCondiciones = [Condicion_NULL,0,0]
        self.ValorResultados = [0,0]
        #self.SCTotal = self.frmEditApp.SCTotal
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
            self.frmEditApp.tempApp.Estados[self.padre.estado].Condiciones[0]]]()

        self.choiceAccion.SetSelection (\
            frmEditApp.tempApp.Estados[self.padre.estado].Condiciones[0])
        self.choiceParametro1.SetSelection (\
            frmEditApp.tempApp.Estados[self.padre.estado].Condiciones[1])
        self.choiceParametro2.SetSelection (\
            frmEditApp.tempApp.Estados[self.padre.estado].Condiciones[2])
        self.choiceEstadoTrue.SetSelection (\
            frmEditApp.tempApp.Estados[self.padre.estado].Resultados[0])
        self.choiceEstadoFalse.SetSelection (\
            frmEditApp.tempApp.Estados[self.padre.estado].Resultados[1])

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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Condiciones = self.ValorCondiciones[:]
        self.frmEditApp.tempApp.Estados[self.padre.estado].Resultados = self.ValorResultados[:]
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Condiciones = self.ValorCondiciones[:]
        self.frmEditApp.tempApp.Estados[self.padre.estado].Resultados = self.ValorResultados[:]
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Condiciones = self.ValorCondiciones[:]
        self.frmEditApp.tempApp.Estados[self.padre.estado].Resultados = self.ValorResultados[:]
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Condiciones = self.ValorCondiciones[:]
        self.frmEditApp.tempApp.Estados[self.padre.estado].Resultados = self.ValorResultados[:]
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
        self.frmEditApp.tempApp.Estados[self.padre.estado].Condiciones = self.ValorCondiciones[:]
        self.frmEditApp.tempApp.Estados[self.padre.estado].Resultados = self.ValorResultados[:]
        return cadena

    def ActualizarSeudoCodigo(self):
        self.frmEditApp.SCTotal[self.numero] = self.GeneradoresCodigo[GetTexto(self.choiceAccion)]()
        self.padre.Modificado = True
        self.txtctrlSeudo.SetValue("")
        for i in range(len(self.frmEditApp.SCTotal)-1):
            if self.frmEditApp.SCTotal[i]:
                self.txtctrlSeudo.AppendText("Bloque "+str(i)+": \n\t"+ \
                    self.frmEditApp.SCTotal[i] + "\n\n")
        if self.frmEditApp.SCTotal[-1]:
            self.txtctrlSeudo.AppendText("Condicion: \n" +\
                self.frmEditApp.SCTotal[-1])


    def OnChoiceComparacion( self, event ):
        self.Acciones.get(event.GetString())()
        self.ActualizarSeudoCodigo()

    def OnChoice( self, event ):
        self.ActualizarSeudoCodigo()


    def OnEnterWindow( self, event ):
        self.txtctrlSeudo.SetValue("")
        for i in range(len(self.frmEditApp.SCTotal)-1):
            if self.frmEditApp.SCTotal[i]:
                self.txtctrlSeudo.AppendText("Bloque "+str(i)+": \n\t"+ \
                    self.frmEditApp.SCTotal[i] + "\n\n")
        if self.frmEditApp.SCTotal[-1]:
            self.txtctrlSeudo.AppendText(u"Condición: \n" + self.frmEditApp.SCTotal[-1])


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

    def OnBitSpinCtrl( self, event ):
        """ Function doc
        Carga el valor del vector de bits en el campo nombre
        @param PARAM: event
        @return RETURN: No
        """
        spin = self.BitsSpinCtrl.GetValue()
        self.BitsTxtCtrl.SetValue(self.miBits[spin])

    def OnText(self,event):
        """ Function doc
        Carga el valor ingresado (String) en el vector de bis
        @param PARAM: event
        @return RETURN: No
        """
        self.miBits[self.BitsSpinCtrl.GetValue()] = self.BitsTxtCtrl.GetValue()

    def OnEditBit( self, event ):
        global miBits
        miBits = self.miBits[:]

    def OnUndoBit( self, event ):
        global miBits
        self.miBits = miBits[:]
        self.BitsTxtCtrl.SetValue(self.miBits[self.BitsSpinCtrl.GetValue()])

    def OnClose(    self, event ):
        self.item.Enable(True)
        event.Skip()


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
            num = self.padre.programas[selA].AppNum
            self.padre.programas[selA] = self.padre.programas[selB].copy()
            self.padre.programas[selA].AppNum = num
            self.padre.AppMenuItems[num].SetText(u"Programa %0.2d: %s"%(num,self.padre.programas[selA].Nombre))
            self.txtctrlCopia.AppendText("Copiado %s en %s\n"%(selB,selA))
            self.CargarChoices()
          
    def OnCerrar( self, event ):
        self.Destroy()
    
    def CargarChoices(self):
        choices = []
        for i in self.padre.programas:
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
        global miAnalogica
        self.Asup = miAnalogica["Asup"]
        self.Bsup = miAnalogica["Bsup"]
        self.Csup = miAnalogica["Csup"]
        self.Dsup = miAnalogica["Dsup"]
        self.Ainf = miAnalogica["Ainf"]
        self.Binf = miAnalogica["Binf"]
        self.Cinf = miAnalogica["Cinf"]
        self.Dinf = miAnalogica["Dinf"]
        self.txtctrlAsup.SetValue(str(self.Asup))
        self.txtctrlBsup.SetValue(str(self.Bsup))
        self.txtctrlCsup.SetValue(str(self.Csup))
        self.txtctrlDsup.SetValue(str(self.Dsup))
        self.txtctrlAinf.SetValue(str(self.Ainf))
        self.txtctrlBinf.SetValue(str(self.Binf))
        self.txtctrlCinf.SetValue(str(self.Cinf))
        self.txtctrlDinf.SetValue(str(self.Dinf))

    def On4zonas( self, event ):
        event.Skip()
    
    def OnValorADC( self, event ):
        event.Skip()
    
    def OnGuardar( self, event ):
        event.Skip()
    
    def OnCargarDefault( self, event ):
        event.Skip()
    
    def OnCerrar( self, event ):
        event.Skip()
      
    def OnInfo( self, event ):
        win = miFrameZonas(self)
        win.Show()
    
    def OnChar( self, event ):
        EsNumero( event)
    
    def OnKillFocus ( self, event):
        txtctrl = event.GetEventObject()
        texto = int(txtctrl.GetString(0,-1))
        if texto > 100:
            dlg = wx.MessageDialog(self, u"Insertar valor entre 0 y 100",\
                caption="Editar nivel",\
                pos=wx.DefaultPosition)
            dlg.ShowModal()
            txtctrl.SetFocus()
            txtctrl.SetValue("")
            print texto
        
    def OnEnter( self , event):
        numero = event.GetString()
        print numero
        
        if int(numero)<100:
            event.Skip()
            

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
shelf.close()
