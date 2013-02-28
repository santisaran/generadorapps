#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  proggen.py
#  
#  Copyright 2013 santiago <spaleka@cylgem.com.ar>
#  

from struct import pack,unpack
from apps import *


def main():
	cadena = ""
	salida = open("\\users\\santiago\\documents\\proyectos\\AtoP\\soft\\progcyloc.prg",'w')
	for i in range(Cantidad_Apps):
		cadena = cadena + "[Programa"+"%0.2d" % i +"]"+"\n"
		cadena = cadena + "Activo=Verdadero"+"\n"
		cadena = cadena + "Numero=0"+"\n"
		cadena = cadena + "Titulo="+"\n"
		cadena = cadena + "Comentario="+"\n"
		for j in range(Cantidad_Estados):
			cadena = cadena + "[Estado"+"%0.2d" % (i*Cantidad_Estados+j) +"]"+"\n"
			cadena = cadena + "Activo=Verdadero"+"\n"
			cadena = cadena + "Parametro1=0"+"\n"
			cadena = cadena + "Parametro2=0"+"\n"
			cadena = cadena + "Resultado1=0"+"\n"
			cadena = cadena + "Resultado2=0"+"\n"
			cadena = cadena + "TipoCondicion=0"+"\n"
			cadena = cadena + "Titulo="+"\n"
			cadena = cadena + "Comentario="+"\n"
			for k in range(Cantidad_Bloques):
				cadena = cadena + "[Bloques"+"%0.3d" % (i*Cantidad_Estados*Cantidad_Bloques+j*Cantidad_Bloques+k) +"]"+"\n"
				cadena = cadena + "Parametro1=0"+"\n"
				cadena = cadena + "Parametro2=0"+"\n"
				cadena = cadena + "Parametro3=0"+"\n"
				cadena = cadena + "TipoBloque=2"+"\n"
				cadena = cadena + "Comentario="+"\n"
	salida.write(cadena)
	salida.close()
	lista = []
	for i in range(Cantidad_Apps):
		cadena = cadena + "[Programa"+"%0.2d" % i +"]"+"\n"
		cadena = cadena + "Activo=Verdadero"+"\n"
		cadena = cadena + "Numero=0"+"\n"
		cadena = cadena + "Titulo="+"\n"
		cadena = cadena + "Comentario="+"\n"
		for j in range(Cantidad_Estados):
			cadena = cadena + "[Estado"+"%0.2d" % (i*Cantidad_Estados+j) +"]"+"\n"
			cadena = cadena + "Activo=Verdadero"+"\n"
			cadena = cadena + "Parametro1=0"+"\n"
			cadena = cadena + "Parametro2=0"+"\n"
			cadena = cadena + "Resultado1=0"+"\n"
			cadena = cadena + "Resultado2=0"+"\n"
			cadena = cadena + "TipoCondicion=0"+"\n"
			cadena = cadena + "Titulo="+"\n"
			cadena = cadena + "Comentario="+"\n"
			for k in range(Cantidad_Bloques):
				cadena = cadena + "[Bloques"+"%0.3d" % (i*Cantidad_Estados*Cantidad_Bloques+j*Cantidad_Bloques+k) +"]"+"\n"
				cadena = cadena + "Parametro1=0"+"\n"
				cadena = cadena + "Parametro2=0"+"\n"
				cadena = cadena + "Parametro3=0"+"\n"
				cadena = cadena + "TipoBloque=2"+"\n"
				cadena = cadena + "Comentario="+"\n"

	for i in Cantidad_Estados:
		listaEstados = [chr(0xAA),chr(0),chr(tipoEstado),chr(i)]
		for j in Cantidad_Bloques:
			listaBloques = [chr(0xAA),chr(0),chr(tipoBloque),]
		listaCondiciones = [chr(0xAA),chr(0),chr(tipoCondiciones),]
		listaResultados = [chr(0xAA),chr(0),chr(tipoResultados),]
	return 0

if __name__ == '__main__':
	main()

