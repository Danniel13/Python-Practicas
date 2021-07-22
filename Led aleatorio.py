from machine import Pin
import utime

rojo = Pin(2, Pin.OUT)
verde = Pin(15, Pin.OUT)
azul = Pin(16, Pin.OUT)
while True:
    rojo.off()
    azul.off()
    verde.on()
    utime.sleep(1)
    verde.off()
    azul.off()
    rojo.on()
    utime.sleep(1)
    rojo.off()
    verde.off()
    azul.on()
    utime.sleep(1)
    rojo.on()
    verde.on()
    azul.on()
    utime.sleep(1)