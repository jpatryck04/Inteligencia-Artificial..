import numpy as np

# Crear un array para representar la temperatura promedio diaria
temperaturas = np.array([22, 24, 25, 27, 30, 32, 28, 25, 26, 27])

# Calcular la temperatura media
temperatura_media = np.mean(temperaturas)

# Calcular la temperatura máxima
temperatura_maxima = np.max(temperaturas)

# Calcular la temperatura mínima
temperatura_minima = np.min(temperaturas)

# Imprimir los resultados
print("Temperatura media de la semana:", temperatura_media)
print("Temperatura máxima de la semana:", temperatura_maxima)
print("Temperatura mínima de la semana:", temperatura_minima)
