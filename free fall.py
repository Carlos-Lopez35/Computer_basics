#importar numpy
import numpy as np 
#definir altura y aceleración gravitacional
h= 10000
g= 9.8 
#partes de tiempo
saltos_temporales= 10
t= np.linspace (0, 50, saltos_temporales)
#calculo de la posición de la pelota para cada t
y = h - (0.5 * g * t**2)
#evitar que la altura sea negativa
y = np.maximum(y, 0)
#calcular distancia a la que se encuentra la pelota en cada t
distancia = np.diff(y)
#calcular la media de las distancias
media_distancias = np.mean(distancia)
#mostrar resultados
print("Tiempos:", t)
print("Alturas:", y)
print("Distancia recorrida en cada intervalo:", np.abs(distancia))
print("Distancia media recorrida:", media_distancias)