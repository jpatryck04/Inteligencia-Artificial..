import numpy as np
import matplotlib.pyplot as plt

# Crear un array para representar los días de la semana
dias = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# Crear un array para representar la temperatura promedio diaria
temperaturas = np.array([22, 24, 25, 27, 30, 32, 28, 25, 26, 27])

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Graficar la temperatura promedio diaria
plt.plot(dias, temperaturas, marker='o', color='b', label='Temperatura promedio')

# Añadir etiquetas y título
plt.xlabel('Días de la semana')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura promedio diaria en función de los días de la semana')
plt.legend()

# Mostrar la cuadrícula
plt.grid()

# Mostrar el gráfico
plt.show()
