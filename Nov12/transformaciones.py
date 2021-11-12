import sys
import numpy as np


opciones=sys.argv[1:]
if (len(opciones)!= 1):
    print("Error en el numero de argumentos")
    exit()
   
if opciones[0] =="Temperaturas":
    print("Entre a conversion de temperaturas")
    op=1 #1 igual Celsius a Kelvin, 0 igual Kelvin a Celsius
    if op==1:
        print("Temperaturas de Celsius a Kelvin")
        Tin=0
        Tfin=100
        delta=20
        n=int((Tfin-Tin)/delta)
        #for i in range(n):
        #    TC=Tin+i*delta
        #    TK=TC+273.15
        #    print(TC,TK)
        TCK=np.zeros((2,n))
        ##TC=np.zeros(n)
        ##TK=np.zeros(n)
        for i in range(n):
            TCK[0,i]=Tin+i*delta
            TCK[1,i]=TCK[0,i]+273.15
            ##TC[i]=Tin+i*delta
            ##TK[i]=TK[i]+273.15
        ##np.savetxt("Temperaturas1_CtoK.txt",(TC,TK))
        np.savetxt("Temperaturas2_CtoK.txt",TCK.T)
        
        
        
        
    elif op==0:
        print("Temperaturas de Kelvin a Celsius")
        
    else:
        print("Opcion de temperaturas no reconocido")
        
elif opciones[0] == "Coordenadas":
    print("Entre a conversion de coordenadas")

elif opciones[0] == "Unidades":
    print("Entre a conversion de unidades")

else:
    print("opción no reconocida")
