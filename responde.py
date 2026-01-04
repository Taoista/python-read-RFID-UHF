import serial
import time

ser = serial.Serial("COM3", 115200, timeout=0.5)

cmd = bytes.fromhex("BB 00 22 00 00 22 7E")

while True:
    ser.write(cmd)
    data = ser.read(128)
    if data:
        print("RX:", data.hex(" ").upper())
    time.sleep(0.3)
