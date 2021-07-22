from machine import Pin
import utime

verde = Pin(2, Pin.OUT)
Amarillo = Pin(15, Pin.OUT)
Rojo = Pin(16, Pin.OUT)
while true:
    verde.on()
    Amarillo.off()
    rojo.off()
    utime.sleep(5)
    verde.off()
    Amarillo.on()
    