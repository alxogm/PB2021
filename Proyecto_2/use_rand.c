//Ejemplo adaptado https://man7.org/linux/man-pages/man3/srand.3.html

#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]){
    int  nloops,j;
    float r,a,b;
    unsigned int seed=0;

    if (argc != 2) {
        fprintf(stderr, "Forma de uso: %s <numero de iteraciones>\n", argv[0]);
        exit(EXIT_FAILURE);
        }

    nloops = atoi(argv[1]);
    //printf("%d\n",RAND_MAX);
    
    srand(seed);
    a=-5.5;
    b=6.5;
    for(j = 0; j < nloops; j++) {
        r =  (rand()*(1.0/RAND_MAX)*(b-a))+a;
        printf("%f\n", r);
        }
    
    exit(EXIT_SUCCESS);
}
