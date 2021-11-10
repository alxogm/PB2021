//Ejemplo de uso de sprintf para definir una cadena de caracteres, que cambia dentro de un ciclo, para usar esa variable como nombre de archivo a guardar.

#include <stdio.h>

int main(){
	char fname[11];
    FILE *fp;
	int i,j=0;
	for(i=0;i<11;i++){
        //Creación del nombre del archivo a crear y escribir en el
        sprintf(fname,"salida_t%d%d",j,i);
        printf("%s\n",fname);
        //
        fp=fopen(fname,"w");
        fprintf(fp,"abri y cerre archivo");
        fclose(fp);
	}
    return(0);
}
