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
    rojo.off()
    untime.sleep(3)
    verde.off()
    Anarillo.off()
    rojo.on()
    untime.sleep(5)
    verde.off()
    Amarillo.on()
    rojo.on()
    untime.sleep(2)
    
    