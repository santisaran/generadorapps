#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generarCylocDefines.py
#  
#  Copyright 2013 Santiago <saran@Truchepe>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
Encabezado = u"""/* Archivo Generado con generarheader.py,\nNo modificar este\
 archivo*/\n\n"""

tupleBits = (
	("BitContacto",		u"Estado de la entrada contacto 	p2.13"),
	("BitBtnPanic",		u"Estado de la entrada Pánico	 	p2.10"),
	("Bitpulsdesact",	u"Estado de la entrada pulsdesact	p0.17"),
	("BitPuerta",		u"Estado de la entrada Puerta		p1.10"),
	("BitPorton",		u"Estado de la entrada Porton		p2.11"),
	("BitTrailer",		u"Estado de la entrada Trailer		p2.12"),
	("BitSetCorteC",	u"									p1.16"),
	("BitSetCorteNA",	u"	 								p0.25"),
	("BitAux1in",		u"									p0.01"),
	("BitAux2in",		u"										 "),	
	("BitSetCorte",		u"Indica si se debe activar el rele de corte"),
	("BitAux1out",		u""),
	("BitAux2out",		u""),
	("Bitan0Zonas",		u"""True => usar zonas, False => devolver valor AD
\t\t\t\tb1|b0 |zona
\t\t\t\tLas zonas son 	0 | 0 |a
\t\t\t\t0 | 1 |b
\t\t\t\t1 | 0 |c
\t\t\t\t1 | 1 |d"""),
	("Bitan0Zb0",		u"indicador zona Bit bajo"),
	("Bitan0Zb1",		u"indicador zona Bit alto"),
	("Bitan0ZVal",		u"True => dato de zona válido"),
	("Bitan0",			u"""False, no hay datos correctos
\t\t\tTrue, valor válido con antirrebote. (el antirrebote se define con:
\t\t\tFrecan0, frecuencia de muestreo en ms de entrada analógica.
\t\t\tCNTan0, Contador cuantos an0 dentro del rango.
\t\t\tCfgCNTan0, Cantidad de muestras para validar valor An0. """),
	("Bitan0val", 		u"True => dato válido en el vector MemoriaUsuario_Bytes[an0VALOR]"),
	("Bitan1val", 		u"True => dato válido en el vector MemoriaUsuario_Bytes[an1VALOR]"),
	("Bitan2val", 		u"True => dato válido en el vector MemoriaUsuario_Bytes[an2VALOR]"),
	("Bitan3val", 		u"True => dato válido en el vector MemoriaUsuario_Bytes[an3VALOR]"),
	("Bitan4val", 		u"True => dato válido en el vector MemoriaUsuario_Bytes[an4VALOR]"),
	("Bitan5val", 		u"True => dato válido en el vector MemoriaUsuario_Bytes[an5VALOR]"),
	("BitLeerAn0",		u"True => petición de lectura AD0."),
	("BitLeerAn1",		u"True => petición de lectura AD1."),
	("BitLeerAn2",		u"True => petición de lectura AD2."),
	("BitLeerAn3",		u"True => petición de lectura AD3."),
	("BitLeerAn4",		u"True => petición de lectura AD4."),
	("BitLeerAn5",		u"True => petición de lectura AD5."),
	("BitLeerXYZ",		u"	"),
	("BitLed",			u"Led prendido u apagado."),
	("BitDestellar",	u" "),
	("BitCLed",			u""),
	("BitAux1CfgInOut", u"Aux1 1=salida, 0=entrada"),
	("BitAux2CfgInOut", u"Aux2 1=salida, 0=entrada"),
	("BitErrorLed",		u"Falla salida de led."),
	("BitErrorCorte",	u" "),
	("BitErrorAux1",	u" "),
	("BitErrorAux2",	u" "),
	("Accel_Flag_DR",	u"Flag indicador de dato nuevo de aceleracion disponible."),
	("Accel_Flag_Choque",u"Flag de accidente. Para mas informacion, ver Registro STAT"),
	("BitPulsos",	 	u" "),
	("BitBuzz",	 		u""),
	("BitAntenaGPSCorto",		u""),
	("BitAntenaGPSPresente", 	u""),
	("BitAntenaGSMCorto",		u""),
	("BitAntenaGSMPresente", 	u""),
	("Bitfinal",u"Bit final para calcular dinamicamente tamaño"),
)

tupleBytes = (
	("FrecContacto",	u"frecuencia de muestreo contacto."),
	("CNTContacto",		u"Contador cuantos Contacto iguales."),
	("CfgCNTContacto",	u"Cantidad de muestras para validar Contacto."),
	("FrecAux1in",		u"frecuencia de muestreo en ms de Aux1in."),
	("CfgCNTAux1in",	u"Cantidad de muestras para validar Aux1in."),
	("CNTAux1in",		u"Contador de Aux1in iguales"),
	("FrecAux2in",		u"frecuencia de muestreo en ms de Aux1in."),
	("CfgCNTAux2in",	u"Cantidad de muestras para validar Aux1in."),
	("CNTAux2in",		u"Contador de Aux1in iguales"),
	("FrecBtnPanic",	u"frecuencia de muestreo en ms de btn pánico."),
	("CNTBtnPanic",		u"Contador cuantos btn pánico iguales."),
	("CfgCNTBtnPanic",	u"Cantidad de muestras para validar btn pánico."),
	("Frecpulsdesact",	u"frecuencia de muestreo en ms del puls desactivacion"),
	("CNTpulsdesact",	u"Contador cuantos puls desact iguales."),
	("CfgCNTpulsdesact",u"Cantidad de muestras para validar puls desactivacion"),
	("Frecpuerta",		u"frecuencia de muestreo en ms de puerta."),
	("CNTpuerta",		u"Contador cuantos puerta iguales."),
	("CfgCNTpuerta",	u"Cantidad de muestras para validar puerta."),
	("Frecporton",		u"frecuencia de muestreo en ms de portón."),
	("CNTporton",		u"Contador cuantos portón iguales."),
	("CfgCNTporton",	u"Cantidad de muestras para validar portón."),
	("Frectrailer",		u"frecuencia de muestreo en ms de trailer."),
	("CNTtrailer",		u"Contador cuantos trailer iguales."),
	("CfgCNTtrailer",	u"Cantidad de muestras para validar trailer."),
	("FrecCorteNA",		u"frecuencia de muestreo en ms de CorteNA."),
	("CNTCorteNA",		u"Contador cuantos CorteNA iguales."),
	("CfgCNTCorteNA",	u"Cantidad de muestras para validar CorteNA."),
	("FrecCorteC",		u"frecuencia de muestreo en ms de CorteC."),
	("CNTCorteC",		u"Contador cuantos CorteC iguales."),
	("CfgCNTCorteC",	u"Cantidad de muestras para validar CorteC."),
	("TiempoCorte",		u"tiempo entre activacion y lectura de la realimentacion."),
	("TiempoAux1",		u""),
	("TiempoAux2",		u""),
	("CorteReintentos",	u""),
	("Aux1Reintentos",	u""),
	("Aux2Reintentos",	u""),
	("Frecan0",			u"frecuencia de muestreo en ms de entrada analógica."),
	("FrecVccTest",		u"frecuencia de muestreo en ms de entrada Vcc."),
	("CNTan0",			u"Contador cuantos an0 dentro del rango."),
	("CfgCNTan0",		u"Cantidad de muestras para validar AD0.  "),
	("an0VALOR",		u"Valor de la conversión para AD0"),
	("an0Zai",			u"Límite inferior zona A"),
	("an0Zas",			u"Límite superior zona A"),
	("an0Zbi",			u"Límite inferior zona B"),
	("an0Zbs",			u"Límite superior zona B "),
	("an0Zci",			u" Límite inferior zona C"),
	("an0Zcs",			u" Límite superior zona C"),
	("an0Zdi",			u"Límite inferior zona D"),
	("an0Zds",			u"Límite superior zona D"),
	("an1VALOR",		u"Valor de la conversión para AD1"),
	("an2VALOR",		u"Valor de la conversión para AD2"),
	("an3VALOR",		u"Valor de la conversión para AD3"),
	("an4VALOR",		u"Valor de la conversión para AD4"),
	("an5VALOR",		u"Valor de la conversión para AD5"),
	("an0ZONA",			u""),
	("VccVALOR",		u""),
	("FrecLed",			u"Frecuencia de encendido ms de LED"),
	("CfgCNTLed",		u"Configuración cantidad de destellos led cada vez que es disparado."),
	("CNTLed",			u""),
	("DutyLed",			u"porcentaje apagado encendido 50ms de paso."),
	("CfgCNTCLed",		u""),
	#("//TMRLed",u"timer incrementado cada 1ms."),
	("Accel_X_MSB",		u"MSB de la aceleracion Actual eje X."),
	("Accel_X_LSB",		u"LSB de la aceleracion Actual eje X."),
	("Accel_Y_MSB",		u"MSB de la aceleracion Actual eje Y."),
	("Accel_Y_LSB",		u"LSB de la aceleracion Actual eje Y."),
	("Accel_Z_MSB",		u"MSB de la aceleracion Actual eje Z."),
	("Accel_Z_LSB",		u"LSB de la aceleracion Actual eje Z."),
	("Accel_StChoque",	u"""Copia del registro STATE del detector de transitorios del acelerometro.
			Actualizado solo cuando hay un choque!"""),
	("Frecbuzz",		u""),
	("CfgCNTbuzz",		u""),
	("CNTbuzz",			u""),
	("Frecoscbuzz",		u""),
	("Dutyenc",			u"")
)
defineCantidades = (
	("Cantidad_Apps",		20,""),
	("Cantidad_Estados",	10,""),
	("Cantidad_Bloques",	5,""),
	("Cantidad_de_Bytes", 256,""),
	("Cantidad_de_Bits", 	64/8,"64 bits, en grupos de bytes"),
)

descripBloque = """/*
* BLOQUES:
*	[31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1  0 ]
*         |  TIPO BLOQUE    |     parametro3        |   parametro2       |       parametro1         |
*
* Almacenado en los bits [29:24] de la informacion de los bloques (uint32_t)*/"""

tupleBloques = (
	("Bloque_Null",				""),
	("Bloque_Incrementar",		""),
	("Bloque_Decrementar",		""),
	("Bloque_AND_2_BIT",		""),
	("Bloque_OR_2_BIT",			""),
	("Bloque_NOT_BIT",			""),
	("Bloque_Sumar_2_Reg",		""),
	("Bloque_Restar_2_Reg",		""),
	("Bloque_Invertir_Reg",		""),
	("Bloque_Transmitir_BB",	""),
	("Bloque_SetBit",			""),
	("Bloque_ClrBit",			""),
	("Bloque_ClrReg",			"")
)

descripCondiciones = u"""Defines Tipos de Condiciones"""
defineCondiciones = (
("Condicion_Mayor",		0),
("Condicion_Menor",		1),
("Condicion_Igual",		2),
("Condicion_Bit_True",	3),
("Condicion_Bit_False",	4),
("Condicion_NULL",		5),
("BLOQUE(Bloque)",  	"((uint32_t)Bloque<<8*3)"),
("PARAM1(param)",		"((uint32_t)param<<8*0)"),
("PARAM2(param)",		"((uint32_t)param<<8*1)"),
("PARAM3(param)",		"((uint32_t)param<<8*2)")
)

enumEstados = (
	("ESTADO0",),
	("ESTADO1",),
	("ESTADO2",),
	("ESTADO3",),
	("ESTADO4",),
	("ESTADO5",),
	("ESTADO6",),
	("ESTADO7",),
	("ESTADO8",),
	("ESTADO9",)
)




def main():
	
	NombreBits = {}
	# {"NOMBRE":[VALOR,COMENTARIO], }
 
	archivoh = u"" + Encabezado

	archivoh += u"enum NombreBits\n{\n"
	for num,BIT in enumerate(tupleBits):
		NombreBits[BIT[0]] = (num,BIT[1])
		archivoh += u"\t" + BIT[0] +u" = " + str(num) + u", /*" + BIT[1] + u"*/\n"


	NombreBytes = {}
	archivoh = archivoh + u"\nenum NombreBytes\n{\n"
	for num,BIT in enumerate(tupleBytes):
		NombreBytes[BIT[0]] = (num,BIT[1])
		archivoh += u"\t" + BIT[0] +u" = " + str(num) + u", /*" + BIT[1] + u"*/\n"	
	archivoh += u"}\n\n"
	
	for item in defineCantidades:
		archivoh += "#define\t" + str(item[0]) + "\t" + str(item[1]) + "\t// " + str(item[2]) + "\n"

	archivoh += "\n" + descripBloque + "\n\n"

	archivoh += "enum TipoBloques\n{ \n"
	for num,item in enumerate(tupleBloques):
		archivoh += "\t" + str(item[0]) + ",\t" + str(item[1]) + "\n"
	archivoh += "};\n"

	archivoh += "\n// " + descripCondiciones + "\n\n"
	
	for item in defineCondiciones:
		archivoh += "#define\t" + str(item[0]) + "\t" + str(item[1]) + "\n"
	archivoh += "\n"
	
	archivoh += "enum defineEstados\n{ \n"
	for item in enumEstados:
		archivoh +=item[0] + ",\n"
	archivoh += "};\n"
	
	parsear = open("/home/saran/Documentos/trabajo/crear.h",'w')
	parsear.write(archivoh.encode('utf-8'))
	parsear.close()
	return 0

if __name__ == '__main__':
	main()

