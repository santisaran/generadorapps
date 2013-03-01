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

int main (void)
{
    int retorno;
    FILE *fp;

    unsigned int i,j,k;
    unsigned int numApp, numEstado, numBloque, app, estado, bloque;
    unsigned int index = 0;
    uchar lectura[TAMANIOBLOQUE];
    uchar Leyendo = APLICACION;
    uchar interno=0;
    uchar Sincro = 0;
    if((fp = fopen("\\users\\santiago\\documents\\proyectos\\atop\\soft\\generadorsvn\\generadorapps\\uno.cb","rb"))<1)
    {
        printf("\nError al abrir archivo\n");
    }

    printf("leidos %d bytes: %02X %02X %02X %02X",retorno,lectura[0],lectura[1], lectura[2],lectura[3]);
    do
    {
        retorno = fread(lectura,sizeof(uchar),4,fp);
		if((lectura[0] == 0xAA) && (lectura[1] == (uchar)APLICACION))
		{
			numApp = (uint)lectura[2];
			if(numApp < Cantidad_Apps)
			{
				EstadoActual_App[numApp] = lectura[3];
				printf("\nEstado Actual de App %d: %d\n",numApp,EstadoActual_App[numApp]);
			}
		}
		else
		{
			printf("\nError Aplicacion App: %d,Est: %d,Bl: %d",numApp,numEstado,numBloque);
			return 1;
		}
		for (i=0;i<Cantidad_Estados;i++)
		{
			retorno = fread(lectura,sizeof(uchar),6,fp);
			printf("\nleidos %d bytes: %02X %02X %02X %02X %02X %02X\n",retorno,lectura[0],lectura[1], lectura[2],lectura[3],lectura[4],lectura[5]);
			if((lectura[0] == 0xAA) && (lectura[1] == (uchar)ESTADO)\
				&& (lectura[4] == 0xAA) && (lectura[5] == BLOQUE) )
			{
				numEstado = (lectura[3]<<8)+lectura[2];
				printf("\nNumero de estado: %d\n",numEstado);

			}
			else
			{
				printf("\nError ESTADO App:%d,Est:%d,Bl%d",numApp,numEstado,numBloque);
				return 1;
			}
			for(j=0;j<Cantidad_Bloques;j++)
			{
				retorno = fread(lectura,sizeof(uchar),6,fp);
				printf("\nleidos %d bytes: %02X %02X %02X %02X %02X %02X\n",retorno,lectura[0],lectura[1], lectura[2],lectura[3],lectura[4],lectura[5]);
				numBloque = ((uint)lectura[1]<<8)+(uint)lectura[0];
				printf("Bloque N: %d",numBloque);

				app = numBloque/(Cantidad_Estados*Cantidad_Bloques);
                estado = (numBloque%(Cantidad_Estados*Cantidad_Bloques))/Cantidad_Bloques;
                bloque = numBloque%(Cantidad_Estados*Cantidad_Bloques)%Cantidad_Bloques;

				Bloques[app][estado][bloque] = \
					(lectura[5]<<24) +(lectura[4]<<16) +(lectura[3]<<8) +lectura[2];
                printf("\nBloque: %X\n",Bloques[app][estado][bloque]);

			}
			retorno = fread(lectura,sizeof(uchar),5,fp);
			if((lectura[0] == 0xAA) && (lectura[1] == (uchar)CONDICION))
			{
				Condiciones[app][estado][0] = lectura[2];
				Condiciones[app][estado][1] = lectura[3];
				Condiciones[app][estado][2] = lectura[4];
			}
			else
			{
				printf("Error CONDICION App: %d,Est: %d,Bl: %d",numApp,numEstado,numBloque);
				return 1;
			}
			retorno = fread(lectura,sizeof(uchar),4,fp);
			if((lectura[0] == 0xAA) && (lectura[1] == (uchar)RESULTADO))
			{
				Resultado[app][estado][0] = lectura[2];
				Resultado[app][estado][1] = lectura[3];
			}
			else
			{
				printf("error Bloques App: %d,Est: %d,Bl: %d",numApp,numEstado,numBloque);
				return 1;
			}
		}
	}
	while((numApp<Cantidad_Apps-1)&(retorno > 0));

    for (i=0;i<Cantidad_Apps;i++)
	{
		for(j=0;j<Cantidad_Estados;j++)
		{
			for(k=0;k<Cantidad_Bloques;k++)
			{
				printf("Bloque: %08X ",Bloques[i][j][k]);
			}
		}
	}
	fclose(fp);
    return 0;
}
