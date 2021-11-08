//Ejemplo de uso de sprintf para definir una cadena de caracteres, que cambia dentro de un ciclo. 

#include <stdio.h>

int main(){
	char fname[11];
	int i;
	for(i=0;i<100;i++){
        sprintf(fname,"salida_t%d",i);
	printf("%s\n",fname);
	}
}
