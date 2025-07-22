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

# Parámetros de la portadora
fc = 1000           # Frecuencia de la portadora (Hz)
Ac = 1              # Amplitud de la portadora

# Señal portadora
portadora = Ac * np.cos(2 * np.pi * fc * t)

# Señal modulada (AM doble banda con portadora)
modulada = (1 + mensaje) * portadora

# Graficar la señal modulada
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], modulada[:1000])  # Mostramos solo una parte para que se vea bien
plt.title('Señal Modulada en Amplitud (AM)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()
plt.show()

# Calcular la FFT
N = len(modulada)              # Número de muestras
fft_modulada = np.fft.fft(modulada)
fft_modulada = np.abs(fft_modulada) / N  # Magnitud normalizada

# Crear eje de frecuencias
freq = np.fft.fftfreq(N, 1/fs)

# Graficar solo la mitad positiva (por simetría)
plt.figure(figsize=(10,4))
plt.plot(freq[:N//2], fft_modulada[:N//2])
plt.title('Espectro de la señal modulada (AM)')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.grid(True)
plt.tight_layout()
plt.show()

# Importar librería para ruido
from numpy.random import normal

# Parámetros de ruido
SNR_dB = 10  # Relación señal a ruido en decibelios

# Potencia señal modulada
pot_signal = np.mean(modulada**2)

# Calcular potencia ruido para el SNR deseado
SNR = 10**(SNR_dB / 10)
pot_noise = pot_signal / SNR

# Generar ruido gaussiano blanco
ruido = np.sqrt(pot_noise) * normal(0, 1, len(modulada))

# Señal modulada con ruido
modulada_ruido = modulada + ruido

# Graficar señal modulada con ruido
plt.figure(figsize=(10,4))
plt.plot(t[:1000], modulada_ruido[:1000])
plt.title(f'Señal Modulada con Ruido (SNR = {SNR_dB} dB)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()
plt.show()

def atenuar(senal, factor):
    """
    Atenúa la señal multiplicando por un factor < 1.
    """
    return factor * senal

def distorsionar(senal, distor_factor, freq_dist, t):
    """
    Agrega una distorsión armónica a la señal.
    distor_factor: amplitud de la distorsión.
    freq_dist: frecuencia de la distorsión (Hz).
    """
    distor = distor_factor * np.sin(2 * np.pi * freq_dist * t)
    return senal + distor

# Parámetros de atenuación y distorsión
factor_atenuacion = 0.5       # Reduce la amplitud a la mitad
factor_distorsion = 0.1       # Amplitud de la distorsión
freq_distorsion = 300         # Frecuencia de la distorsión en Hz

# Aplicar atenuación y distorsión a la señal modulada con ruido
senal_modificada = atenuar(modulada_ruido, factor_atenuacion)
senal_modificada = distorsionar(senal_modificada, factor_distorsion, freq_distorsion, t)

# Graficar la señal modificada
plt.figure(figsize=(10,4))
plt.plot(t[:1000], senal_modificada[:1000])
plt.title('Señal Modulada con Ruido, Atenuación y Distorsión')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()
plt.show()
