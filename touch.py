from machine import Pin, TouchPad
import utime

def main():
    entradaT = TouchPad(Pin(12))
    entradaT.config(600)

"""
while True:
    print(entradaT.read())
    utime.sleep(0.5)
"""

   with open("logs.txt","a") as file:
        print(file.read())

if __name__=="__main__":
    main()