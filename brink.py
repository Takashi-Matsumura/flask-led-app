import machine
import utime

led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.value(1)  # ON
    utime.sleep(0.5)
    led.value(0)  # OFF
    utime.sleep(0.5)