import serial
import time

PORT = "COM3"        # cambia si es necesario
BAUDRATE = 115200

def checksum(data):
    return sum(data) & 0xFF

ser = serial.Serial(PORT, BAUDRATE, timeout=0.5)
time.sleep(1)

# READ EPC
cmd = [
    0xBB, 0x00, 0x22,
    0x00, 0x00
]

crc = checksum(cmd[1:])
cmd.append(crc)
cmd.append(0x7E)

print("TX READ:", " ".join(f"{b:02X}" for b in cmd))
ser.write(bytes(cmd))

time.sleep(0.3)
resp = ser.read(200)

if resp:
    print("RX:", " ".join(f"{b:02X}" for b in resp))
else:
    print("RX: (sin respuesta)")

ser.close()

