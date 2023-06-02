import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import geom
from scipy.stats import mode
#a) Muestras aleatorias de tama˜nos 10^2, 10^3, 10^4 y 10^5
r1 = geom.rvs(0.08,size = 10**2)
r2 = geom.rvs(0.08,size = 10**3)
r3 = geom.rvs(0.08,size = 10**4)
r4 = geom.rvs(0.08,size = 10**5)
#b) Diagrama de cajas para cada muestra generada
fig, (ax1, ax2) = plt.subplots(2,1,figsize=(8,8))
ax1.boxplot([r1, r2, r3, r4])
ax1.set_xticklabels(['N=10^2', 'N=10^3', 'N=10^4', 'N=10^5'])
ax1.set_ylabel('X~G(p=0.08)')
ax1.set_title('Diagramas de Caja _ Distribución Geométrica')
#c) Histograma de las muestras generadas
ax2.hist(r1, bins='auto', alpha=0.7, density=True, label='n = 10^2')
ax2.hist(r2, bins='auto', alpha=0.7, density=True, label='n = 10^3')
ax2.hist(r3, bins='auto', alpha=0.7, density=True, label='n = 10^4')
ax2.hist(r4, bins='auto', alpha=0.7, density=True, label='n = 10^5')
ax2.set_xlabel('X~G(p=0.08)')
ax2.set_ylabel('Frecuencia Relativa')
ax2.set_title('Histogramas de Frecuencia _ Distribución Geométrica')
ax2.legend()
fig.tight_layout()
plt.show()
print("Muestras :  [10^2, 10^3, 10^4, 10^5]")
#d) Mediana y moda de cada muestra
print("Medianas : ",[np.median(r1), np.median(r2), np.median(r3), np.median(r4)])
print("Modas    : ",[mode(r1,axis=None,keepdims=True).mode[0],
                mode(r2,axis=None,keepdims=True).mode[0],
                mode(r3,axis=None,keepdims=True).mode[0],
                mode(r4,axis=None,keepdims=True).mode[0]])
#e) Medias muestrales y media poblacional
print("Medias   : ",[np.mean(r1), np.mean(r2), np.mean(r3), np.mean(r4)])
print("µ = ",1/0.08)
#f) Varianzas muestrales y varianza teórica
v=[np.var(r1), np.var(r2), np.var(r3), np.var(r4)]
print("Varianzas: ",[np.var(r1), np.var(r2), np.var(r3), np.var(r4)])
print("σ = ",(1-0.08)/(0.08**2))
