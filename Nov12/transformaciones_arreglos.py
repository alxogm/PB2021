import sys
import numpy as np


opciones=sys.argv[1:]
if (len(opciones)!= 1):
    print("Error en el numero de argumentos")
    exit()
   
if opciones[0] =="Temperaturas":
    print("Entre a conversion de temperaturas")
    op=0 #1 igual Celsius a Kelvin, 0 igual Kelvin a Celsius
    if op==1:
        print("Temperaturas de Celsius a Kelvin")
        Tin=0
        Tfin=100
        delta=20
        n=int((Tfin-Tin)/delta)
        
        TC=np.arange(Tin,Tfin,delta)
        TK=TC+273.15
        
        TCK=np.zeros((2,n))
        ##TCK[0,:]=np.arange(Tin,Tfin,delta)
        ##TCK[1,:]=TCK[0]+273.15
        TCK[0]=np.arange(Tin,Tfin,delta)
        TCK[1]=TCK[0]+273.15
        
        np.savetxt("Temperaturas1_CtoK_arr.txt",(TC,TK))
        np.savetxt("Temperaturas2_CtoK_arr.txt",TCK.T)
        
    elif op==0:
        print("Temperaturas de Kelvin a Celsius")
        Tin=100
        Tfin=300
        delta=0.01
        n=int((Tfin-Tin)/delta)
#        TK=np.arange(Tin,Tfin,delta)
        TK,step=np.linspace(Tin,Tfin,n,endpoint=True,retstep=True)
        print(step)
        TC=TK-273.15
        TKC=np.zeros((2,n))
        ##TCK[0,:]=np.arange(Tin,Tfin,delta)
        ##TCK[1,:]=TCK[0]+273.15
        TKC[0],step=np.linspace(Tin,Tfin,n,retstep=True)
        TKC[1]=TKC[0]-273.15
        
        np.savetxt("Temperaturas1_KtoC_arr.txt",(TK,TC))
        np.savetxt("Temperaturas2_KtoC_arr.txt",TKC.T)
        
    else:
        print("Opcion de temperaturas no reconocido")
        
elif opciones[0] == "Coordenadas":
    print("Entre a conversion de coordenadas")

elif opciones[0] == "Unidades":
    print("Entre a conversion de unidades")

else:
    print("opción no reconocida")
