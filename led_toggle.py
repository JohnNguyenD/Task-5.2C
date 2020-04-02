from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)


## hardware
led1 = LED(18)
led2 = LED(12)
led3 = LED(13)

## GUI Definitions
##Led
win = Tk()
win.title("Led Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

##Event Function
def led1Toggle():
    if led1.is_lit:
        led1.off()
        LedButton1['text'] = "Turn LED1 on"
    else:
        led1.on()
        LedButton1['text'] = "Turn LED1 off"
 
def led2Toggle():
    if led2.is_lit:
        led2.off()
        LedButton2['text'] = "Turn LED2 on"
    else:
        led2.on()
        LedButton2['text'] = "Turn LED2 off"
        
def led3Toggle():
    if led3.is_lit:
        led3.off()
        LedButton3['text'] = "Turn LED3 on"
    else:
        led3.on()
        LedButton3['text'] = "Turn LED3 off"
##Widgets
LedButton1 = Button(win, text = "Turn Led1 on", font = myFont, command = led1Toggle, bg = 'bisque2', height = 1 , width = 80)
LedButton1.grid(row = 0, column = 1)

LedButton2 = Button(win, text = "Turn Led2 on", font = myFont, command = led2Toggle, bg = 'bisque2', height = 1 , width = 80)
LedButton2.grid(row = 1, column = 1)

LedButton3 = Button(win, text = "Turn Led3 on", font = myFont, command = led3Toggle, bg = 'bisque2', height = 1 , width = 80)
LedButton3.grid(row = 2, column = 1)



