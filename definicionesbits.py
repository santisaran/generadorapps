DefinicionesBits = (
	("BitContacto", u"Estado de la entrada contacto", "p2.13"),
	("BitBtnPanic", u"Estado de la entrada Pánico", "p2.10"),
	("Bitpulsdesact", u"Estado de la entrada pulsdesact", "p0.17"),
	("BitPuerta", u"Estado de la entrada Puerta", "p1.10"),
	("BitPorton",u"Estado de la entrada Porton", "p2.11"),
	("BitTrailer",u"Estado de la entrada Trailer", "p2.12"),
	("BitSetCorteC",u"","p1.16"),
	("BitSetCorteNA",u"";"p0.25"),
	("BitAux1in",u"","p0.01"),
	("BitAux2in","",""),
	("BitSetCorte",u"Indica si se debe activar el rele de corte.",""),
	("BitAux1out","",""),
	("BitAux2out","",""),
	("Bitan0Zonas",u"""True => usar zonas, False => devolver valor AD
\t\t\tb1|b0 |zona
\t\t\tLas zonas son 0 | 0 |a
\t\t\t              0 | 1 |b
\t\t\t              1 | 0 |c
\t\t\t              1 | 1 |d""",""),

	("Bitan0Zb0",u"indicador zona bit bajo",""),
	("Bitan0Zb1",u"indicador zona bit alto",""),
	
	("Bitan0ZVal",u"True => dato de zona válido",""),
	("Bitan0",u"""False, no hay datos correctos
True, valor válido con antirrebote. (el antirrebote se define con:
Frecan0, frecuencia de muestreo en ms de entrada analógica.
CNTan0, Contador cuantos an0 dentro del rango.
CfgCNTan0, Cantidad de muestras para validar valor An0. """,""),
	
	("Bitan1val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an1VALOR]",""),
	("Bitan2val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an2VALOR]",""),
	("Bitan3val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an3VALOR]",""),
	("Bitan4val", u"True => dato válido en el vector MemoriaUsuario_Bytes[an4VALOR]",""),
	("Bitan5val", u"""True => dato válido en el vector MemoriaUsuario_Bytes[an5VALOR]",""),
	
	("BitLeerAn0",u"True => petición de lectura AD0.",""),
	("BitLeerAn1",u"True => petición de lectura AD1.",""),
	("BitLeerAn2",u"True => petición de lectura AD2.",""),
	("BitLeerAn3",u"True => petición de lectura AD3.",""),
	("BitLeerAn4",u"True => petición de lectura AD4.",""),
	("BitLeerAn5",u"True => petición de lectura AD5.",""),
	
	("BitLeerXYZ","",""),
	
	("BitLed",u"Led prendido u apagado.",""),
	("BitDestellar","",""),
	("BitCLed","",""),
	
	("BitAux1CfgInOut",u"Aux1 1=salida, 0=entrada",""),
	("BitAux2CfgInOut",u"Aux2 1=salida, 0=entrada",""),
	(
	("BitErrorLed",u"Falla salida de led.",""),
	("BitErrorCorte","",""),
	("BitErrorAux1","","" ),
	("BitErrorAux2","","" ),
	
	("Accel_Flag_DR",u"Flag indicador de dato nuevo de aceleracion disponible",""),
	("Accel_Flag_Choque", u"Flag de accidente. Para mas informacion, ver Registro STAT",""),
	
	("BitPulsos","",""),
	("BitBuzz","",""),
	("BitAntenaGPSCorto","",""),
	("BitAntenaGPSPresente","",""),
	("BitAntenaGSMCorto","",""),
	("BitAntenaGSMPresente","",""))
