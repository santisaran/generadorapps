#include <stdio.h>
#include <sys/stat.h> 
#include <fcntl.h>

void main ()
{
    int retorno;
    int fp;
    unsigned int i;
    unsigned int index = 0;
    unsigned char lectura[512];

    fp = open("/home/saran/Documentos/trabajo/generadorwx/generadorapps/actual.cb",O_RDONLY);
    do
    {
        retorno = read(fp,lectura,512);
        for (i=0;i<retorno;i++)
        {
            printf("%02X ",lectura[i]);
        }
    }while(retorno == 512);
    close(fp);
}
