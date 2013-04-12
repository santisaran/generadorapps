#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cylocsender.py
#
#  Copyright 2013 santiago <spaleka@cylgem.com.ar>
#


#TODO usar isModified() para guardar cambios.
#TODO independizar MODIFIDACO para cada ventana
#TODO guardar SMS en binario

import wx
import threading
import serial

import wxSerialConfigDialog


import GUI

PUERTO = 42
BAUDRATE = 19200
TIMEOUT = None
XONXOFF = False
WRITETIMEOUT = None

COMENZARPROG = 0x55

SERIALRX = wx.NewEventType()
EVT_SERIALRX = wx.PyEventBinder(SERIALRX, 0)

class SerialRxEvent(wx.PyCommandEvent):
    eventType = SERIALRX
    def __init__(self, windowID, data):
        wx.PyCommandEvent.__init__(self, self.eventType, windowID)
        self.data = data

    def Clone(self):
        self.__class__(self.GetId(), self.data)

class MyCylocFrame (GUI.CylocFrame):
    def __init__(self):
        super(MyCylocFrame,self).__init__(None)
        self.anterior = False
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimeout, self.timer1)
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnMantenerCom, self.timer2)
        #EVT_RESULT(self.frame, self.OnAcquireData)
        self.alive = threading.Event()
        try:
            self.serial = serial.Serial(serial.device(PUERTO), BAUDRATE,timeout=TIMEOUT, xonxoff=XONXOFF,writeTimeout=WRITETIMEOUT)
        except serial.SerialException, e:
            dlg = wx.MessageDialog(None, str(e), "Serial Port Error", wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            self.serial = serial.Serial()
            self.OnPortSettings()
        else:
            self.StartThread()
            self.SetTitle("Puerto: %s [%s, %s%s%s%s%s]" % (
                self.serial.portstr,
                self.serial.baudrate,
                self.serial.bytesize,
                self.serial.parity,
                self.serial.stopbits,
                self.serial.rtscts and ' RTS/CTS' or '',
                self.serial.xonxoff and ' Xon/Xoff' or '',
                )
            )        
        self.Bind(EVT_SERIALRX, self.OnSerialRead)
        self.EsperaACK = False
        self.ESTADOSSERIE = {0x55:self.RecvACK,0x01:self.RecvStart,0x02:self.RecvStop,0x03:self.RecvResend, 0x04:self.RecvAlive}
        
        
    def StartThread(self):
        """Start the receiver thread"""        
        self.thread = threading.Thread(target=self.ComPortThread)
        self.thread.setDaemon(1)
        self.alive.set()
        self.thread.start()


    def StopThread(self):
        """Stop the receiver thread, wait util it's finished."""
        if self.thread is not None:
            self.serial.setTimeout(0)
            self.serial.setWriteTimeout(0)
            self.alive.clear()          #clear alive event for thread
            self.thread.join()          #wait until thread has finished
            self.thread = None

  
    def ComPortThread(self):
        """Thread that handles the incomming traffic. Does the basic input
           transformation (newlines) and generates an SerialRxEvent"""
        while self.alive.isSet():               #loop while alive event is true
            try:
                text = self.serial.read(1)          #read one, with timout
                if text:
                    #self.sIbuf.put(text)
                    #check if not timeout
                    n = self.serial.inWaiting()     #look if there is more to read
                    if n:
                        text = text + self.serial.read(n)
                    event = SerialRxEvent(self.GetId(), text)
                    self.GetEventHandler().AddPendingEvent(event)
            except:
                print "error puerto serie"
                self.alive.clear()


    def OnSerialRead(self, event):
        """Maneja la entrada de puerto serie"""
        text = event.data
        try:
            #Agregar cadena de texto en el cuadro de izquierda
            self.textCtrlEntrada.AppendText(text.encode('latin1','ignore'))            
        except:
            pass
        #Agregar lo recibido por el puerto serie en fomato hexadecimal
        self.textCtrlEntradaHex.AppendText(str(map(hex,map(ord,text))))
        
        if self.EsperaACK:
            retorno = map(ord,text)
            print "recibido: " + str(retorno)
            if (len(retorno) == 2) and (retorno[0] == 0xaa): 
                if self.ESTADOSSERIE.has_key(retorno[1]):
                    self.ESTADOSSERIE[retorno[1]]()
            elif (len(retorno) == 1):
                if retorno[0] == 0xaa:
                    self.anterior = True
                elif self.anterior:
                    self.anterior = False
                    if self.ESTADOSSERIE.has_key(retorno[0]):
                        print "error salvado"
                        self.ESTADOSSERIE[retorno[0]]()
                
                
    def RecvACK(self):
        print "recibido ACK"
        self.ACKrecibido = True
        try:
            self.serial.write(COMENZARPROG)
            self.EsperaACK = True
            self.timer2.Start(500,oneShot=True)
        except:
            self.StopThread()
                
    def RecvStart(self):
        print "Recibido Start"
        pass
    
    def RecvStop(self):
        print "Recibido Stop"
        pass
    
    def RecvResend(self):
        print "Recibido Resend"
        pass
    
    def RecvAlive(self):
        self.timer2.Start(500,oneShot=True)
        print "ACK"
        pass
                    
    def OnPortSettings(self, event=None):
        """Show the portsettings dialog. The reader thread is stopped for the
           settings change."""
        if event is not None:           #will be none when called on startup
            self.StopThread()
            self.serial.close()
        ok = False
        while not ok:
            dialog_serial_cfg = wxSerialConfigDialog.SerialConfigDialog(None, -1, "",
                show=wxSerialConfigDialog.SHOW_BAUDRATE|wxSerialConfigDialog.SHOW_FORMAT|wxSerialConfigDialog.SHOW_FLOW,
                serial=self.serial
            )
            result = dialog_serial_cfg.ShowModal()
            dialog_serial_cfg.Destroy()
            #open port if not called on startup, open it on startup and OK too
            if result == wx.ID_OK or event is not None:
                try:
                    self.serial.open()
                except serial.SerialException, e:
                    dlg = wx.MessageDialog(None, str(e), "Serial Port Error", wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()
                    dlg.Destroy()
                else:
                    self.StartThread()
                    self.SetTitle("Serial Terminal on %s [%s, %s%s%s%s%s]" % (
                        self.serial.portstr,
                        self.serial.baudrate,
                        self.serial.bytesize,
                        self.serial.parity,
                        self.serial.stopbits,
                        self.serial.rtscts and ' RTS/CTS' or '',
                        self.serial.xonxoff and ' Xon/Xoff' or '',
                        )
                    )
                    ok = True
            else:
                #on startup, dialog aborted
                self.alive.clear()
                ok = True

    def OnClose( self, event ):
        self.StopThread()
        self.Destroy()
        event.Skip()
        
    def OnEnviarDatos(self , event):
        for i in range(self.textCtrlRep.GetValue()):
            aenviar = self.textCtrlDatos.GetValue()
            self.serial.write(aenviar)
            print aenviar
            
    def OnEnviarBinario(self , event):
        print "Enviando binario:"
        for i in range(self.textCtrlBinRep.GetValue()):
            aenviar = self.textCtrlBin.GetValue()            
            if len(aenviar)%2:
                aenviar = "0" + aenviar
            for j in range(len(aenviar)/2):
                dato = int(aenviar[j*2:(j*2)+2],16)
                print dato,
                self.serial.write(chr(dato))
        self.timer2.Stop()        
        
    def OnIniciarSerie(self,event):
        if self.tglBtnComenzar.GetValue():
            print "enviando encabezado"
            dato = chr(0xaa)
            for i in range(16):
                self.serial.write(dato)
                self.EsperaACK = True
                self.timer1.Start(1000,oneShot=True)
                self.tglBtnComenzar.SetLabel(u"Detener Comunicación")
        
                
#####################################################
#Timers: 
#Timer1 usado como timeout de conexión serie

    def OnTimeout(self,event):
        if self.EsperaACK:
            print "Tiempo fuera"
            self.EsperaACK = False
            self.tglBtnComenzar.SetValue(False)
            self.tglBtnComenzar.SetLabel(u"Comenzar Comunicación")
            self.timer2.Stop()
            
#timer2 usado para mantener la conexión.

    def OnMantenerCom(self,event):
        if self.tglBtnComenzar.GetValue():
            self.serial.write(chr(0x55))
            self.timer1.Start(1000,oneShot=True)
            self.EsperaACK = True
        
#####################################################       
                
    def OnBinChar(self,event):
        EsHexa(event)
        
    def OnBorrar(self, event):
        self.textCtrlEntrada.Clear()
        self.textCtrlEntradaHex.Clear()

            
    
def EsHexa(event):
    """Esta función recibe un evento del tipo EVTCHAR y se fija si el caracter
    ingresado es hexadecimal o un caracter de control, si no  es alguno de esos, 
    lo descarta"""
    
    keycode = event.GetKeyCode()
    if keycode < 255:
    # valid ASCII
        if chr(keycode).isdigit():
            # Valid alphanumeric character
            event.Skip()
        elif (keycode > 64 and keycode < 71)or(keycode > 96 and keycode < 103):
            event.Skip()
        elif keycode < 31 or keycode == 127 or keycode == '\n':
            event.Skip()
    elif keycode > 255:
        event.Skip()        
        
        
aplicacion = wx.App(0)
frame_usuario = MyCylocFrame()
frame_usuario.Show()
aplicacion.MainLoop()
