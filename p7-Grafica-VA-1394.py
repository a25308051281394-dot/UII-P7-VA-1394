import numpy as np
import matplotlib.pyplot as plt

No_lista=[1,2,3,17,48]
Califica_ML=[20,30,80,100,90]
Califica_VA=[70,90,60,90,100]
plt.plot(No_lista,Califica_ML,label="Califica ML")
plt.plot(No_lista,Califica_ML,label="Califica VA")
plt.title( "Calificaciones Materianas")
plt.xlabel("Numero de lista")
plt.ylabel("Calificacion")
plt.legend()
plt.show ()