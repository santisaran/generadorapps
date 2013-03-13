# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Apr 10 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frmPpal
###########################################################################

class frmPpal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generador de Programas: ", pos = wx.DefaultPosition, size = wx.Size( 597,496 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menubar1.SetExtraStyle( wx.WS_EX_BLOCK_EVENTS )
		
		self.m_archivo = wx.Menu()
		self.m_file_nuevoPrograma = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Nuevo Programa"+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.m_file_nuevoPrograma )
		
		self.m_file_abrirPrograma = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Abrir Programa"+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.m_file_abrirPrograma )
		
		self.m_file_guardarPrograma = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Guardar Programa"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.m_file_guardarPrograma )
		
		self.m_file_guardarComo = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Guardar Programa Como", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.m_file_guardarComo )
		
		self.m_archivo.AppendSeparator()
		
		self.m_file_gen = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Generar archivo Cyloc", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.m_file_gen )
		
		self.m_archivo.AppendSeparator()
		
		self.OnClose = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Salir"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.OnClose )
		
		self.m_menubar1.Append( self.m_archivo, u"&Archivo" ) 
		
		self.m_variables = wx.Menu()
		self.m_variables_Byte = wx.MenuItem( self.m_variables, wx.ID_ANY, u"Editar Variables Byte", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_variables.AppendItem( self.m_variables_Byte )
		
		self.m_variables_bit = wx.MenuItem( self.m_variables, wx.ID_ANY, u"Editar variables Bit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_variables.AppendItem( self.m_variables_bit )
		
		self.mVariablesSMS = wx.MenuItem( self.m_variables, wx.ID_ANY, u"Editar Mensajes de Texto", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_variables.AppendItem( self.mVariablesSMS )
		
		self.m_menubar1.Append( self.m_variables, u"Va&riables" ) 
		
		self.m_aplicaciones = wx.Menu()
		self.m_menubar1.Append( self.m_aplicaciones, u"A&plicaciones" ) 
		
		self.m_drivers = wx.Menu()
		self.m_drivers_analog = wx.MenuItem( self.m_drivers, wx.ID_ANY, u"Entrada Analógica", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_drivers.AppendItem( self.m_drivers_analog )
		
		self.m_menubar1.Append( self.m_drivers, u"&Drivers" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button22 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button22.Hide()
		
		bSizer32.Add( self.m_button22, 0, wx.ALL, 5 )
		
		self.scroolled = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.scroolled.SetScrollRate( 5, 5 )
		self.sizerbotones = wx.GridSizer( 0, 2, 0, 0 )
		
		
		self.scroolled.SetSizer( self.sizerbotones )
		self.scroolled.Layout()
		self.sizerbotones.Fit( self.scroolled )
		bSizer32.Add( self.scroolled, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer32 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnCerrar )
		self.Bind( wx.EVT_MENU, self.OnNuevoPrograma, id = self.m_file_nuevoPrograma.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAbrirPrograma, id = self.m_file_abrirPrograma.GetId() )
		self.Bind( wx.EVT_MENU, self.OnGuardarPrograma, id = self.m_file_guardarPrograma.GetId() )
		self.Bind( wx.EVT_MENU, self.OnGuardarComo, id = self.m_file_guardarComo.GetId() )
		self.Bind( wx.EVT_MENU, self.OnGenerar, id = self.m_file_gen.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCerrar, id = self.OnClose.GetId() )
		self.Bind( wx.EVT_MENU, self.OnEditarBytes, id = self.m_variables_Byte.GetId() )
		self.Bind( wx.EVT_MENU, self.OnEditarBit, id = self.m_variables_bit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnEditarSMS, id = self.mVariablesSMS.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDriverAnalog, id = self.m_drivers_analog.GetId() )
		self.m_button22.Bind( wx.EVT_BUTTON, self.OnTest )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCerrar( self, event ):
		event.Skip()
	
	def OnNuevoPrograma( self, event ):
		event.Skip()
	
	def OnAbrirPrograma( self, event ):
		event.Skip()
	
	def OnGuardarPrograma( self, event ):
		event.Skip()
	
	def OnGuardarComo( self, event ):
		event.Skip()
	
	def OnGenerar( self, event ):
		event.Skip()
	
	
	def OnEditarBytes( self, event ):
		event.Skip()
	
	def OnEditarBit( self, event ):
		event.Skip()
	
	def OnEditarSMS( self, event ):
		event.Skip()
	
	def OnDriverAnalog( self, event ):
		event.Skip()
	
	def OnTest( self, event ):
		event.Skip()
	

###########################################################################
## Class frmEditBit
###########################################################################

class frmEditBit ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Editar variables  Bits", pos = wx.DefaultPosition, size = wx.Size( 441,392 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.BitScroled = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.BitScroled.SetScrollRate( 5, 5 )
		self.gridBotones = wx.FlexGridSizer( 0, 2, 0, 1 )
		self.gridBotones.SetFlexibleDirection( wx.BOTH )
		self.gridBotones.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		self.BitScroled.SetSizer( self.gridBotones )
		self.BitScroled.Layout()
		self.gridBotones.Fit( self.BitScroled )
		bSizer30.Add( self.BitScroled, 1, wx.EXPAND |wx.ALL, 0 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Actualizar cambios", wx.Point( 0,1 ), wx.DefaultSize, 0 )
		bSizer31.Add( self.m_button15, 1, wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Deshacer cambios", wx.Point( 1,1 ), wx.DefaultSize, 0 )
		bSizer31.Add( self.m_button16, 1, wx.ALL, 5 )
		
		
		bSizer30.Add( bSizer31, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer30 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button15.Bind( wx.EVT_BUTTON, self.OnEditBit )
		self.m_button16.Bind( wx.EVT_BUTTON, self.OnUndoBit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnEditBit( self, event ):
		event.Skip()
	
	def OnUndoBit( self, event ):
		event.Skip()
	

###########################################################################
## Class frmEditByte
###########################################################################

class frmEditByte ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 522,397 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		self.ByteScroled = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.ByteScroled.SetScrollRate( 5, 5 )
		self.gridBotones = wx.FlexGridSizer( 0, 2, 0, 0 )
		self.gridBotones.SetFlexibleDirection( wx.BOTH )
		self.gridBotones.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		self.ByteScroled.SetSizer( self.gridBotones )
		self.ByteScroled.Layout()
		self.gridBotones.Fit( self.ByteScroled )
		bSizer32.Add( self.ByteScroled, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.frmEditByte_btn_Actualizar = wx.Button( self, wx.ID_ANY, u"Actualizar cambios", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.frmEditByte_btn_Actualizar, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.frmEditByte_btn_Deshacer = wx.Button( self, wx.ID_ANY, u"Deshacer cambios", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.frmEditByte_btn_Deshacer, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer32.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer32 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.frmEditByte_btn_Actualizar.Bind( wx.EVT_BUTTON, self.OnEditByte )
		self.frmEditByte_btn_Deshacer.Bind( wx.EVT_BUTTON, self.OnUndoByte )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnEditByte( self, event ):
		event.Skip()
	
	def OnUndoByte( self, event ):
		event.Skip()
	

###########################################################################
## Class frmEditApp 
###########################################################################

class frmEditApp  ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Editar Aplicación", pos = wx.DefaultPosition, size = wx.Size( 553,418 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Datos de la aplicación" ), wx.VERTICAL )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.textoPrograma = wx.StaticText( self, wx.ID_ANY, u"Aplicación: ", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.textoPrograma.Wrap( -1 )
		gSizer5.Add( self.textoPrograma, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.frm_edit_btn_Nombre = wx.Button( self, wx.ID_ANY, u"Cambiar Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.frm_edit_btn_Nombre, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Estado Inicial", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		gSizer5.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		choiceEstadoInicialChoices = []
		self.choiceEstadoInicial = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceEstadoInicialChoices, 0 )
		self.choiceEstadoInicial.SetSelection( 0 )
		gSizer5.Add( self.choiceEstadoInicial, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer16.Add( gSizer5, 0, wx.EXPAND, 5 )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Lista de Estados" ), wx.VERTICAL )
		
		listEstadosChoices = []
		self.listEstados = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listEstadosChoices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
		sbSizer15.Add( self.listEstados, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.frm_edit_btn_editarestado = wx.Button( self, wx.ID_ANY, u"&Editar Estado", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer30.Add( self.frm_edit_btn_editarestado, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.frm_edit_btn_copiarestado = wx.Button( self, wx.ID_ANY, u"C&opiar Estado", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer30.Add( self.frm_edit_btn_copiarestado, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.frm_edit_btn_delestado = wx.Button( self, wx.ID_ANY, u"Eliminar Estado", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer30.Add( self.frm_edit_btn_delestado, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )
		
		
		sbSizer15.Add( bSizer30, 0, wx.EXPAND, 5 )
		
		
		sbSizer16.Add( sbSizer15, 1, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.frm_edit_btn_delapp = wx.Button( self, wx.ID_ANY, u"Eliminar Aplicación", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.frm_edit_btn_delapp, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer26.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.frm_edit_btn_guardarapp = wx.Button( self, wx.ID_ANY, u"&Guardar aplicación", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.frm_edit_btn_guardarapp, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.frm_edit_btn_cerrar = wx.Button( self, wx.ID_ANY, u"&Cerrar", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer26.Add( self.frm_edit_btn_cerrar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		sbSizer16.Add( bSizer26, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer4.Add( sbSizer16, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.frm_edit_btn_Nombre.Bind( wx.EVT_BUTTON, self.OnCambiarNombre )
		self.choiceEstadoInicial.Bind( wx.EVT_CHOICE, self.OnChoiceEstadoInicial )
		self.listEstados.Bind( wx.EVT_LISTBOX_DCLICK, self.OnEditarEstado )
		self.frm_edit_btn_editarestado.Bind( wx.EVT_BUTTON, self.OnEditarEstado )
		self.frm_edit_btn_copiarestado.Bind( wx.EVT_BUTTON, self.OnDuplicarEstado )
		self.frm_edit_btn_delestado.Bind( wx.EVT_BUTTON, self.OnEliminarEstado )
		self.frm_edit_btn_delapp.Bind( wx.EVT_BUTTON, self.OnEliminarApp )
		self.frm_edit_btn_guardarapp.Bind( wx.EVT_BUTTON, self.OnGuardarApp )
		self.frm_edit_btn_cerrar.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnCambiarNombre( self, event ):
		event.Skip()
	
	def OnChoiceEstadoInicial( self, event ):
		event.Skip()
	
	def OnEditarEstado( self, event ):
		event.Skip()
	
	
	def OnDuplicarEstado( self, event ):
		event.Skip()
	
	def OnEliminarEstado( self, event ):
		event.Skip()
	
	def OnEliminarApp( self, event ):
		event.Skip()
	
	def OnGuardarApp( self, event ):
		event.Skip()
	
	

###########################################################################
## Class DialogoCopiarApp
###########################################################################

class DialogoCopiarApp ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Copiar Programas", pos = wx.DefaultPosition, size = wx.Size( 340,170 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Copia:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer27.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		choiceAppAChoices = []
		self.choiceAppA = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceAppAChoices, 0 )
		self.choiceAppA.SetSelection( 0 )
		bSizer28.Add( self.choiceAppA, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer28.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		choiceAppBChoices = []
		self.choiceAppB = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceAppBChoices, 0 )
		self.choiceAppB.SetSelection( 0 )
		bSizer28.Add( self.choiceAppB, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer27.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		self.txtctrlCopia = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer27.Add( self.txtctrlCopia, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Copiar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer29.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnCerrar = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.btnCerrar, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer29, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer27 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnCerrar )
		self.choiceAppA.Bind( wx.EVT_CHOICE, self.OnChoiceAppA )
		self.choiceAppB.Bind( wx.EVT_CHOICE, self.OnChoiceAppB )
		self.m_button24.Bind( wx.EVT_BUTTON, self.OnCopiar )
		self.btnCerrar.Bind( wx.EVT_BUTTON, self.OnCerrar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCerrar( self, event ):
		event.Skip()
	
	def OnChoiceAppA( self, event ):
		event.Skip()
	
	def OnChoiceAppB( self, event ):
		event.Skip()
	
	def OnCopiar( self, event ):
		event.Skip()
	
	

###########################################################################
## Class DlgCopiarEstado
###########################################################################

class DlgCopiarEstado ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Copiar Estado", pos = wx.DefaultPosition, size = wx.Size( 340,170 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Copia:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer27.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		choiceEstAChoices = []
		self.choiceEstA = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceEstAChoices, 0 )
		self.choiceEstA.SetSelection( 0 )
		bSizer28.Add( self.choiceEstA, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer28.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		choiceEstBChoices = []
		self.choiceEstB = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceEstBChoices, 0 )
		self.choiceEstB.SetSelection( 0 )
		bSizer28.Add( self.choiceEstB, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer27.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		self.txtctrlCopia = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer27.Add( self.txtctrlCopia, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCopiar = wx.Button( self, wx.ID_ANY, u"Copiar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.btnCopiar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer29.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnCerrar = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.btnCerrar, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer29, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer27 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnCerrar )
		self.choiceEstA.Bind( wx.EVT_CHOICE, self.OnChoiceAppA )
		self.choiceEstB.Bind( wx.EVT_CHOICE, self.OnChoiceAppB )
		self.btnCopiar.Bind( wx.EVT_BUTTON, self.OnCopiar )
		self.btnCerrar.Bind( wx.EVT_BUTTON, self.OnCerrar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCerrar( self, event ):
		event.Skip()
	
	def OnChoiceAppA( self, event ):
		event.Skip()
	
	def OnChoiceAppB( self, event ):
		event.Skip()
	
	def OnCopiar( self, event ):
		event.Skip()
	
	

###########################################################################
## Class frmBloques
###########################################################################

class frmBloques ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edición de Bloques de un estado", pos = wx.DefaultPosition, size = wx.Size( 725,320 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.notBloque = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizer18.Add( self.notBloque, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"Estado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		bSizer29.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_button27 = wx.Button( self, wx.ID_ANY, u"Guardar Estado", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button27, 0, wx.ALL, 5 )
		
		self.m_button28 = wx.Button( self, wx.ID_ANY, u"Descartar Cambios", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button28, 0, wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Título", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer29.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.txtctrlTitulo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer29.Add( self.txtctrlTitulo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Comentario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		bSizer29.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.txtctrlComentario = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer29.Add( self.txtctrlComentario, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer18.Add( bSizer29, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer18 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button27.Bind( wx.EVT_BUTTON, self.OnGuardar )
		self.m_button28.Bind( wx.EVT_BUTTON, self.OnClose )
		self.txtctrlTitulo.Bind( wx.EVT_TEXT, self.OnTitulo )
		self.txtctrlTitulo.Bind( wx.EVT_TEXT_ENTER, self.OnTitulo )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnGuardar( self, event ):
		event.Skip()
	
	
	def OnTitulo( self, event ):
		event.Skip()
	
	

###########################################################################
## Class panelBloque
###########################################################################

class panelBloque ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,357 ), style = wx.TAB_TRAVERSAL )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Acción" ), wx.VERTICAL )
		
		choiceAccionChoices = []
		self.choiceAccion = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceAccionChoices, 0 )
		self.choiceAccion.SetSelection( 0 )
		sbSizer2.Add( self.choiceAccion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer21.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Parámetro 1" ), wx.VERTICAL )
		
		choiceParametro1Choices = []
		self.choiceParametro1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceParametro1Choices, 0 )
		self.choiceParametro1.SetSelection( 0 )
		self.choiceParametro1.Enable( False )
		
		sbSizer6.Add( self.choiceParametro1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer21.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Parámetro 2" ), wx.VERTICAL )
		
		choiceParametro2Choices = []
		self.choiceParametro2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceParametro2Choices, 0 )
		self.choiceParametro2.SetSelection( 0 )
		self.choiceParametro2.Enable( False )
		
		sbSizer8.Add( self.choiceParametro2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer21.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Guardar en:" ), wx.VERTICAL )
		
		choiceGuardarChoices = []
		self.choiceGuardar = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceGuardarChoices, 0 )
		self.choiceGuardar.SetSelection( 0 )
		self.choiceGuardar.Enable( False )
		
		sbSizer9.Add( self.choiceGuardar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer21.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer20.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Seudocódigo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		bSizer22.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.txtctrlSeudo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer22.Add( self.txtctrlSeudo, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer20.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer20 )
		self.Layout()
		
		# Connect Events
		self.choiceAccion.Bind( wx.EVT_CHOICE, self.OnChoiceAccion )
		self.choiceParametro1.Bind( wx.EVT_CHOICE, self.OnChoice )
		self.choiceParametro2.Bind( wx.EVT_CHOICE, self.OnChoice )
		self.choiceGuardar.Bind( wx.EVT_CHOICE, self.OnChoice )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnChoiceAccion( self, event ):
		event.Skip()
	
	def OnChoice( self, event ):
		event.Skip()
	
	
	

###########################################################################
## Class panelCondicion
###########################################################################

class panelCondicion ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,363 ), style = wx.TAB_TRAVERSAL )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Comparación" ), wx.VERTICAL )
		
		choiceAccionChoices = [ u"Null", u"Mayor", u"Menor", u"==", u"Bit 1", u"Bit 0?", u"Bit 1?" ]
		self.choiceAccion = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceAccionChoices, 0 )
		self.choiceAccion.SetSelection( 1 )
		sbSizer10.Add( self.choiceAccion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer24.Add( sbSizer10, 1, wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Parámetro 1" ), wx.VERTICAL )
		
		choiceParametro1Choices = []
		self.choiceParametro1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceParametro1Choices, 0 )
		self.choiceParametro1.SetSelection( 0 )
		self.choiceParametro1.Enable( False )
		
		sbSizer11.Add( self.choiceParametro1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer24.Add( sbSizer11, 1, wx.EXPAND, 5 )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Parámetro 2" ), wx.VERTICAL )
		
		choiceParametro2Choices = []
		self.choiceParametro2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceParametro2Choices, 0 )
		self.choiceParametro2.SetSelection( 0 )
		self.choiceParametro2.Enable( False )
		
		sbSizer12.Add( self.choiceParametro2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer24.Add( sbSizer12, 1, wx.EXPAND, 5 )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Estado Siguiente Si Verdadero" ), wx.VERTICAL )
		
		choiceEstadoTrueChoices = [ u"Estado0", u"Estado1", u"Estado2", u"Estado3", u"Estado4", u"Estado5", u"Estado6", u"Estado7", u"Estado8", u"Estado9" ]
		self.choiceEstadoTrue = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceEstadoTrueChoices, 0 )
		self.choiceEstadoTrue.SetSelection( 0 )
		self.choiceEstadoTrue.Enable( False )
		
		sbSizer13.Add( self.choiceEstadoTrue, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer24.Add( sbSizer13, 1, wx.EXPAND, 5 )
		
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Estado Siguiente si Falso" ), wx.VERTICAL )
		
		choiceEstadoFalseChoices = [ u"Estado0", u"Estado1", u"Estado2", u"Estado3", u"Estado4", u"Estado5", u"Estado6", u"Estado7", u"Estado8", u"Estado9" ]
		self.choiceEstadoFalse = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceEstadoFalseChoices, 0 )
		self.choiceEstadoFalse.SetSelection( 0 )
		self.choiceEstadoFalse.Enable( False )
		
		sbSizer14.Add( self.choiceEstadoFalse, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer24.Add( sbSizer14, 1, wx.EXPAND, 5 )
		
		
		bSizer23.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.txtctrlSeudo = wx.StaticText( self, wx.ID_ANY, u"Seudocódigo Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtctrlSeudo.Wrap( -1 )
		bSizer25.Add( self.txtctrlSeudo, 0, wx.ALL, 5 )
		
		self.txtctrlSeudo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer25.Add( self.txtctrlSeudo, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer23.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer23 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_ENTER_WINDOW, self.OnEnterWindow )
		self.choiceAccion.Bind( wx.EVT_CHOICE, self.OnChoiceComparacion )
		self.choiceParametro1.Bind( wx.EVT_CHOICE, self.OnChoice )
		self.choiceParametro2.Bind( wx.EVT_CHOICE, self.OnChoice )
		self.choiceEstadoTrue.Bind( wx.EVT_CHOICE, self.OnChoice )
		self.choiceEstadoFalse.Bind( wx.EVT_CHOICE, self.OnChoice )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnEnterWindow( self, event ):
		event.Skip()
	
	def OnChoiceComparacion( self, event ):
		event.Skip()
	
	def OnChoice( self, event ):
		event.Skip()
	
	
	
	

###########################################################################
## Class frmEntrada
###########################################################################

class frmEntrada ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 438,131 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer26.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"Cantidad de muestras para validar cambio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		bSizer26.Add( self.m_staticText48, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtctrlMuestras = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.txtctrlMuestras, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer26, 0, wx.EXPAND, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer28.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Tiempo de muestreo [ms]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		bSizer28.Add( self.m_staticText49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtctrlTiempo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.txtctrlTiempo, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_guardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.btn_guardar, 1, wx.ALL, 5 )
		
		self.btn_cerrar = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.btn_cerrar, 1, wx.ALL, 5 )
		
		self.btn_cargar = wx.Button( self, wx.ID_ANY, u"Cargar Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.btn_cargar, 1, wx.ALL, 5 )
		
		
		bSizer29.Add( bSizer30, 1, wx.EXPAND, 5 )
		
		
		bSizer25.Add( bSizer29, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer25 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnCerrar )
		self.txtctrlMuestras.Bind( wx.EVT_CHAR, self.OnChar )
		self.txtctrlTiempo.Bind( wx.EVT_CHAR, self.OnChar )
		self.btn_guardar.Bind( wx.EVT_BUTTON, self.OnGuardar )
		self.btn_cerrar.Bind( wx.EVT_BUTTON, self.OnCerrar )
		self.btn_cargar.Bind( wx.EVT_BUTTON, self.OnCargarDefaults )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCerrar( self, event ):
		event.Skip()
	
	def OnChar( self, event ):
		event.Skip()
	
	
	def OnGuardar( self, event ):
		event.Skip()
	
	
	def OnCargarDefaults( self, event ):
		event.Skip()
	

###########################################################################
## Class DlgGenError
###########################################################################

class DlgGenError ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generador", pos = wx.DefaultPosition, size = wx.Size( 202,122 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"Nombre no Válido", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText63.Wrap( -1 )
		bSizer61.Add( self.m_staticText63, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALL, 5 )
		
		self.m_button48 = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.m_button48, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer61 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button48.Bind( wx.EVT_BUTTON, self.OnAceptar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnAceptar( self, event ):
		event.Skip()
	

###########################################################################
## Class frmAnalog
###########################################################################

class frmAnalog ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuración entrada analógica", pos = wx.DefaultPosition, size = wx.Size( 550,408 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Modo de funcionamiento" ), wx.VERTICAL )
		
		self.radbtn4zonas = wx.RadioButton( self, wx.ID_ANY, u"Utilizar 4 zonas", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.radbtn4zonas, 0, wx.ALL, 5 )
		
		self.radbtnValorADC = wx.RadioButton( self, wx.ID_ANY, u"Obtener valor ADC", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.radbtnValorADC, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( sbSizer12, 0, wx.EXPAND|wx.ALL, 5 )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Configuración Zonas" ), wx.VERTICAL )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Límite superior zona A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer3.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinAsup = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		self.spinAsup.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		gSizer3.Add( self.spinAsup, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Límite inferior zona A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer3.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinAinf = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		self.spinAinf.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.spinAinf.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		self.spinAinf.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.spinAinf, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Límite superior zona B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer3.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinBsup = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer3.Add( self.spinBsup, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Límite inferior zona B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer3.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinBinf = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer3.Add( self.spinBinf, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Límite superior zona C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer3.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCsup = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer3.Add( self.spinCsup, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Límite inferior zona C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer3.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCinf = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer3.Add( self.spinCinf, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Límite superior zona D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer3.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinDsup = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer3.Add( self.spinDsup, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Límite inferior zona D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer3.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinDinf = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer3.Add( self.spinDinf, 0, wx.ALL, 5 )
		
		
		sbSizer13.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		self.btnInformacion = wx.Button( self, wx.ID_ANY, u"Información", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer13.Add( self.btnInformacion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer5.Add( sbSizer13, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Configuración General", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer7.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Tiempo de muestreo[ms]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gSizer5.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.txtctrlTiempo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.txtctrlTiempo, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Cantidad de muestras\npara validar zona", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		gSizer5.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.txtctrlMuestras = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.txtctrlMuestras, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		
		bSizer7.Add( gSizer5, 0, wx.EXPAND, 5 )
		
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Comentario" ), wx.VERTICAL )
		
		self.txtctrlComentarios = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizer14.Add( self.txtctrlComentarios, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( sbSizer14, 1, wx.EXPAND, 5 )
		
		self.frm_analog_btnGuardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.frm_analog_btnGuardar, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.frm_analog_btnCargarDefault = wx.Button( self, wx.ID_ANY, u"Cargar Default", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.frm_analog_btnCargarDefault, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.frm_analog_btnCerrar = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.frm_analog_btnCerrar, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.radbtn4zonas.Bind( wx.EVT_RADIOBUTTON, self.On4zonas )
		self.radbtnValorADC.Bind( wx.EVT_RADIOBUTTON, self.OnValorADC )
		self.spinAsup.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocus )
		self.spinAsup.Bind( wx.EVT_SPINCTRL, self.OnSpin )
		self.spinAinf.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocus )
		self.spinAinf.Bind( wx.EVT_SPINCTRL, self.OnSpin )
		self.spinBsup.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocus )
		self.spinBsup.Bind( wx.EVT_SPINCTRL, self.OnSpin )
		self.spinBinf.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocus )
		self.spinBinf.Bind( wx.EVT_SPINCTRL, self.OnSpin )
		self.spinCsup.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocus )
		self.spinCsup.Bind( wx.EVT_SPINCTRL, self.OnSpin )
		self.spinCinf.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocus )
		self.spinCinf.Bind( wx.EVT_SPINCTRL, self.OnSpin )
		self.spinDsup.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocus )
		self.spinDsup.Bind( wx.EVT_SPINCTRL, self.OnSpin )
		self.spinDinf.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocus )
		self.spinDinf.Bind( wx.EVT_SPINCTRL, self.OnSpin )
		self.btnInformacion.Bind( wx.EVT_BUTTON, self.OnInfo )
		self.txtctrlTiempo.Bind( wx.EVT_CHAR, self.OnChar )
		self.txtctrlMuestras.Bind( wx.EVT_CHAR, self.OnChar )
		self.txtctrlComentarios.Bind( wx.EVT_CHAR, self.OnCambios )
		self.frm_analog_btnGuardar.Bind( wx.EVT_BUTTON, self.OnGuardar )
		self.frm_analog_btnCargarDefault.Bind( wx.EVT_BUTTON, self.OnCargarDefault )
		self.frm_analog_btnCerrar.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def On4zonas( self, event ):
		event.Skip()
	
	def OnValorADC( self, event ):
		event.Skip()
	
	def OnKillFocus( self, event ):
		event.Skip()
	
	def OnSpin( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def OnInfo( self, event ):
		event.Skip()
	
	def OnChar( self, event ):
		event.Skip()
	
	
	def OnCambios( self, event ):
		event.Skip()
	
	def OnGuardar( self, event ):
		event.Skip()
	
	def OnCargarDefault( self, event ):
		event.Skip()
	
	

###########################################################################
## Class FrameZonas
###########################################################################

class FrameZonas ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Zonas", pos = wx.DefaultPosition, size = wx.Size( 500,474 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"El localizador tomará como válidos los valores del conversor analógicos que estén dentro de las zonas indicadas, devolviendo como resultado la zona actual en la que se encuentra el valor de entrada.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticText29.Wrap( -1 )
		self.m_staticText29.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer35.Add( self.m_staticText29, 1, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.TOP, 5 )
		
		self.bitmap_ADC = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"pics/zonas.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.bitmap_ADC, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer35 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_LEFT_DCLICK, self.OnClose )
		self.Bind( wx.EVT_LEFT_DOWN, self.OnClose )
		self.m_staticText29.Bind( wx.EVT_LEFT_DOWN, self.OnClose )
		self.bitmap_ADC.Bind( wx.EVT_LEFT_DOWN, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	
	
	
	

