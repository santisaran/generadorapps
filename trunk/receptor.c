#include <stdio.h>
#include <sys/stat.h> 
#include <fcntl.h>

#define TAMANIOBLOQUE  512
#define		Cantidad_Apps				20
#define		Cantidad_Estados			10
#define		Cantidad_Bloques			5

typedef enum {
	ESTADO0,
	ESTADO1,
	ESTADO2,
	ESTADO3,
	ESTADO4,
	ESTADO5,
	ESTADO6,
	ESTADO7,
	ESTADO8,
	ESTADO9,
}estados_t;

static estados_t EstadoActual_App [Cantidad_Apps];
static unsigned long Bloques [Cantidad_Apps][Cantidad_Estados][Cantidad_Bloques];
// Parametro1   = (Bloques[App][Estado][Bloque] & 0x000000FF)	  ;
// Parametro2   = (Bloques[App][Estado][Bloque] & 0x0000FF00) >> 8 ;
// Parametro3   = (Bloques[App][Estado][Bloque] & 0x00FF0000) >> 16;
// TipoDeBloque = (Bloques[App][Estado][Bloque] & 0x3F000000) >> 24;
static unsigned char Condiciones [Cantidad_Apps][Cantidad_Estados][3];
// tipo condicion 	= Codiciones[app][estado][0]
// parametro1 		= Codiciones[app][estado][1]
// parametro2		= Codiciones[app][estado][2]
// Resultados de las condiciones
static estados_t Resultado [Cantidad_Apps][Cantidad_Estados][2];

enum{
    APLICACION=1,
    BLOQUE,
    ESTADO,
    CONDICION,
    RESULTADO,
    ERROR_LECTURA
};
typedef unsigned int uint;
typedef unsigned char uchar;

int main ()
{
    int retorno;
    int fp;
    
    unsigned int i,j,k;
    unsigned int numApp, numEstado, numBloque;
    unsigned int index = 0;
    uchar lectura[TAMANIOBLOQUE];
    uchar Leyendo = APLICACION;
    uchar interno=0;
    uchar Sincro = 0;
    fp = open("/home/saran/Documentos/trabajo/generadorwx/generadorapps/actual.cb",O_RDONLY);
    retorno = read(fp,lectura,4);
    
    do{
		if((lectura[0] == 0xAA) && (lectura[1] == (uchar)APLICACION))
		{
			numApp = (uint)lectura[2];
			if(numApp < Cantidad_Apps)
			{
				EstadoActual_App[numApp] = lectura[4];
			}
		}
		else
		{
			printf("Error Aplicacion App:%d,Est:%d,Bl%d",numApp,numEstado,numBloque);
			return 1;
		}
		for (i=0;i<Cantidad_Estados;i++)
		{
			retorno = read(fp,lectura,6);
			if((lectura[0] == 0xAA) && (lectura[1] == (uchar)ESTADO)\
				&& (lectura[4] == 0xAA) && (lectura[5] == BLOQUE) )
			{
				numEstado = (lectura[3]<<8)+lectura[2];
			}
			else
			{	
				printf("Error ESTADO App:%d,Est:%d,Bl%d",numApp,numEstado,numBloque);
				return 1;
			}
			for(j=0;j<Cantidad_Bloques;j++)
			{
				retorno = read(fp,lectura,6);
				numBloque = (lectura[1]<<8)+lectura[0];
				if (numBloque < Cantidad_Bloques)
				{
					Bloques[numApp][numEstado][numBloque] = \
						(lectura[5]<<24) +(lectura[4]<<16) +(lectura[3]<<8) +lectura[2];
				}
			}
			retorno = read(fp,lectura,5);
			if((lectura[0] == 0xAA) && (lectura[1] == (uchar)CONDICION))
			{
				Condiciones[numApp][numEstado][0] = lectura[2];
				Condiciones[numApp][numEstado][1] = lectura[3];
				Condiciones[numApp][numEstado][2] = lectura[4];
			}
			else
			{
				printf("Error CONDICION App:%d,Est:%d,Bl:%d",numApp,numEstado,numBloque);
				return 1;
			}
			retorno = read(fp,lectura,4);
			if((lectura[0] == 0xAA) && (lectura[1] == (uchar)RESULTADO))
			{
				Resultado[numApp][numEstado][0] = lectura[2];
				Resultado[numApp][numEstado][1] = lectura[3];
			}
			else
			{
				printf("error Bloques App:%d,Est:%d,Bl%d",numApp,numEstado,numBloque);
				return 1;
			}
		}
	}while(numApp<Cantidad_Apps-1);
	for (i=0;i<Cantidad_Apps;i++)
	{
		for(j=0;j<Cantidad_Estados;j++)
		{
			for(k=0;k<Cantidad_Bloques;k++)
			{
				printf("Bloque: %d",Bloques[i][j][k]);
			}
		}
	}
	close(fp);
    return 0;
}
