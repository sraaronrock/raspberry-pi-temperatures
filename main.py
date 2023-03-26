import signal
import time

# Función que maneja la señal SIGINT (control + c)
def signal_handler(sig, frame):
    print('\nPrograma detenido')
    exit(0)

# Asignar la función de manejo de señales al SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Bucle while infinito
while True:
    # Abrir el archivo de temperatura
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
        # Leer la temperatura en miligrados Celsius
        temp = int(f.read()) / 1000.0

    # Mostrar la temperatura por consola
    print(f'Temperatura: {temp:.1f}°C')

    # Esperar 10 segundos
    time.sleep(10)
