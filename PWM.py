from machine import Pin, PWM

verde = PWM(Pin(15),60)
Amarillo = Pin(15, Pin.OUT)
Rojo = Pin(16, Pin.OUT)

verde.duty(50)
rojo.on()
rojo.value(1)
rojo.value(true)
    
    