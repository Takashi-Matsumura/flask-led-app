import socket
import network
from machine import Pin

led = Pin("LED", Pin.OUT)
ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print("Connecting to WiFi...")
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

ip = wlan.ifconfig()[0]
print("Connected! IP Address:", ip)

s = socket.socket()
s.bind(('0.0.0.0', 80))
s.listen(1)
print("HTTP server is running on port 80")

while True:
    try:
        cl, addr = s.accept()
        req = cl.recv(1024).decode()
        print(f"Request from {addr}: {req}")

        if 'GET /led/on' in req:
            led.value(1)
        elif 'GET /led/off' in req:
            led.value(0)

        cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nOK")
        cl.close()
    except Exception as e:
        print("通信中に例外が発生：", e)