import sys

Tin=float(sys.argv[1])
Tfin=float(sys.argv[2])
delta=float(sys.argv[3])

print(f"Tin={Tin},Tfin={Tfin},delta={delta}")

n=int((Tfin-Tin)/delta)


## Comentario de comparación de la sintaxis de un ciclo for en C y un ciclo for en python
#for(i=0;i<n;i++){
#
#}


TC=Tin

for i in range(n):
    TK=TC+273.15
    print(f"La {TC} de Celsius a Kelvin es TK={TK}")
    TC=TC+delta
