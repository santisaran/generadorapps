# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generador de Programas", pos = wx.DefaultPosition, size = wx.Size( 597,496 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		self.m_file_salir = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Salir"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.m_file_salir )
		
		self.m_menubar1.Append( self.m_archivo, u"&Archivo" ) 
		
		self.m_variables = wx.Menu()
		self.m_variables_Byte = wx.MenuItem( self.m_variables, wx.ID_ANY, u"Editar Variables Byte", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_variables.AppendItem( self.m_variables_Byte )
		
		self.m_variables_bit = wx.MenuItem( self.m_variables, wx.ID_ANY, u"Editar variables Bit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_variables.AppendItem( self.m_variables_bit )
		
		self.m_menubar1.Append( self.m_variables, u"Va&riables" ) 
		
		self.m_programas = wx.Menu()
		self.m_menubar1.Append( self.m_programas, u"&Programas" ) 
		
		self.m_drivers = wx.Menu()
		self.m_drivers_analog = wx.MenuItem( self.m_drivers, wx.ID_ANY, u"Entrada Analógica", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_drivers.AppendItem( self.m_drivers_analog )
		
		self.m_drivers_contacto = wx.MenuItem( self.m_drivers, wx.ID_ANY, u"Entrada Contacto", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_drivers.AppendItem( self.m_drivers_contacto )
		
		self.m_drivers_aux1 = wx.MenuItem( self.m_drivers, wx.ID_ANY, u"Entrada Auxiliar 1", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_drivers.AppendItem( self.m_drivers_aux1 )
		
		self.m_drivers_panico = wx.MenuItem( self.m_drivers, wx.ID_ANY, u"Entrada Pánico", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_drivers.AppendItem( self.m_drivers_panico )
		
		self.m_drivers_puls = wx.MenuItem( self.m_drivers, wx.ID_ANY, u"Entrada Pulsador", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_drivers.AppendItem( self.m_drivers_puls )
		
		self.m_drivers_porton = wx.MenuItem( self.m_drivers, wx.ID_ANY, u"Entrada Portón", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_drivers.AppendItem( self.m_drivers_porton )
		
		self.m_drivers_corteNA = wx.MenuItem( self.m_drivers, wx.ID_ANY, u"Entrada CorteNA", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_drivers.AppendItem( self.m_drivers_corteNA )
		
		self.m_drivers_cortec = wx.MenuItem( self.m_drivers, wx.ID_ANY, u"Entrada CorteC", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_drivers.AppendItem( self.m_drivers_cortec )
		
		self.m_menubar1.Append( self.m_drivers, u"&Drivers" ) 
		
		self.m_ventana = wx.Menu()
		self.m_menubar1.Append( self.m_ventana, u"&Ventana" ) 
		
		self.m_ayuda = wx.Menu()
		self.m_menubar1.Append( self.m_ayuda, u"A&yuda" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button22 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_button22, 0, wx.ALL, 5 )
		
		self.scroolled = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.scroolled.SetScrollRate( 5, 5 )
		self.sizerbotones = wx.BoxSizer( wx.VERTICAL )
		
		
		self.scroolled.SetSizer( self.sizerbotones )
		self.scroolled.Layout()
		self.sizerbotones.Fit( self.scroolled )
		bSizer32.Add( self.scroolled, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer32 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnEditarBytes, id = self.m_variables_Byte.GetId() )
		self.Bind( wx.EVT_MENU, self.OnEditarBit, id = self.m_variables_bit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDriverAnalog, id = self.m_drivers_analog.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDriver, id = self.m_drivers_contacto.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDriver, id = self.m_drivers_aux1.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDriver, id = self.m_drivers_panico.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDriver, id = self.m_drivers_puls.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDriver, id = self.m_drivers_porton.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDriver, id = self.m_drivers_corteNA.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDriver, id = self.m_drivers_cortec.GetId() )
		self.m_button22.Bind( wx.EVT_BUTTON, self.OnTest )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnEditarBytes( self, event ):
		event.Skip()
	
	def OnEditarBit( self, event ):
		event.Skip()
	
	def OnDriverAnalog( self, event ):
		event.Skip()
	
	def OnDriver( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	def OnTest( self, event ):
		event.Skip()
	

###########################################################################
## Class frmEditBit
###########################################################################

class frmEditBit ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Editar variables  Bits", pos = wx.DefaultPosition, size = wx.Size( 441,102 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.BitsTxtCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( 1,0 ), wx.DefaultSize, 0 )
		self.BitsTxtCtrl.SetMaxLength( 0 ) 
		gbSizer1.Add( self.BitsTxtCtrl, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.BitsSpinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( 0,0 ), wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 255 )
		gbSizer1.Add( self.BitsSpinCtrl, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Actualizar cambios", wx.Point( 0,1 ), wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_button15, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Deshacer cambios", wx.Point( 1,1 ), wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_button16, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gbSizer1.AddGrowableCol( 0 )
		gbSizer1.AddGrowableCol( 1 )
		gbSizer1.AddGrowableRow( 1 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.BitsTxtCtrl.Bind( wx.EVT_TEXT, self.OnText )
		self.BitsSpinCtrl.Bind( wx.EVT_SPINCTRL, self.OnBitSpinCtrl )
		self.m_button15.Bind( wx.EVT_BUTTON, self.OnEditBit )
		self.m_button16.Bind( wx.EVT_BUTTON, self.OnUndoBit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnText( self, event ):
		event.Skip()
	
	def OnBitSpinCtrl( self, event ):
		event.Skip()
	
	def OnEditBit( self, event ):
		event.Skip()
	
	def OnUndoBit( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgGenProg
###########################################################################

class dlgGenProg ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generador de Programación", pos = wx.DefaultPosition, size = wx.Size( 394,146 ), style = wx.DEFAULT_DIALOG_STYLE|wx.DIALOG_NO_PARENT )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Ingrese un título para el programa nuevo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_genprg_btn_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_genprg_btn_ok, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )
		
		
		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_genprg_btn_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		gSizer2.Add( self.m_genprg_btn_cancel, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.txtctrl_prog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtctrl_prog.SetMaxLength( 0 ) 
		bSizer2.Add( self.txtctrl_prog, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_genprg_btn_ok.Bind( wx.EVT_BUTTON, self.OnGenPrgOk )
		self.m_genprg_btn_cancel.Bind( wx.EVT_BUTTON, self.OnGenPrgCancel )
		self.txtctrl_prog.Bind( wx.EVT_TEXT_ENTER, self.OnGenPrgOk )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnGenPrgOk( self, event ):
		event.Skip()
	
	def OnGenPrgCancel( self, event ):
		event.Skip()
	
	

###########################################################################
## Class frmEditByte
###########################################################################

class frmEditByte ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Editar variables Byte", pos = wx.DefaultPosition, size = wx.Size( 413,101 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.BytesTxtCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( 1,0 ), wx.DefaultSize, 0 )
		self.BytesTxtCtrl.SetMaxLength( 0 ) 
		gbSizer1.Add( self.BytesTxtCtrl, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.BytesSpinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( 0,0 ), wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 1 )
		gbSizer1.Add( self.BytesSpinCtrl, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		self.frmEditByte_btn_Actualizar = wx.Button( self, wx.ID_ANY, u"Actualizar cambios", wx.Point( 0,1 ), wx.DefaultSize, 0 )
		gbSizer1.Add( self.frmEditByte_btn_Actualizar, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.frmEditByte_btn_Deshacer = wx.Button( self, wx.ID_ANY, u"Deshacer cambios", wx.Point( 1,1 ), wx.DefaultSize, 0 )
		gbSizer1.Add( self.frmEditByte_btn_Deshacer, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gbSizer1.AddGrowableCol( 0 )
		gbSizer1.AddGrowableCol( 1 )
		gbSizer1.AddGrowableRow( 1 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.BytesTxtCtrl.Bind( wx.EVT_TEXT, self.OnText )
		self.BytesSpinCtrl.Bind( wx.EVT_SPINCTRL, self.OnByteSpinCtrl )
		self.frmEditByte_btn_Actualizar.Bind( wx.EVT_BUTTON, self.OnEditByte )
		self.frmEditByte_btn_Deshacer.Bind( wx.EVT_BUTTON, self.OnUndoByte )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnText( self, event ):
		event.Skip()
	
	def OnByteSpinCtrl( self, event ):
		event.Skip()
	
	def OnEditByte( self, event ):
		event.Skip()
	
	def OnUndoByte( self, event ):
		event.Skip()
	

###########################################################################
## Class frmEditApp 
###########################################################################

class frmEditApp  ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Editar Programa", pos = wx.DefaultPosition, size = wx.Size( 498,406 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Datos del Programa" ), wx.VERTICAL )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.textoPrograma = wx.StaticText( self, wx.ID_ANY, u"Programa Nº:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textoPrograma.Wrap( -1 )
		bSizer25.Add( self.textoPrograma, 0, wx.ALL, 5 )
		
		self.frm_edit_btn_Nombre = wx.Button( self, wx.ID_ANY, u"Cambiar Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.frm_edit_btn_Nombre, 0, wx.ALL, 5 )
		
		
		sbSizer16.Add( bSizer25, 0, wx.EXPAND, 5 )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Lista de Estados" ), wx.VERTICAL )
		
		listEstadosChoices = []
		self.listEstados = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listEstadosChoices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
		sbSizer15.Add( self.listEstados, 1, wx.ALL|wx.EXPAND, 5 )
		
		gSizer3 = wx.GridSizer( 2, 4, 0, 0 )
		
		self.frm_edit_btn_editarestado = wx.Button( self, wx.ID_ANY, u"&Editar Estado", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.frm_edit_btn_editarestado, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.frm_edit_btn_copiarestado = wx.Button( self, wx.ID_ANY, u"C&opiar Estado", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.frm_edit_btn_copiarestado, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.frm_edit_btn_delestado = wx.Button( self, wx.ID_ANY, u"Eliminar Estado", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.frm_edit_btn_delestado, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		sbSizer15.Add( gSizer3, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		sbSizer16.Add( sbSizer15, 1, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.frm_edit_btn_delprog = wx.Button( self, wx.ID_ANY, u"Eliminar Programa", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.frm_edit_btn_delprog, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer26.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.frm_edit_btn_guardarprog = wx.Button( self, wx.ID_ANY, u"&Guardar Programa", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.frm_edit_btn_guardarprog, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
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
		self.listEstados.Bind( wx.EVT_LISTBOX_DCLICK, self.OnEditarEstado )
		self.frm_edit_btn_editarestado.Bind( wx.EVT_BUTTON, self.OnEditarEstado )
		self.frm_edit_btn_copiarestado.Bind( wx.EVT_BUTTON, self.OnDuplicarEstado )
		self.frm_edit_btn_delestado.Bind( wx.EVT_BUTTON, self.OnEliminarEstado )
		self.frm_edit_btn_delprog.Bind( wx.EVT_BUTTON, self.OnEliminarPrograma )
		self.frm_edit_btn_guardarprog.Bind( wx.EVT_BUTTON, self.OnGuardarPrograma )
		self.frm_edit_btn_cerrar.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnCambiarNombre( self, event ):
		event.Skip()
	
	def OnEditarEstado( self, event ):
		event.Skip()
	
	
	def OnDuplicarEstado( self, event ):
		event.Skip()
	
	def OnEliminarEstado( self, event ):
		event.Skip()
	
	def OnEliminarPrograma( self, event ):
		event.Skip()
	
	def OnGuardarPrograma( self, event ):
		event.Skip()
	
	

###########################################################################
## Class DialogoCopiarApp
###########################################################################

class DialogoCopiarApp ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Copiar Programas", pos = wx.DefaultPosition, size = wx.Size( 340,124 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Copia:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer27.Add( self.m_staticText25, 1, wx.ALL, 5 )
		
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
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Copiar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer29.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.OnCancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.OnCancelar, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer29, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer27 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.choiceAppA.Bind( wx.EVT_CHOICE, self.OnChoiceAppA )
		self.choiceAppB.Bind( wx.EVT_CHOICE, self.OnChoiceAppB )
		self.m_button24.Bind( wx.EVT_BUTTON, self.OnCopiar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
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
		self.txtctrlTitulo.SetMaxLength( 0 ) 
		bSizer29.Add( self.txtctrlTitulo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Comentario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		bSizer29.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.txtctrlComentario = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.txtctrlComentario.SetMaxLength( 0 ) 
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
		self.txtctrlSeudo.SetMaxLength( 0 ) 
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
		self.txtctrlSeudo.SetMaxLength( 0 ) 
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
		bSizer26.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.frmEstado_txtctrl_muestras = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.frmEstado_txtctrl_muestras.SetMaxLength( 0 ) 
		bSizer26.Add( self.frmEstado_txtctrl_muestras, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer26, 0, wx.EXPAND, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer28.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Tiempo de muestreo [ms]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		bSizer28.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.frmEstado_txtctrl_tiempo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.frmEstado_txtctrl_tiempo.SetMaxLength( 0 ) 
		bSizer28.Add( self.frmEstado_txtctrl_tiempo, 0, wx.ALL, 5 )
		
		
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
		self.btn_guardar.Bind( wx.EVT_BUTTON, self.OnGuardar )
		self.btn_cerrar.Bind( wx.EVT_BUTTON, self.OnCerrar )
		self.btn_cargar.Bind( wx.EVT_BUTTON, self.OnCargarDefaults )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCerrar( self, event ):
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuración entrada analógica", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Modo de Funcionamiento", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		bSizer8.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.dlg_analog_rad_4zonas = wx.RadioButton( self, wx.ID_ANY, u"Utilizar 4 zonas", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP|wx.RB_SINGLE )
		self.dlg_analog_rad_4zonas.SetValue( True ) 
		bSizer8.Add( self.dlg_analog_rad_4zonas, 0, wx.ALL, 5 )
		
		self.dlg_analog_rad_valorADC = wx.RadioButton( self, wx.ID_ANY, u"Obtener valor ADC", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP|wx.RB_SINGLE )
		bSizer8.Add( self.dlg_analog_rad_valorADC, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Configuración Zonas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		bSizer9.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Límite superior zona A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer3.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.dlg_Analog_txtctrl_Asup = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlg_Analog_txtctrl_Asup.SetMaxLength( 0 ) 
		gSizer3.Add( self.dlg_Analog_txtctrl_Asup, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Límite inferior zona A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer3.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.dlg_Analog_txtctrl_Ainf = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlg_Analog_txtctrl_Ainf.SetMaxLength( 0 ) 
		gSizer3.Add( self.dlg_Analog_txtctrl_Ainf, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Límite superior zona B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer3.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.dlg_Analog_txtctrl_Bsup = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlg_Analog_txtctrl_Bsup.SetMaxLength( 0 ) 
		gSizer3.Add( self.dlg_Analog_txtctrl_Bsup, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Límite inferior zona B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer3.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.dlg_Analog_txtctrl_Binf = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlg_Analog_txtctrl_Binf.SetMaxLength( 0 ) 
		gSizer3.Add( self.dlg_Analog_txtctrl_Binf, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Límite superior zona C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer3.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.dlg_Analog_txtctrl_Csup = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlg_Analog_txtctrl_Csup.SetMaxLength( 0 ) 
		gSizer3.Add( self.dlg_Analog_txtctrl_Csup, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Límite inferior zona C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer3.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.dlg_Analog_txtctrl_Cinf = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlg_Analog_txtctrl_Cinf.SetMaxLength( 0 ) 
		gSizer3.Add( self.dlg_Analog_txtctrl_Cinf, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Límite superior zona D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer3.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.dlg_Analog_txtctrl_Dsup = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlg_Analog_txtctrl_Dsup.SetMaxLength( 0 ) 
		gSizer3.Add( self.dlg_Analog_txtctrl_Dsup, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Límite inferior zona D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer3.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.dlg_Analog_txtctrl_Dinf = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlg_Analog_txtctrl_Dinf.SetMaxLength( 0 ) 
		gSizer3.Add( self.dlg_Analog_txtctrl_Dinf, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer9, 0, wx.EXPAND, 10 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Configuración General", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		bSizer11.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Tiempo de muestreo[ms]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gSizer5.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.dlg_analog_textCtrl_muestreo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlg_analog_textCtrl_muestreo.SetMaxLength( 0 ) 
		gSizer5.Add( self.dlg_analog_textCtrl_muestreo, 0, wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Cantidad de muestras\nPara validar zona", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		gSizer5.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.dlg_Analog_txtCtrl_muestras = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlg_Analog_txtCtrl_muestras.SetMaxLength( 0 ) 
		gSizer5.Add( self.dlg_Analog_txtCtrl_muestras, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Comentario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl17.SetMaxLength( 0 ) 
		bSizer7.Add( self.m_textCtrl17, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.frm_analog_btnGuardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.frm_analog_btnGuardar, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.frm_analog_btnCargarDefault = wx.Button( self, wx.ID_ANY, u"Cargar Default", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.frm_analog_btnCargarDefault, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.frm_analog_btnCerrar = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.frm_analog_btnCerrar, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.dlg_analog_rad_4zonas.Bind( wx.EVT_RADIOBUTTON, self.On4zonas )
		self.dlg_analog_rad_valorADC.Bind( wx.EVT_RADIOBUTTON, self.OnValorADC )
		self.frm_analog_btnGuardar.Bind( wx.EVT_BUTTON, self.OnGuardar )
		self.frm_analog_btnCargarDefault.Bind( wx.EVT_BUTTON, self.OnCargarDefault )
		self.frm_analog_btnCerrar.Bind( wx.EVT_BUTTON, self.OnCerrar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
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
	

