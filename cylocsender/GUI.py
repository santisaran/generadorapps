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
## Class CylocFrame
###########################################################################

class CylocFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 629,465 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrlEntrada = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer4.Add( self.textCtrlEntrada, 3, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlEntradaHex = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer4.Add( self.textCtrlEntradaHex, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Datos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textCtrlDatos = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer2.Add( self.textCtrlDatos, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Rep:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textCtrlRep = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 1 )
		bSizer2.Add( self.textCtrlRep, 0, wx.ALL, 5 )
		
		self.btn_EnviarTexto = wx.Button( self, wx.ID_ANY, u"Enviar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_EnviarTexto, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Binarios", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.textCtrlBin = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer5.Add( self.textCtrlBin, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Rep:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.textCtrlBinRep = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0 )
		bSizer5.Add( self.textCtrlBinRep, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Enviar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button41 = wx.Button( self, wx.ID_ANY, u"Borrar Pantalla", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button41, 0, wx.ALL, 5 )
		
		self.btnSalir = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnSalir, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"EnviarInit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button5, 0, wx.ALL, 5 )
		
		self.tglBtnComenzar = wx.ToggleButton( self, wx.ID_ANY, u"Comenzar Comunicación", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.tglBtnComenzar, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.textCtrlDatos.Bind( wx.EVT_TEXT_ENTER, self.OnEnviar )
		self.btn_EnviarTexto.Bind( wx.EVT_BUTTON, self.OnEnviarDatos )
		self.textCtrlBin.Bind( wx.EVT_CHAR, self.OnBinChar )
		self.textCtrlBin.Bind( wx.EVT_TEXT_ENTER, self.OnEnterBin )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnEnviarBinario )
		self.m_button41.Bind( wx.EVT_BUTTON, self.OnBorrar )
		self.btnSalir.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnIniciarSerie )
		self.tglBtnComenzar.Bind( wx.EVT_TOGGLEBUTTON, self.OnIniciarSerie )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnEnviar( self, event ):
		event.Skip()
	
	def OnEnviarDatos( self, event ):
		event.Skip()
	
	def OnBinChar( self, event ):
		event.Skip()
	
	def OnEnterBin( self, event ):
		event.Skip()
	
	def OnEnviarBinario( self, event ):
		event.Skip()
	
	def OnBorrar( self, event ):
		event.Skip()
	
	def OnClose( self, event ):
		event.Skip()
	
	def OnIniciarSerie( self, event ):
		event.Skip()
	
	

