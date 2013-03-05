#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  acelerometro.py
#  
#  Copyright 2013 santiago <spaleka@cylgem.com.ar>
#  

from struct import unpack
import pylab as pl
import scipy as sp
import numpy as np

archivo = open("F:\\datos.bin",'rb')	
archstr = archivo.read() 	
archivo.close()
vector = []
for i in range(len(archstr)/8):
	vector.append(unpack('hhhH',archstr[i*8:i*8+8]))

modulo = []
for i in vector:
	modulo.append(((float(i[0])**2+float(i[1])**2+float(i[2])**2)**(0.5))/1024.0)

x = [i[0]/1024.0 for i in vector]
y = [i[1]/1024.0 for i in vector]
z = [i[2]/1024.0 for i in vector]
t = [i[3]/1024.0 for i in vector]
#pl.plot(t,x,t,y,t,z)
pl.plot(x)
pl.plot(y)
pl.plot(z)
pl.plot(modulo,color='k')
#pl.plot(t,range(len(t)))
pl.show()

