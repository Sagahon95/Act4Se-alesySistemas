import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 10000          # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs)  # Tiempo de 0 a 1 segundo

fm = 100            # Frecuencia del mensaje (Hz)
Am = 1              # Amplitud del mensaje
mensaje = Am * np.sin(2 * np.pi * fm * t)

# Graficar la señal de mensaje
plt.figure(figsize=(10, 4))
plt.plot(t, mensaje)
plt.title('Señal de mensaje (moduladora)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()
plt.show()

