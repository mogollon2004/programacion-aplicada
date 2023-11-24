from machine import Pin
from utime import sleep

# Definir los pines de los LEDs y el pin del pulsador
led_pins = (15, 2, 4, 5, 18, 19, 21, 22)
leds = [Pin(pin, Pin.OUT) for pin in led_pins]
pulsador = Pin(14, Pin.IN, Pin.PULL_UP)  # Pin del pulsador con resistencia de pull-up

# Función para parpadear un LED
def parpadear_led(led, duracion=0.3):
    led.on()
    sleep(duracion)
    led.off()
    sleep(duracion)

# Función para encender todos los LEDs al mismo tiempo
def encender_todos_leds():
    for led in leds:
        led.on()

# Bucle principal
while True:
    if not pulsador.value():  # Si el pulsador se presiona (nivel bajo)
        encender_todos_leds()
        sleep(1)  # Espera 1 segundo antes de apagar los LEDs
    else:
        for led in leds:
            parpadear_led(led)  # Parpadear todos los LEDs
