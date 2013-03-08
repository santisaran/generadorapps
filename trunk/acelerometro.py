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

#archivo = open("F:\\noviaje.bin",'rb')   
archivo = open("C:\\Users\\santiago\\Documents\\Proyectos\\ATOP\\LOGS\\Acel\\prueba_.bin","rb")
archstr = archivo.read()
archivo.close()
vector = []

for i in range(len(archstr)/8):
    vector.append(unpack('hhhH',archstr[i*8:i*8+8]))

modulo = []

for i in vector:
    modulo.append(((float(i[0])**2+float(i[1])**2+float(i[2])**2)**(0.5)))


promedio = 0.0  
for i in modulo:
    promedio += i
promedio = promedio/len(modulo)

print "Promedio Modulo: " +str(promedio)

xprom = 0.0

x = [i[0]/(promedio) for i in vector]

for i in x:
    xprom += i
print "Promedio X: "+ str(promedio)


y = [i[1]/(promedio) for i in vector]
z = [i[2]/(promedio) for i in vector]
xyz = [i/(promedio) for i in modulo]

xfil = [(x[i]+x[i+1]+x[i+2]+x[i+3]+x[i+4]+x[i+5])/6.0 for i in range(len(x)-5)]
for i in range(5):
    xfil.append(0)
yfil = [(y[i]+y[i+1]+y[i+2]+y[i+3]+y[i+4]+y[i+5])/6.0 for i in range(len(y)-5)]
for i in range(5):
    yfil.append(0)
zfil = [(z[i]+z[i+1]+z[i+2]+z[i+3]+z[i+4]+z[i+5])/6.0 for i in range(len(z)-5)]
for i in range(5):
    zfil.append(0)

modulofil = [(modulo[i]+modulo[i+1]+modulo[i+2]+modulo[i+3]+modulo[i+4]+modulo[i+5])/(6*(promedio)) for i in range(len(modulo)-5)]
for i in range(5):
    modulofil.append(0)
    


t = [i[3]/1000.0 for i in vector] #vector tiempo en minutos
tacc = []
acc = 0

for i in range(len(t)):
    tacc.append((t[i] + acc))
    acc = tacc[i]

#pl.plot(tacc[:-5],xfil[:-5],tacc[:-5],yfil[:-5],tacc[:-5],zfil[:-5],\
    #tacc[:-5],modulofil[:-5])
   
fig = pl.figure()
fig.add_subplot(211)
pl.plot(tacc,x,tacc,y,tacc,z,tacc,xyz)
fig.add_subplot(212)
pl.plot(tacc,xfil,tacc,yfil,tacc,zfil,tacc,modulofil)
pl.show()

