from machine import Pin
import utime
entrada = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    utime.sleep(1)
    datos = entrada.value()
    print(datos)
    