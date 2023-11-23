import machine
from machine import UART
import time

LED_PIN = 15



led = machine.Pin(LED_PIN, machine.Pin.OUT)

led.off()


# Crear un objeto para el puerto serial
uart = machine.UART(0, baudrate=9600)

# variable para almacenar el dato recibido por el puerto serial
dato = b''

while True:
    # Leer el dato recibido por el puerto serial si hay alguno disponible
    if uart.any():
        dato = uart.read(1)
        
        # Comparar el dato con las opciones posibles
        if dato == b'A': # Si se recibe la letra A, encender el led
            led.on()
        elif dato == b'B': # Si se recibe la letra B, apagar el led
            led.off()
        else: # Si se recibe cualquier otro dato, apagar 
            led.off()
    
  
    # Esperar un segundo antes de repetir el ciclo
    time.sleep(1)
